from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
# to validate an email format
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# to secure password within db
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 

db = 'users'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.bands = []
        self.joined_bands = []

    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['confirm_password'] != user['password']:
            flash("Passwords must match.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form_data):
        is_valid = True
        user_in_db = User.get_by_email(form_data)
        if not user_in_db:
            flash("Invalid Email/Password")
            is_valid = False
        if not bcrypt.check_password_hash(user_in_db.password, form_data['password']):
            flash("Invalid Email/Password")
            is_valid = False
        return is_valid

    @classmethod
    def new_user(cls, data):
        query = "insert into users(first_name, last_name, email, password, created_at, updated_at) values(%(first_name)s, %(last_name)s, %(email)s, %(password)s, now(), now());"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        return cls(result[0])