from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.favoritos=[]

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, email, password) VALUES(%(nombre)s, %(email)s, %(password)s);"
        return connectToMySQL('esquema_canciones').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('esquema_canciones').query_db(query)
        usuarios = []
        for c in resultados:
            usuarios.append(cls(c))
        return usuarios
    
    @classmethod
    def get_by_id(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultados = connectToMySQL('esquema_canciones').query_db(query,datos)

        return cls(resultados[0])


    @classmethod
    def get_favoritos(cls, datos):
        query= """
            SELECT * from canciones 
            LEFT JOIN favoritos ON canciones.id = favoritos.cancion_id
            WHERE favoritos.usuario_id = %(id)s
        """

        return connectToMySQL('esquema_canciones').query_db(query,datos)
    
    
    @classmethod
    def get_no_favoritos(cls, datos):
        #Arreglar query
        query = """
                SELECT canciones.* FROM canciones 
                LEFT JOIN favoritos 
                    ON canciones.id = favoritos.cancion_id 
                    AND favoritos.usuario_id = %(id)s
                WHERE favoritos.usuario_id IS NULL;
            """

        return connectToMySQL('esquema_canciones').query_db(query,datos)


    @classmethod
    def add_favoritos(cls, datos):
        query = "INSERT INTO favoritos (usuario_id, cancion_id) VALUES(%(usuario_id)s, %(cancion_id)s);"
        return connectToMySQL('esquema_canciones').query_db(query, datos)
        
    
    