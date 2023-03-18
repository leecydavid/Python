# model is everything happening in the backend - 
# anything we want to get done in sql we will manipulate it from this file

# import the function that will connect mysqlconnection.py to connectToMySQL 
    # this function allows us to connect mysql to the fron end(flask)
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja_model

# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    # the get_all is retrieving all info from the dojos table so we can start manipulating sql 
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        dojos = []
        # Create an empty list to append our instances
        # name this whatever the name is of one of your tables 

        if results:
            for u in results:
                new_dojo = cls(u)
                dojos.append(new_dojo)
            return dojos
    
    @classmethod
    def create (cls, data):
        query = "INSERT into dojos(name) VALUES(%(name)s);"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def display (cls, data):
        query = "SELECT * FROM dojos WHERE name= %(name)s"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def show(cls, id):
        data = {
        "id": id
        }

        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)

        if results:
            dojo = cls(results[0])

            ninjas = []
            for row in results: 
                ninjas_data = {
                    **row,
                    'id': row['ninjas.id'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at']
                }

                new_ninja = ninja_model.Ninja(ninjas_data)
                ninjas.append(new_ninja)

            dojo.ninjas = ninjas 

        return dojo
    





    
        
    
        

    












        # ninjas = []
        # if results:
        #     for row in results:
        #         dojo = cls(row)

        #         ninjas_data = {
        #             'id': row['ninja.id'],
        #             'first_name': row['ninjas.first_name'],
        #             'last_name': row['ninjas.last_name'],
        #             'age': row['ninjas.age'],
        #             'dojo_id': row['ninjas.dojo_id'],
        #             'created_at': row['ninjas.created_at'],
        #             'updated_at': row['ninjas.updated_at']
        #         }

        #         ninja = Ninja(ninja_data)

        #         dojo.creator = dojo 
        #         dojos.append(dojo)





            




    

    
        # ninjas = []
        # if results:
        #     for row in results:
        #         ninja = cls(row)

        #         ninjas_data = {
        #             'id': row['ninjas.id'],
        #             'first_name': row['ninjas.first_name'],
        #             'last_name': row['ninjas.last_name'],
        #             'age': row['ninjas.age'],
        #             'created_at': row['ninjas.created_at'],
        #             'updated_at': row['ninjas.updated_at'],
        #             'dojo_id': row['ninjas.dojo_id']
        #         }

        #         new_ninja = ninja_model.Ninja(ninjas_data)
        #         ninjas.append(new_ninja)

        #         dojo.ninjas = ninjas
        #         return dojo



        # if result:
        #     dojo = cls(result[0])
        #     ninjas = []

        #     for row in result:
        #         ninjas_data = {
        #             **row,
        #             'id': row['ninjas.id'],
        #             'created_at': row['created_at'],
        #             'updated_at': row['updated_at']
        #         }
        #         new_ninja = ninja_model.Ninja(ninjas_data)
        #         ninjas.append(new_ninja)

        #     dojo.ninjas = ninjas

        #     return dojo

    

    

    

# query = "SELECT first_name, last_name, age FROM ninjas JOIN dojos ON dojo_id = dojos.id WHERE dojos.id = %(dojos.id)s;"


        # if result: 
        #     dojo = cls(result[0])
        #     ninjas = []
        #     for row in result:
        #         ninjas_data = {
        #             **row
        #             'id': row['ninjas.id'],
        #             'created_at': row['created_at'],
        #             'updated_at': row['updated_at']
        #         }
        
        #     new_ninja = ninja_model.Ninja(ninjas_data)

        #     ninjas.append(new_ninja)

        #     dojo.ninjas = ninjas


    
