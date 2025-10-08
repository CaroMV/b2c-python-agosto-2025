#zona de importaciones
from flask import Flask, render_template, redirect, session

#inializacion de la clase Flask, vamos a crear la instancia "app"
app=Flask(__name__)


#Zona de rutas
#decoradores para establecer rutas
@app.route('/')
def hola_mundo():

    color="red"
    num=3
    return render_template('index.html', color=color, num=num)


@app.route('/juego/<int:num>')
def nivel2(num):

    color="red"
    return render_template('index.html', color=color, num=num)

@app.route('/juego/<int:num>/<color>')
def nivel3(num, color):
    return render_template('index.html', color=color, num=num)

#Zona de ejecución
if __name__=="__main__":
    app.run(debug=True)