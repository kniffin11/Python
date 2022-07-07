# all of the class stuff ie methods will be in this file, in the models folder
# dont forget to update the import on the corrresponding file within flask_app.models.class_file_name
# also dont forget to update the below import to the new location of mysqlconnection -- the config folder
from flask_app.config.mysqlconnection import connectToMySQL
# import the ninja model to associate these together
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "select * from dojos;"
        # call to the db from mysql
        total_dojos = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # create an empty list to store the data from the db
        dojos = []

        # for each index of total users, add the instance with all data to the list
        for dojo in total_dojos:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "insert into dojos ( name, created_at, updated_at) values (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        # this selects all of the ninjas with the same foreign dojo id 
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        list_of_ninjas = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        # list_of_ninjas will be a list of all the ninjas in the dojo
        list = cls(list_of_ninjas[0]) 
        # list = list_of_ninjas[0]
        for a_ninja in list_of_ninjas: 
            ninja_data = {
                # syntax: var_name : increment_from_loop['table_from_db_name.row_name_from_db']
                # when theres two variables with the same name you have to use table_name.variable_name to spcify which is used
                "id" : a_ninja["ninjas.id"],
                "first_name" : a_ninja["first_name"],
                "last_name" : a_ninja["last_name"],
                "age" : a_ninja["age"],
                # "dojo_id" : data["dojo_id"],
                "created_at" : a_ninja["ninjas.created_at"],
                "updated_at" : a_ninja["ninjas.updated_at"]
            }

            # var_name = model_file_name.class_name(data_for_init)
            ninja_instance = ninja.Ninja(ninja_data)
            # add this to the list  
            list.ninjas.append(ninja_instance)
        return list_of_ninjas

    @classmethod
    def add(cls, data):
        query = "insert into dojos(name, created_at) values(%(name)s, now());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)