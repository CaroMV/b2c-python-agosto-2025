from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


db= "eventos_db"

class Evento:
    def __init__(self, data):
        self.id = data['id']
        self.nombre_evento = data['nombre_evento']
        self.ubicacion = data['ubicacion']
        self.fecha = data['fecha']
        self.detalles = data['detalles']
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.usuario_id=data["usuario_id"]

    @classmethod
    def save(cls, datos):
        query= """
                INSERT INTO eventos (nombre_evento, ubicacion, fecha, detalles, usuario_id) VALUES ( %(nombre_evento)s, %(ubicacion)s, %(fecha)s, %(detalles)s, %(usuario_id)s)
        """
        return connectToMySQL(db).query_db(query, datos)

    @classmethod
    def get_all(cls):
        query=""" 
                SELECT * FROM eventos
            """
        resultados = connectToMySQL(db).query_db(query)
        eventos=[]
        for e in resultados:
            eventos.append(cls(e))
        return eventos
    
    @classmethod
    def get_by_id(cls, datos):
        query= """
                SELECT * FROM eventos WHERE id = %(id)s
            """
        resultados = connectToMySQL(db).query_db(query, datos)
        
        return cls(resultados[0])

    @classmethod
    def update(cls, datos):
        query = """
                UPDATE eventos
                SET nombre_evento=%(nombre_evento)s, ubicacion = %(ubicacion)s, fecha=%(fecha)s, detalles = %(detalles)s
                WHERE id = %(id)s
        """
        return connectToMySQL(db).query_db(query, datos)

    # ============= VALIDACION ============
    @staticmethod
    def validar_evento(datos):
        es_valido = True

        if len(datos['nombre_evento']) < 3:
            flash('El Nombre del evento debe tener al menos 3 caracteres', 'crear_evento')
            es_valido = False

        if len(datos['ubicacion']) < 3:
            flash('La ubicacion debe tener al menos 3 caracteres', 'crear_evento')
            es_valido = False
        
        if len(datos['detalles']) < 3:
            flash('Los detalles debe tener al menos 3 caracteres', 'crear_evento')
            es_valido = False



        return es_valido