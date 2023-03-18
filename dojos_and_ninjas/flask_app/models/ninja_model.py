from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# this class is getting all the variables in the ninjas table
    # always set this class to Upper case to whatever the name is of one of your table names but singular
        # take in self and data(with data you can transfer the table variables and target them in different ways when we refer back to data, you'll see)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # refer back to wrlds assignment on how to write sql queries!!!!
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        ninjas = []
        # change name
        # Create an empty list to append our instances

        # Iterate over the database results and create instances of friends with cls.
        if results:
            for u in results:
                new_ninja= cls(u)
                # change new_ninja
                ninjas.append(new_ninja)
                # change name of user (ninja in this case)
            return ninjas
            # return the name of whatever is = []()
        # you can copy and paste this whole thing BUT change the names after results
        
    @classmethod
    def new_create(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def save(cls, data):
        query = "SELECT * FROM ninjas WHERE name = %(name)s"
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return result
    

        

