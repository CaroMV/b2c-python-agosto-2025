from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_app.models.seguidor import Seguidor
from flask_bcrypt import Bcrypt

bcrypt= Bcrypt(app)

#

#!------- RUTA DE RENDERIZADO DE FORMULARIO DE REGISTRO Y FORMULARIO DE LOGIN
@app.route('/')
def login_registro_render():

    return render_template('inicio_login_registro.html')

@app.route('/usuario/registro')
def usuario_registro():
    pass_hasheada=bcrypt.generate_password_hash(request.form['password'])

    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'], 
        'email': request.form['email'],
        'password': pass_hasheada,
        'confirmar_password': request.form['confirmar_password'],
    }

    if not Usuario.validacionRegistroUsuario(datos):
        print("Error en la validación de datos")
        return redirect('/')
    
    usuario_registrado = Usuario.save(datos)
    
    #? Si quiero que el registro me logee al finalizar el proceso
    # session['usuario']= usuario_registrado
    # return redirect('/siguienteruta')
    return redirect('/')

@app.route('/usuario/login')
def login():
    
    datos={
        'email': request.form['email'],
        'password': request.form['password']
    }

    usuario= Usuario.get_by_email(datos['email'])

    if not usuario or not bcrypt.check_password_hash(usuario.password, datos['password']):
        flash("Usuario no encontrado o contraseña incorrecta")

    session['usuario']=usuario

    return redirect('/siguienteruta')

