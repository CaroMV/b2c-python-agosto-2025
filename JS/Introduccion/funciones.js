// Bloques de código reutilizables

function nombreDeLaFuncion(parametros){


}


function mensajeBienvenida(){
    console.log('Bienvenido')
}

function mensajeBienvenidaPersonalizado(nombrePersona){
    console.log('Bienvenido,', nombrePersona)

    return 'Bienvenido, '+ nombrePersona
}

mensajeBienvenida()
mensajeBienvenidaPersonalizado('Carolina')

let mensaje1= mensajeBienvenida()
let mensaje2= mensajeBienvenidaPersonalizado('Carolina')

console.log('Mensaje 1:', mensaje1,'Mensaje 2:', mensaje2,)