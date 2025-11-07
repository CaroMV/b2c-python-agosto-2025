from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.evento import Evento
from flask_app.models.usuario import Usuario



#Lista de eventos 
@app.route('/eventos')
def eventos():
    if 'usuario_id' not in session:
        return redirect('/')
    
    usuario= Usuario.get_by_id({'id':session['usuario_id']})
    lista_eventos = Evento.get_all()
    return render_template('eventos.html', lista_eventos=lista_eventos, usuario=usuario)



#nuevo evento: renderizar plantilla

@app.route('/nuevo_evento')
def nuevo_evento():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nuevo_evento.html', datos={})


#crear_evento: procesar la creacion de un evento
@app.route('/crear_evento', methods=['POST'])
def crear_evento():
    datos={
        'nombre_evento': request.form['nombre_evento'],
        'ubicacion': request.form['ubicacion'],
        'fecha': request.form['fecha'],
        'detalles': request.form['detalles'],
        'usuario_id':session['usuario_id']
    }
    if not Evento.validar_evento(datos):
        return render_template('nuevo_evento.html', datos=datos)
    
    Evento.save(datos)
    return redirect('/eventos')


#Ver evento : renderizado plantilla ver evento
@app.route('/ver_evento/<int:id>')
def ver_evento(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    evento = Evento.get_by_id({'id': id})
    dueño = Usuario.get_by_id({'id': evento.usuario_id})
    return render_template('ver_evento.html', evento=evento, dueño=dueño)

#editar evento : renderizar plantilla
@app.route('/editar_evento/<int:id>')
def editar_evento(id):
    if 'usuario_id' not in session:
        return redirect('/')   
    
    datos= Evento.get_by_id({'id':id})
    print(datos.nombre_evento)
    return render_template('editar_evento.html', datos=datos)



#actualizar_evento: procesar la edicion del evento
@app.route('/actualizar', methods=['POST'])
def actualizar():
    datos={
        'id':request.form['id'],
        'nombre_evento': request.form['nombre_evento'],
        'ubicacion': request.form['ubicacion'],
        'fecha': request.form['fecha'],
        'detalles': request.form['detalles'],
        'usuario_id':session['usuario_id']
    }
    if not Evento.validar_evento(datos):
        return redirect(f'/editar_evento/{datos.id}')
    Evento.update(datos)
    return redirect('/eventos')

#borrar evento