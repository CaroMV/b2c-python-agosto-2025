from flask_app import app 

from flask import render_template,redirect,request,session,flash

from flask_app.models.taco import Taco #Importamos la clase
from flask_app.models.restaurante import Restaurante

@app.route('/mostrar_restaurantes')
def mostrar_lista_restaurantes():
    todos_restaurantes = Restaurante.get_all()
    return render_template('crear_restaurante.html', todos_restaurantes= todos_restaurantes)

@app.route('/crear_restaurante', methods=['post'])
def crear_restaurante():
        datos = {
        "nombre":request.form['nombre'],
    }
        Restaurante.save(datos)
        return redirect('/mostrar_restaurantes')