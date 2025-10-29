from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.taco import Taco #Importamos la clase
from flask_app.models.restaurante import Restaurante

@app.route('/')
def index():
    todos_restaurantes = Restaurante.get_all()
    return render_template("index.html", todos_restaurantes=todos_restaurantes)

@app.route('/crear',methods=['POST'])
def crear():
    datos = {
        "tortilla":request.form['tortilla'],
        "guiso": request.form['guiso'],
        "salsa": request.form['salsa'],
        #Nuevo campo que viene de la relación entre taco y restaurante
        "restaurante_id": request.form['restaurante_id']
    }
    Taco.save(datos)
    return redirect('/tacos')

@app.route('/tacos')
def tacos():
    tacos = Taco.get_all()
    return render_template("resultados.html",todos_tacos = tacos)

@app.route('/mostrar/<int:taco_id>')
def detalle(taco_id):
    datos = {
        'id': taco_id
    }
    taco = Taco.get_one(datos)
    return render_template("detalle.html",taco = taco)

#Ruta encargada de renderizar plantilla:

@app.route('/editar/<int:taco_id>')
def editar(taco_id):
    
    datos = {
        'id': taco_id
    }

    taco = Taco.get_one(datos)
    return render_template("editar.html", taco = taco)

#Encargada de Procesar el método post que envía los datos nuevos
@app.route('/actualizar/<int:taco_id>', methods=['POST'])
def actualizar(taco_id):
    datos = {
        'id': taco_id,
        "tortilla":request.form['tortilla'],
        "guiso": request.form['guiso'],
        "salsa": request.form['salsa']
    }
    Taco.update(datos)
    return redirect(f"/mostrar/{taco_id}")

@app.route('/borrar/<int:taco_id>')
def borrar(taco_id):
    datos = {
        'id': taco_id,
    }
    Taco.delete(datos)
    return redirect('/tacos')