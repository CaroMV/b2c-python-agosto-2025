let informacionUsuario = {
    clave:'valor',
    nombre:'Carolina',
    apellido:'Moreno',
    edad:30,
    hobbies:['Videojuegos', 'Musica', 'Programación'], 
    preferencias:{
        color_favorito: 'negro',
        musica_favorita: 'Rock', 
    }
}

console.log(informacionUsuario["preferencias"])


var hamburguesaClasica = {
    "pan": "pan con semillas de sésamo",
    "carne": "carne de res 100%",
    "queso": "queso cheddar",
    "extras": ["lechuga", "tomate", "cebolla", "salsa especial"],
    "infoHamburguesa": function() {
        console.log("Pan: " + this.pan);
        console.log("Carne: " + this.carne);
        console.log("Queso: " + this.queso);
        console.log("Extras: " + this.extras.join(", "));
    }
}
console.log(hamburguesaClasica.pan)
