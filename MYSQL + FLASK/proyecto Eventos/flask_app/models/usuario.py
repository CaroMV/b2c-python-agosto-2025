from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt

import re

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')


db = 'eventos_db'


class Usuario:
    def __init__(self,data):
        self.id=data["id"]
        self.nombre=data["nombre"]
        self.apellido=data["apellido"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def save(cls, datos):
        query= """
                INSERT INTO usuarios (nombre, apellido, email, password) VALUES ( %(nombre)s, %(apellido)s, %(email)s, %(password)s)
        """
        return connectToMySQL(db).query_db(query, datos)
    
    @classmethod
    def get_by_email( cls, datos):
        query= """
                SELECT * FROM usuarios where email = %(email)s
        """
        resultados = connectToMySQL(db).query_db(query, datos)
        
        if len(resultados) <1:
            return False
        
        return cls(resultados[0])
    
    @classmethod
    def get_by_id(cls, datos):
        query= """
                SELECT * FROM usuarios WHERE id = %(id)s
            """
        resultados = connectToMySQL(db).query_db(query, datos)
        
        return cls(resultados[0])
    
    # ============= VALIDACION ============
    @staticmethod
    def validar_registro(datos):
        es_valido = True

        if len(datos['nombre']) < 2:
            flash('El nombre debe tener al menos 2 caracteres', 'registro')
            es_valido = False

        if len(datos['apellido']) < 2:
            flash('El apellido debe tener al menos 2 caracteres', 'registro')
            es_valido = False

        if not EMAIL_REGEX.match(datos['email']):
            flash('Formato de email inválido', 'registro')
            es_valido = False

        if Usuario.get_by_email({'email': datos['email']}):
            flash('El email ya se encuentra registrado', 'registro')
            es_valido = False

        if datos['password'] != datos['confirmacion']:
            flash('Las contraseñas no coinciden', 'registro')
            es_valido = False

        if len(datos['password']) < 8:
            flash('La contraseña debe tener al menos 8 caracteres', 'registro')
            es_valido = False

        return es_valido

    

    @staticmethod
    def validar_login(datos):
        usuario = Usuario.get_by_email({'email': datos['email']})
        if not usuario:
            flash('Email no registrado', 'login')
            return False
        if not bcrypt.check_password_hash(usuario.password, datos['password']):
            flash('Contraseña incorrecta', 'login')
            return False
        return usuario