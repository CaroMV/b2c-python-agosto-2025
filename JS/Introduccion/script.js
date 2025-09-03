// Para poder generar un espacio en la memoria de nuestro computador, vamos a generar una variable
// Ese espacio en memoria tiene un nombre, y ese nombre es el nombre de la variable

//Palabra reservada var:
var nombre = 'valor'
console.log('Variable nombre 1:',nombre)

nombre = 'valor2'
console.log('Variable nombre 2:',nombre)
//Console.log nos permite ver un mensaje en la consola
console.log('hola')
console.log(nombre)

//palabra reservada let
//variables que yo quiera modificar a lo largo del codigo
let edad = 30


//CONST
//variables que no queramos modificar a lo largo codigo

const nombreCompleto = 'Carolina Moreno'


let cantidad_estudiantes = 6+1
console.log('Cantidad de Estudiantes',cantidad_estudiantes)


const nombreEstudiante = 'Angel'
const apellidoEstudiante = 'Alvis'

console.log(nombreEstudiante, apellidoEstudiante)

// anti ejemplo: 
console.log(nombreEstudiante)


//Operaciones Combinadas
let totalCompra = 0

totalCompra= totalCompra+5
totalCompra= totalCompra+10
totalCompra+=20

console.log('Total de Compra',totalCompra)


let texto = 'Erase una vez,'
texto+=' un pueblo abandonado,'

console.log('Texto:', texto)