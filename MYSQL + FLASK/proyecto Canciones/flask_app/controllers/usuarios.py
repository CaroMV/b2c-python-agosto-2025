from flask_app import app

from flask import render_template, request, redirect, session

from flask_app.models.usuario import Usuario
from flask_app.models.cancion import Cancion


#página 1: donde se renderiza el formulario de nuevos usuarios y ver los que están creados
@app.route('/usuarios')
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template('usuarios.html', todos_los_usuarios=todos_los_usuarios)

@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"], 
        "email": request.form["email"],
        "password": request.form["password"] 
    }
    Usuario.save(data)

    return redirect('/usuarios')

@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    data={
        "id":id
    }
    usuario= Usuario.get_by_id(data)
    favoritos = Usuario.get_favoritos(data)
    todas_las_canciones = Usuario.get_favoritos(data)

    return render_template('detalle_usuario.html', usuario=usuario, favoritos=favoritos, todas_las_canciones=todas_las_canciones)

@app.route('/usuarios/<int:id>/agregar_favorito')
def usuario_agregar_favoritos(id):
    print('REQUEST')
    print(request.form)
    data={
        "usuario_id": id,
        "cancion_id": request.form["cancion_id"]
    }
    Usuario.add_favoritos(data)
    return redirect(f'/usuarios/{id}')