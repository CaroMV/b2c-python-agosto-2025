from flask_app.config.mysqlconnection import connectToMySQL

class Seguidor:
    def __init__(self, data):
        self.id= data['id']
        self.usuario_id= data['usuario_id']
        self.seguidor_id= data['seguidor_id']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    
    # ===== CRUD =====

    # ----- CREAR -----
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO seguidores (usuario_id, seguidor_id) VALUES ( %(usuario_id)s,%(seguidor_id)s )
                """
        return connectToMySQL('registro_seguidores_db').query_db(query, data)
    
    # ----- READ -----
    # en esta seccion tenemos las querys de tipo SELECT

    @classmethod
    def get_seguidos_by_usuario(cls,data):
        query = """
                SELECT * FROM usuarios
                JOIN seguidores ON seguidores.seguido_id= usuarios.id
                where seguidores.seguidor_id= %(seguidor_id)s;
            """
        resultados = connectToMySQL('registro_seguidores_db').query_db(query,data)
        if len(resultados) ==0:
            print('Este usuario no sigue a nadie')
            return []
        
        #Si queremos que la lista de usuarios seguidos esté en la instancia usuarios

        # from flask_app.models.usuario import Usuario
        # seguidos = [Usuario(row) for row in resultados]
        # return seguidos
    

    # ---- Delete -----
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM seguidores where seguidor_id = %(seguidor_id)s, seguido_id=%(seguido_id)s
            """
        return connectToMySQL('registro_seguidores_db').query_db(query,data)

    #? ==== VALIDACIONES =====
    
    


    
