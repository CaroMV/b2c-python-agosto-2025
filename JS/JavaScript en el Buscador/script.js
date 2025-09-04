// Traer la información del elemento que queremos modificar
//PASO 1:
let boton = document.getElementById('colorButton');

//Verificar paso 1
console.log(boton)

//PASO 2: 
// Establecer el evento
// opcion1
// function cambioColor(){
//     console.log('Cambió de color!')
// }
// boton.addEventListener("click", cambioColor)
//opcion2
boton.addEventListener("click", function(){
    console.log('Este mensaje es distinto')
    boton.style.background="black"
    boton.innerText = "Ya no se puede cambiar de color 😥"
})


let botonPerrito = document.getElementById('perritoButton');
// console.log(botonPerrito)

let imagen = document.getElementById('imagen');

botonPerrito.addEventListener("click", function(){
    imagen.src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQpflckqTzo_CVJxHUPahKCrnIL3d2DIJn1ThfaalZfK682pUAn3mFidzfZM_yuLhNwHlLHRd_UkAVb_KZQfj4pnA"
})

let otroboton= document.getElementById('otroboton')

otroboton.addEventListener('click', function(){
    otroboton.innerHTML = "<p class='superParrafo'> Hola :) </p>"
})