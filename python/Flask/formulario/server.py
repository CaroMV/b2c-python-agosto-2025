from flask import Flask, render_template, request, redirect, session

app= Flask(__name__)

app.secret_key='CualquierClave'

@app.route('/')
def inicio():
    print('Se está renderizando el formulario')
    listado_estudiantes = [

       {'nombre': 'Florencia', 'edad': 25},

       {'nombre': 'Valentina', 'edad': 30},

       {'nombre': 'José', 'edad': 27},

       {'nombre': 'Patricio', 'edad': 21}

   ]
    
    
    return render_template('inicio.html', estudiantes=listado_estudiantes)

@app.route('/crear_contacto', methods=['POST'])
#/buscar?nombre=carolina
def crear_contacto():

    print('Se está procesando el formulario')
    print('Acá está el request')
    print(request.form)
    respuesta=request.form
    
    print("Session:")
    print(session)

    session['nombre_usuario']=respuesta['nombre']

    print("Session 2:")
    print(session)

    respuesta=request.form

    print(type(int(respuesta['edad'])))



    return redirect('/ruta_final')

@app.route('/ruta_final')
def ruta_final():
    print('request ruta final:')
    print(request.form)
    return 'Formulario Enviado'


if __name__=='__main__':
    app.run(debug=True)