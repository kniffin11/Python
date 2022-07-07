# original class file, all of the class stuff ie methods will be in this file, in the models folder
# dont forget to update the import on the corrresponding file within flask_app.models.class_file_name
# also dont forget to update the below import to the new location of mysqlconnection -- the config folder
from users_CRUD_mod.config.mysqlconnection import connectToMySQL

class Users_CR:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # use class methods to query databases
    @classmethod
    def get_all(cls):
        query = "select * from users;"
        # call to the db from mysql
        total_users = connectToMySQL('users').query_db(query)
        # create an empty list to store the data from the db
        users = []

        # for each index of total users, add the instance with all data to the list
        for user in total_users:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "select * from users where id = %(id)s;"
        # make a variable so that the id can be returned and stored
        user_from_data = connectToMySQL('users').query_db(query, data)
        # call upon the id
        return cls(user_from_data[0])
    
    @classmethod
    def save(cls, data):
        # this line of code will be ran in mysql, the values within {}'s are passed from data and the var_names originate from index_create.html -- the 'name' attributes within the form
        query = "insert into users(first_name, last_name, email, created_at) values(%(first_name)s, %(last_name)s, %(email)s, now());"
        # data is a dictionary from server.py
        return connectToMySQL('users').query_db(query, data) # this will return an int representing an id 

    @classmethod
    def update(cls, data):
        query = "update users set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s where id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "delete from users where id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)
