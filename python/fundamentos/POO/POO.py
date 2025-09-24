

#Esto es una clase
class Jugador():
    # Crear el objeto, para eso utilizamos un método, un constructor
    #Los atributos son los datos
    def __init__(self, nombre, edad, posicion):
        self.nombre=nombre 
        self.edad=edad
        self.posicion=posicion
    
    #El resto de los métodos son las acciones que puede hacer el objeto
    def jugar(self):    
        print(f'El jugador {self.nombre} está jugando en la posición {self.posicion}')
        return self

jugador1 = Jugador("Estefania", 25, "Delantera")
jugador2 = Jugador("Esteban", 21, "Delantero")
jugador1.jugar()
jugador2.jugar()



#Estructura procedimental
#Datos de mi almacen
productos = ["pan", "leche", "huevos", "carne"]
precios=[1000, 2500, 3000, 15000]

#Funcion para mostrar los productos
def mostrarProductos(indice):
    print(productos[indice],"-",precios[indice])

mostrarProductos(0)
mostrarProductos(3)

class Producto():
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio

    def mostrar(self):
        print(f'Producto: {self.nombre} - Precio: {self.precio}')
        
    def cambiarPrecio(self, nuevoPrecio):
        self.precio=nuevoPrecio
        print(f'El nuevo precio de {self.nombre} es {self.precio}')

producto1=Producto("pan", 1000)
producto2=Producto("leche", 2500)
producto3=Producto("huevos", 3000)
producto4=Producto("carne", 15000)

producto1.mostrar()
producto1.cambiarPrecio(1200)
producto2.mostrar()
producto2.cambiarPrecio(2700)
producto3.mostrar()
producto4.mostrar() 