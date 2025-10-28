from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.usuario import Usuario

@app.route("/usuarios")
def usuarios():
    lista_usuarios = Usuario.get_all()
    return render_template("info-usuarios.html", lista_usuarios=lista_usuarios)

@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
    }
    Usuario.save(datos)
    return redirect('/usuarios')

@app.route('/eliminar_usuario/<int:id>')
def eliminar_usuario(id):
    datos = {"id": id}
    #quién se eliminó
    usuario_a_eliminar = Usuario.get_by_id(datos)
    #eliminar un usuarios en especifico
    Usuario.delete(datos)
    print(usuario_a_eliminar)
    return redirect('/usuarios')