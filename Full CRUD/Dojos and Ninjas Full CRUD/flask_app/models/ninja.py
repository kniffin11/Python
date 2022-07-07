# all of the class stuff ie methods will be in this file, in the models folder
# dont forget to update the import on the corrresponding file within flask_app.models.class_file_name
# also dont forget to update the below import to the new location of mysqlconnection -- the config folder
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        # self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def new_ninja(cls, data):
        # this gets ran in mysql
        query = "insert into ninjas(first_name, last_name, age, dojo_id, created_at) values(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, now());"
        # this runs the duery with teh information from data and ninjas.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

# to check for valid inputs
    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        if len(ninja['first_name']) < 2:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(ninja['last_name']) < 2:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if int(ninja['age']) < 18:
            flash("Age must be 18 or older.")
            is_valid = False
        return is_valid

