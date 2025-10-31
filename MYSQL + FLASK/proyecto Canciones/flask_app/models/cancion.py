from flask_app.config.mysqlconnection import connectToMySQL

class Cancion:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.favoritos=[]

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO canciones (titulo, artista) VALUES(%(titulo)s, %(artista)s);"
        return connectToMySQL('esquema_canciones').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        resultados = connectToMySQL('esquema_canciones').query_db(query)
        canciones = []
        for cancion in resultados:
            canciones.append(cls(cancion))
        return canciones
    
    @classmethod
    def get_by_id(cls,datos):
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        resultados = connectToMySQL('esquema_canciones').query_db(query,datos)

        return cls(resultados[0])


    #Metodo especializado para obtener los usuarios que tienen esta cancion como favorita
    @classmethod
    def get_usuarios_favoritos(cls, datos):
        query= """
            SELECT * FROM usuarios
            LEFT JOIN favoritos ON usuarios.id=favoritos.usuario_id
            WHERE favoritos.cancion_id = %(id)s
        """

        return connectToMySQL('esquema_canciones').query_db(query,datos)

    
    