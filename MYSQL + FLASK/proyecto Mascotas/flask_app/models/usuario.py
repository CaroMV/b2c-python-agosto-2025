from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        #SABEMOS que los SELECT retornan una LISTA DE DICCIONARIOS SIEMPRE
        resultados = connectToMySQL('primera_flask').query_db(query)

        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios


    # Guardar un nuevo usuario
    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, created_at, updated_at)
            VALUES ( %(nombre)s , %(apellido)s , NOW(), NOW());
        """
        return connectToMySQL('primera_flask').query_db(query, datos)

    @classmethod 
    def get_by_id(cls, datos):

        query = """
            SELECT * from usuarios where id = %(id)s
        """
        resultado=connectToMySQL('primera_flask').query_db(query, datos)

        return resultado[0]

    @classmethod

    def delete(cls, datos):
        query = """
            DELETE FROM usuarios where id = %(id)s
        """
        return connectToMySQL('primera_flask').query_db(query, datos)