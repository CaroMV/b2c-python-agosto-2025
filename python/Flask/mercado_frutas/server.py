from flask import Flask, render_template, request, redirect, session

app= Flask(__name__)

app.secret_key="llaveProyecto"

lista_frutas=[
    {'nombre':'Fresas', 'imagen':'fresas.png'},
    {'nombre':'Frambuesa', 'imagen':'frambuesas.png'},
    {'nombre':'Manzana', 'imagen':'manzana.jpg'},
]

@app.route('/')
def inicio():

    return render_template('index.html', lista_frutas=lista_frutas)

@app.route('/crear_pedido', methods=['POST'])
def crear_pedido():
    print(request.form)

    info_formulario=request.form

    session['fresas']=info_formulario['Fresas']
    session['frambuesas']=info_formulario['Frambuesa']
    session['manzana']=info_formulario['Manzana']
    session['nombre']=info_formulario['nombre']
    session['apellido']=info_formulario['apellido']
    session['email']=info_formulario['email']

    return redirect('/resumen_pedido')

@app.route('/resumen_pedido')
def resumen_pedido():
    return render_template('resumen_pedido.html',session=session)

if __name__=='__main__':
    app.run(debug=True)