from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id= data['id']
        self.nombre=data['nombre']
        self.apellido= data['apellido']
        self.email=data['email']
        self.password= data['password']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    
    # ===== CRUD =====

    # ----- CREAR -----
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO usuarios (nombre, apellido, email, password) VALUES ( %(nombre)s,%(apellido)s,%(email)s,%(password)s )
                """
        return connectToMySQL('registro_seguidores_db').query_db(query, data)
    
    # ----- READ -----
    # en esta seccion tenemos las querys de tipo SELECT

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('registro_seguidores_db').query_db(query)

        usuarios = []
        for u in resultados:
            usuarios.append(cls(u))
        return usuarios
    @classmethod
    def get_by_email(cls, data):
        query = """
                SELECT * FROM usuarios WHERE email = %(email)s
                """
        resultados = connectToMySQL('registro_seguidores_db').query_db(query,data)

        if len(resultados) ==0:
            print('No hay un usuario con este email')
            return False
        return cls(resultados[0])
    

    #? ==== VALIDACIONES =====
    



    
