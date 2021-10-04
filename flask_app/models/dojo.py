from flask_app.config.MySQLConnection import connectToMySQL
from .ninja import Ninja #podria dar error por la referencia de la carpeta

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db( query )
        print(results)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        print(dojos)
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL( 'dojos_ninjas' ).query_db( query, data )
        return result


    @classmethod
    def one_dojo_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(ninja) )
        return dojo
    