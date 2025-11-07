from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_app import bcrypt

@app.route('/')
def inicio():
    return render_template('index.html', datos={})

@app.route('/registrar', methods=['POST'])
def registrar():
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirmacion': request.form['confirmacion']
    }

    if not Usuario.validar_registro(datos):

        return render_template('index.html', datos=datos)

    #generar hash solo en validacion
    password_hash = bcrypt.generate_password_hash(request.form['password'])

    datos_validados = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': password_hash
    }

    usuario_id = Usuario.save(datos_validados)
    session['usuario_id'] = usuario_id

    return redirect('/eventos')


@app.route('/login', methods=['POST'])
def login():
    datos= {
        'email': request.form['email'],
        'password': request.form['password'],
    }
    usuario_logeado = Usuario.validar_login(datos)

    if not usuario_logeado:
        return redirect('/')
    
    session['usuario_id']= usuario_logeado.id

    return redirect('/eventos')

#Logout

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')