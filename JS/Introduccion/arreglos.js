// Arreglos son un tipo de dato que me permite contener otros datos más simples (primarios / primitivos)
// es como una lista o matrices 

let arreglo = []
arreglo=['rosas', 'Margaritas', 'lirios']
// indice   0           1           2  
console.log(arreglo[2])
// .length me indica cuántos elementos hay en la lista

// El indice del último elemento se puede representar así:
// arreglo.length-1 

let gastosDeLaSemana = [1000, 3000, 6000, 1500]
console.log("Gastos de la semana 1", gastosDeLaSemana)
gastosDeLaSemana.push(7000)
gastosDeLaSemana.push(2500)

console.log("Gastos de la semana 2", gastosDeLaSemana)

gastosDeLaSemana.pop()

console.log("Gastos de la semana 3", gastosDeLaSemana)

// método Splice

gastosDeLaSemana.splice(1,2)

console.log("Gastos de la semana 4", gastosDeLaSemana)


// Recorrer un arreglo
let totalCompra=0

for (let i = 0; i < gastosDeLaSemana.length ; i++ ){
    console.log(gastosDeLaSemana[i])
    totalCompra+=gastosDeLaSemana[i]
}

console.log('Total de compra',totalCompra)