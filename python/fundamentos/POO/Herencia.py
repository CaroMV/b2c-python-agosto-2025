#Animales:
#clasificacion grande de varias especies, varios tipos
class Animal:
    def __init__(self):
        self.celula_animal=True
    def mover(self):
        return 'Se mueve'

class Mascota(Animal):
    def __init__(self, nombre):
        super().__init__()
        self.nombre=nombre

    def comer(self):
        return f'{self.nombre} está comiendo'
    
    def sonido(self):
        return f' {self.nombre} hace un sonido'
    
    def mover(self):
        b=super().mover()
        return 'otro mensaje'

class Perro(Mascota): #Perro es una clase que hereda de Mascota
    def sonido(self):
        return f'{self.nombre} Guau'
    def mover(self):
        a=super().mover()
        return a+ ' en 4 patas'

class Gato(Mascota): #Perro es una clase que hereda de Mascota
    def sonido(self):
        return f'{self.nombre} Miau'    

mascota=Mascota("Aceituna")
perro=Perro("Luna")

print(mascota.sonido())
print(perro.sonido())
print(perro.comer())
print(perro.mover())


#Mercado libre

#Una tienda tiene Productos
    #precio
    #nombre
    #marca

#Productos de limpieza
    
#Productos electronicos
    #televisores
        #pulgadas
    #camaras
        #megapixeles
    #telefono movil
        #capacidad de almacenamiento
#Productos de comida
    #vencimiento

#ANTI EJEMPLO
# class ProductoComida:
#     def __init__(self, nombre, precio, marca, vencimiento):
#         self.nombre=nombre
#         self.precio=precio
#         self.marca=marca
#         self.vencimiento=vencimiento

# class Televisores:
#     def __init__(self, nombre, precio, marca, pulgadas):
#         self.nombre=nombre
#         self.precio=precio
#         self.marca=marca
#         self.pulgadas=pulgadas

class Producto:
    def __init__(self, precio, nombre, marca):
        self.nombre=nombre
        self.precio=precio
        self.marca=marca
        self.atributoGeneral="Productos de Mercado Libre"



class Televisor(Producto):
    def __init__(self, precio, nombre, marca, pulgadas):
        super().__init__(precio, nombre, marca)
        self.pulgadas=pulgadas

class ProductoDeComida(Producto):
    def __init__(self, precio, nombre, marca, vencimiento):
        super().__init__(precio, nombre, marca)
        self.vencimiento=vencimiento

televisorSamsung=Televisor(130000, "televisor SmartTV S1239", "Samsung", "50'")
print(televisorSamsung.atributoGeneral)

fideos= ProductoDeComida(800, "Fideos largos", "Talliani", "12-2026")
print(fideos.atributoGeneral)
print(fideos.nombre)
print(fideos.vencimiento)


class Persona:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def saludar(self):
        return "Hola"
    
class Amigo(Persona):
    def saludar(self):
        mensaje=super().saludar()
        return mensaje + ' Amigo'
    

personaComun = Persona("Benjamín")
amigo= Amigo("Pedro")

print(personaComun.saludar())
print(amigo.saludar())






class A:
    def saludar(self):
        print("saludo1")

class B(A):
    def saludar(self):
        print("saludo2")

class C(B):
    def saludar(self):
        print("saludo3")
        
        super(B,self).saludar() #Saludo de B

class D(C):
    def saludar(self):
        print("saludo4")
        
        super(C,self).saludar() #Saludo de B


objetoprueba=D()       

print(objetoprueba.saludar())