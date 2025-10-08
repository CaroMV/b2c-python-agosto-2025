from flask import Flask, render_template, request, redirect, session, flash

app=Flask(__name__)
app.secret_key='clave123'

usuarios=[]

@app.route('/')
def home():
    usuario = session.get('usuario')
    usuarios_registrados = session.get('usuarios', [])
    return render_template('index.html', usuario=usuario, total_usuarios=len(usuarios_registrados))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    #Si esta ruta está haciendo una solicitud de tipo POST, entonces proceso el formulario
    if request.method == 'POST':
        nombre=request.form['nombre']
        email=request.form['email']

        password=request.form['password']
        password_conf=request.form['password-conf']
        if password != password_conf:
            flash('Las contraseñas no coinciden')
        else:
            flash('Te has registrado Exitosamente')
            usuario={
            'nombre':nombre,
            'email':email,
            'password':password
            }
            flash('Inicia sesión en el login')
            usuarios.append(usuario)
            session['usuarios']=usuarios
            print(usuarios)

            return redirect('/login')
            
        print(request.form)
        print('Se está enviando información desde el formulario de registro')

    #Como no estoy recibiendo ninguna solicitud post, renderizo el formulario
    return render_template('registro.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email= request.form['email']
        password= request.form['password']
        print('sesion usuarios: ')
        print(session['usuarios'])
        print('___________________________')
        for usuario in session['usuarios']:
            print('diccionario usuario:')
            print(usuario)
            print('___________________________')
            if usuario['email'] == email  and usuario['password']==password:
                print('se encontró la coincidencia:')
                session['usuario']=usuario

                flash('Inicio de sesión exitoso')
                print(session)
                print('Inicio sesión exitoso')
                return redirect('/')
            else:
                print('contraseña / mail error')
                flash('El correo o la contraseña son incorrectos')

        #proceso el login

    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario')
    print(session)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)