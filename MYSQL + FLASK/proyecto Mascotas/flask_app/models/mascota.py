from flask_app.config.mysqlconnection import connectToMySQL

class Mascota:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.tipo = data['tipo']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mascotas;"
        #SABEMOS que los SELECT retornan una LISTA DE DICCIONARIOS SIEMPRE
        resultados = connectToMySQL('primera_flask').query_db(query)

        mascotas = []
        for mascota in resultados:
            mascotas.append(cls(mascota))
        return mascotas


    # Guardar nueva mascota
    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at)
            VALUES ( %(nombre)s , %(tipo)s , %(color)s , NOW(), NOW());
        """
        return connectToMySQL('primera_flask').query_db(query, datos)
