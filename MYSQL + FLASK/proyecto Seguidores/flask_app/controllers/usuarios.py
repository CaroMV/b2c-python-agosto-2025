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

@app.route('/usuario/registro', methods=['POST'])
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
    
    datos_validados={
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'], 
        'email': request.form['email'],
        'password': pass_hasheada,
    }

    usuario_registrado = Usuario.save(datos_validados)
    
    #? Si quiero que el registro me logee al finalizar el proceso
    # session['usuario']= usuario_registrado
    # return redirect('/siguienteruta')
    return redirect('/')

@app.route('/usuario/login', methods=['POST'])
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


@app.route('/usuario/perfil/<int:id>')
def perfil_usuario(id):

    datos={
        'seguidor_id':id
    }

    dato_usuario={
        'id':id
    }
    usuario=Usuario.get_by_id(dato_usuario)
    
    lista_seguidores = Seguidor.get_seguidos_by_usuario(datos)

    print(lista_seguidores)

    return render_template('perfil_usuario.html', usuario=usuario, lista_seguidores=lista_seguidores)

