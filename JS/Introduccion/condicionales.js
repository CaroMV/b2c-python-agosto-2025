console.log('Inicio')
// La estructura de control de flujo if es una condicional, que ejecuta un bloque de codigo cuando LA CONDICION SEA VERDADERA
let condicion = false

if(condicion){
    console.log('Proceso Alternativo')
}
//comparaciones son booleanos / operaciones logicas
console.log(5>=5)
console.log(5!=="5")



console.log('Proceso')

console.log('Final')



let edad = 'edad'

if (edad>=18){
    console.log('Eres mayor de edad')
} else if (edad<18){
    console.log('Eres menor de edad')
} else{
    console.log('No has ingresado una edad valida')
}


// Operadores logicos

// nos permiten evaluar 2 condiciones

// Operador AND && 

let condicion1= false
let condicion2= false

console.log('Operador &&:', condicion1 && condicion2)

// Operador OR ||

console.log('Operador || OR: ', condicion1 || condicion2)


// Operador Módulo (%)

console.log('Operador Modulo:', 16%8)