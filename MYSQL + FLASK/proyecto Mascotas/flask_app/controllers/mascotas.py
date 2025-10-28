from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.mascota import Mascota

@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", todas_mascotas=mascotas)

@app.route("/crear_mascota", methods=['POST'])
def crear_mascota():
    datos = {
        "nombre": request.form['nombre'],
        "tipo": request.form['tipo'],
        "color": request.form['color']
    }
    Mascota.save(datos)
    return redirect('/')
