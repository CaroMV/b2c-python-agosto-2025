#zona de importaciones
from flask import Flask, render_template

#inializacion de la clase Flask, vamos a crear la instancia "app"
app=Flask(__name__)


#Zona de rutas
#decoradores para establecer rutas
@app.route('/')
def hola_mundo():
    return render_template('index.html')

@app.route('/otra_ruta')
def otra_ruta():
    return 'Esta es otra página de mi server web'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Bienvenido {nombre}'

@app.route('/saludo/<nombre>/<color>')
def saludo_color(nombre,color):
    return f'Bienvenido {nombre}, tu color favorito es: {color}'

@app.route('/<nombre>/<int:numero>')
def nombre_multiplicado(nombre, numero):
    return f'Hola {nombre} '*numero

@app.route('/plantilla')
def plantilla():
    frase="Confía en ti mismo/a, porque eres capaz de lograr lo que te propongas"
    return render_template('primera_plantilla.html', frase_motivacional=frase)


#Zona de ejecución
if __name__=="__main__":
    app.run(debug=True)