// let edad = 30
// if (edad < 18){
//     console.log('Menor de edad')
// } else{
//     //error
//     console.log(Bienvenido)

//     console.log('Registrate con nosotros')
// }


// Consulta y Respuesta

console.log('Inicio de página')
console.log(fetch("https://api.github.com/users/dev-marisa"))
console.log('Fin del proceso')

// async function buscando_devs(){
//     console.log('Buscando un dev...')
//     let res = await fetch("https://api.github.com/users/dev-marisa")
//     let devData = await res.json()
//     console.log('info del dev',devData)
//     console.log('Login:',devData.login)
//     console.log('Avatar:',devData.avatar_url)
// }

// buscando_devs()

// async function buscando_perritos_random() {
//     console.log('Buscando un dev...')
//     let resultado = await fetch("https://dog.ceo/api/breeds/list/all")
//     let perritoData = await resultado.json()
//     console.log('json Perrito: ',perritoData)
// }

// buscando_perritos_random()

async function buscando_perritos_por_raza() {
    console.log('Buscando un dev...')
    let resultado = await fetch("https://dog.ceo/api/breed/husky/images")
    let perritoData = await resultado.json()
    console.log('json Perrito por Raza: ', perritoData)
    console.log('1 perrito: ',perritoData['message'][3])
    return perritoData
}

let perrito = buscando_perritos_por_raza()['message']
let imgperrito1= document.getElementById('imagen-perrito1')
let imgperrito2= document.getElementById('imagen-perrito2')

document.addEventListener('DOMContentLoaded', async function(){
    let resultado = await fetch("https://dog.ceo/api/breed/husky/images")
    let perritoData = await resultado.json()
    
    imgperrito1.src=perritoData['message'][3]
    imgperrito2.src=perritoData['message'][4]

})


let cerrarModal= document.getElementById('cerrar-modal')
let perritoModal = document.getElementById('perrito-modal')
let bottonperrito1= document.getElementById('boton-perrito1')


cerrarModal.addEventListener('click', function(){
    perritoModal.style.display="none"
})

bottonperrito1.addEventListener('click', function(){
    perritoModal.style.display="block"
})

const botonCambio= document.querySelector("#boton-cambio")

console.log(botonCambio)
const elementosLista = document.querySelectorAll(".elemento-navegacion")

console.log(elementosLista)

botonCambio.addEventListener("click",function(){

    for(let i = 0; i<elementosLista.length; i++)
        elementosLista[i].style.backgroundColor="limegreen";

})
// elementosLista[0].style.backgroundColor="limegreen";