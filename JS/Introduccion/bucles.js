// Bucles 
// bloques de codigo que se repiten

// for <- Lo utilizaremos cuando SEPAMOS CUANTAS VECES SE TIENE QUE REPETIR EL BLOQUE 

// while <- Lo utilizaremos cuando NO sepamos cuantas veces se tiene que repetir y el número de repeticiones depende de un 'estado' o factor externo

for (let i = 10; i>=0; i--){
    // bloque de codigo que se ejecuta
    console.log(i)
}

let cantidadDeProducto= 100

while(cantidadDeProducto>0){
    console.log('Ordenando producto...')
    cantidadDeProducto-=10
    console.log('Haciendo paquete de 10...')
    console.log(cantidadDeProducto)
}