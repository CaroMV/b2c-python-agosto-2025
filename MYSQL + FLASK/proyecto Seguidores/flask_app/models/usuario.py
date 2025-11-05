from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.controllers.usuarios import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')



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

    @staticmethod

    #Validación nos retorna un booleano que nos dice si pasamos la validación (verdadoro ) o el formato o datos son invalidos (falso)
    def validacionRegistroUsuario(usuario):
        es_valido = True

        if len(usuario['nombre']) <3:
            flash("El nombre debe tener más de 3 caracteres")
            es_valido = False

        if len(usuario['apellido']) <3:
            flash("El apellido debe tener más de 3 caracteres")
            es_valido = False
        
        #Para validar un email uno requiere cierto formato
            #? emaildeprueba @ nombreserviciooempresa . com /cl / net 
            #? letras/numeros._ @ letras/numeros._ . letras
            #   carolina.moreno carolina_moreno10 CAROLINA.MORENO
        if not EMAIL_REGEX.match(usuario['email']):
            flash('Formato del email invalido')
            es_valido = False

        if Usuario.get_by_email(usuario['email']):
            flash("El email ya se encuentra registrado")
            es_valido = False
        
        if not bcrypt.check_password_hash(usuario['password'], usuario['confimar_password']):
            es_valido = False

        return es_valido


        

    
