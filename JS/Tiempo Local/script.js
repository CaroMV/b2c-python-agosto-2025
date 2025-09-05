
alert('Cargando Reporte del Clima')

function cambiaCiudad(ciudad){

    let climas = {
    buenosaires:{
        nombre:'Buenos Aires',
        dias:[
            {dia: 'Hoy',clima:'Soleado', max: 29, min:18, imagen:'soleado.png'},
            {dia: 'Manana',clima:'Soleado', max: 30, min:15 , imagen:'soleado.png'},
            {dia: 'Miercoles', clima:'Soleado', max: 25, min:10 , imagen:'soleado.png'},
            {dia: 'Jueves',clima:'Nublado',  max: 20, min:10, imagen:'nublado.jpg'},
            {dia: 'Viernes',clima:'Soleado',  max: 23, min:17, imagen:'soleado.png'},
        ]
    },
    ciudaddemexico:{
        nombre:'Ciudad de Mexico',
        dias:[
            {dia: 'Hoy',clima:'Nublado', max: 17, min:12, imagen:'nublado.jpg'},
            {dia: 'Manana',clima:'Lluvioso', max: 15, min:7, imagen:'lluvioso.png'},
            {dia: 'Miercoles', clima:'Lluvioso', max: 17, min:9, imagen:'lluvioso.png'},
            {dia: 'Jueves',clima:'Nublado',  max: 18, min:12, imagen:'nublado.jpg'},
            {dia: 'Viernes',clima:'Tormenta',  max: 16, min:8, imagen:'tormenta.png'},
        ]
    },
    santiago:{
        nombre:'Santiago',
        dias:[
            {dia: 'Hoy',clima:'Soleado', max: 31, min:19,imagen:'soleado.png'},
            {dia: 'Manana',clima:'Soleado', max: 32, min:18,imagen:'soleado.png'},
            {dia: 'Miercoles', clima:'Soleado', max: 28, min:18,imagen:'soleado.png'},
            {dia: 'Jueves',clima:'Nublado',  max: 23, min:16,imagen:'nublado.jpg'},
            {dia: 'Viernes',clima:'Nublado',  max: 24, min:17,imagen:'nublado.jpg'},
        ]
    },
    saopaulo:{
        nombre:'Sao Paulo',
        dias:[
            {dia: 'Hoy',clima:'Soleado', max: 31, min:19,imagen:'soleado.png'},
            {dia: 'Manana',clima:'Soleado', max: 32, min:18,imagen:'soleado.png'},
            {dia: 'Miercoles', clima:'Soleado', max: 28, min:18,imagen:'soleado.png'},
            {dia: 'Jueves',clima:'Nublado',  max: 23, min:16,imagen:'nublado.jpg'},
            {dia: 'Viernes',clima:'Nublado',  max: 24, min:17,imagen:'nublado.jpg'},
        ]
    },
    quito:{
        nombre:'Quito',
        dias:[
            {dia: 'Hoy',clima:'Soleado', max: 31, min:19,imagen:'soleado.png'},
            {dia: 'Manana',clima:'Soleado', max: 32, min:18,imagen:'soleado.png'},
            {dia: 'Miercoles', clima:'Soleado', max: 28, min:18,imagen:'soleado.png'},
            {dia: 'Jueves',clima:'Nublado',  max: 23, min:16,imagen:'nublado.jpg'},
            {dia: 'Viernes',clima:'Nublado',  max: 24, min:17,imagen:'nublado.jpg'},
        ]
    },
}
    console.log(climas[ciudad])


    let infoclima= climas[ciudad]

    document.getElementById('nombre-ciudad').innerText = infoclima.nombre

    // //Hoy

    // document.getElementById('clima-hoy').innerText = infoclima.dias[0].clima
    // document.getElementById('temp-max-hoy').innerText = infoclima.dias[0].max
    // document.getElementById('temp-min-hoy').innerText = infoclima.dias[0].min
    // document.getElementById('imagen-clima-hoy').src='./imagenes/'+infoclima.dias[0].imagen

    // //Mañana
    // document.getElementById('clima-manana').innerText = infoclima.dias[1].clima
    // document.getElementById('temp-max-manana').innerText = infoclima.dias[1].max
    // document.getElementById('temp-min-manana').innerText = infoclima.dias[1].min
    // document.getElementById('imagen-clima-manana').src='./imagenes/'+infoclima.dias[1].imagen

    // //Miercoles
    // document.getElementById('clima-miercoles').innerText = infoclima.dias[2].clima
    // document.getElementById('temp-max-miercoles').innerText = infoclima.dias[2].max
    // document.getElementById('temp-min-miercoles').innerText = infoclima.dias[2].min
    // document.getElementById('imagen-clima-miercoles').src='./imagenes/'+infoclima.dias[2].imagen
    // //Jueves
    // document.getElementById('clima-jueves').innerText = infoclima.dias[3].clima
    // document.getElementById('temp-max-jueves').innerText = infoclima.dias[3].max
    // document.getElementById('temp-min-jueves').innerText = infoclima.dias[3].min
    // document.getElementById('imagen-clima-jueves').src='./imagenes/'+infoclima.dias[3].imagen

    // //Viernes
    // document.getElementById('clima-viernes').innerText = infoclima.dias[4].clima
    // document.getElementById('temp-max-viernes').innerText = infoclima.dias[4].max
    // document.getElementById('temp-min-viernes').innerText = infoclima.dias[4].min
    // document.getElementById('imagen-clima-viernes').src='./imagenes/'+infoclima.dias[4].imagen


    console.log(infoclima.dias.length)

    for (let i = 0; i< infoclima.dias.length; i++ ){
        console.log(infoclima.dias[i].dia.toLowerCase())

        document.getElementById(`clima-${infoclima.dias[i].dia.toLowerCase()}`).innerText = infoclima.dias[i].clima;
        document.getElementById(`temp-max-${infoclima.dias[i].dia.toLowerCase()}`).innerText = infoclima.dias[i].max;
        document.getElementById(`temp-min-${infoclima.dias[i].dia.toLowerCase()}`).innerText = infoclima.dias[i].min;
        document.getElementById(`imagen-clima-${infoclima.dias[i].dia.toLowerCase()}`).src = './imagenes/'+infoclima.dias[i].imagen;
    }

}


let boton_cookies = document.getElementById('boton-cookies')
let contenedor_cookies = document.getElementById('contenedor-cookies')

boton_cookies.addEventListener('click', function(){
    contenedor_cookies.remove()
})


