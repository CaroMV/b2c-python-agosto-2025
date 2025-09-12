
#Comentarios <- #

#let variable = valor
#const variable = valor
#var variable = valor

nombre_variable = 'valor'

nombre = "Carolina"     #String
edad = 30               #int Entero
altura= 1.59            #float Decimal
es_estudiante= False    #booleano

print("Tipos")
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))

#En javascript podía agregar variables en los textos cuando usaba
#Interpolacion
print(f'Bienvenido/a {nombre}')

print("Puedo concatenar"+" varias strings" +" igual que en javascript")

listas=["Facundo", "Jesus", "Angel"]
print(listas[1])

listas.append("Sergio")

print(listas)

lista_grande = [2, 4, 6, 18, 10, 12, 32, 16]

print(lista_grande[2:5])

print(len(lista_grande))
print(max(lista_grande))
print(min(lista_grande))
print(sorted(lista_grande))

print(lista_grande)
lista_grande.pop(3)
print(lista_grande)
print(lista_grande.index(32))


#Tuplas

tupla_letras = ("a", "e", "i", "o", "u")
tupla_letras = tupla_letras +("y",)

print(tupla_letras)


#Diccionarios

persona = {
    "nombre":"Carolina",
    "edad":30,
    "ciudad":"Santiago"
}
print('Diccionario nombre :'+persona["nombre"])
print(f'Diccionario edad: {persona["edad"]}')

persona["altura"]=1.59
print(f'Diccionario con nueva información: {persona}')
persona["nombre"]="Angelica"
print(f'Diccionario con otro nombre: {persona}')

print(persona.get('direccion'))


#Condicionales 

    #En JS las condicionales se hacían así:
    # if (condición){ }
nota=3.9

if nota>=4 :
    print('Has Aprobado')
else:
    print('No has aprobado el examen')


    #En JS cuando probabamos varias condiciones lo hacíamos con el else if


rol = "usuario"

if rol == "admin":
    print("Tienes el acceso total al sistema")
elif rol == "editor":
    print("Puedes editar el contenido")
else:
    print('No tienes acceso al sistema ')

condicion1 =False
condicion2 = False
print(condicion1 and condicion2)

#Bucles / Ciclos
    #En JS for(let i = 0, condicion que rompia bucle , incremento){}
print("----------------------------------")
for i in range(3):
    print(i)
    #Con un argumento, empieza desde 0 y el rango me dice cuántos ciclos se harán
print("----------------------------------")
for i in range(5,10):
    print(i)
    #Cuando uso 2 argumentos, empieza desde el primer argumento y llega hasta el segundo numero (no lo incluye)

print("----------------------------------")
for i in range(2,10,3):
    print(i)

print("----------------------------------")
for i in range(20,1,-4):
    print(i)

print("----------------------------------")
print("Recorrer Strings ")

letras=[]
for i in 'Carolina':
    letras.append(i)
print(letras)

print("----------------------------------")
print("Recorrer Lista ")

lista_compras=["Jamon", "Mantequilla", "Brocoli", "Pan"]

for i in range(len(lista_compras)):
    print(i, lista_compras[i])

for elemento in lista_compras:
    print(elemento)

#Recorrer un Diccionario
print("----------------------------------")
print("Recorrer Diccionario ")    
ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"],

   "Colombia":["Bogotá", "Cartagena", "Medellin"],

    "España": ["Madrid", "Andalucía", "Barcelona"]

}
#Es iterar para obtener las claves
for clave in ciudades:
    print(clave)
print("----------------------------------")
#Es iterar para obtener las claves
for clave in ciudades:
    print(ciudades[clave])

print("----------------------------------")

print("keys ",ciudades.keys())
print("values ",ciudades.values())

print("----------------------------------")
print("Iterar en la lista de claves")

for clave in ciudades.keys():
    print(clave)

for valores in ciudades.values():
    print(valores)

print("ITEMS: ",ciudades.items())

for clave, valor in ciudades.items():
    print(clave, "-", valor)


#Bucle While

num=0

while num<10:
    num+=1
    print(num,'Código')
else:
    print('Ya no se cumple la condición, termina el bucle while')


#Funciones:
    #En JS function nombreFunción(parametros, parametros...){bloque que se ejecuta}
print("----------------------------------")

def funcion():
    print("Hola")

funcion()

def saludar(nombre):
    print(f'Bienvenido {nombre}')
    return(f'Ahora si, te entrego un valor: Bienvenido, {nombre}')

saludo1=saludar("Estefania")
saludo2=saludar("Jesus")
print(saludo1)
print(saludo2)
print("----------------------------------")



def imprimirListas(lista):
    if len(lista) == 0:
        print(f'La lista no contiene nada')
    else:
        for elemento in lista:
            print(elemento)

listavacia=[]
imprimirListas(lista_compras)
imprimirListas(lista_grande)
imprimirListas(listas)
imprimirListas(listavacia)
