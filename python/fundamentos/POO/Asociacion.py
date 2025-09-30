class Profesor:
    def __init__(self, nombre):
        self.nombre=nombre

class Curso:
    def __init__(self, nombre, profesor):
       self.nombre = nombre
       self.profesor=profesor


profe_caro=Profesor("Carolina")

curso=Curso("Full Stack Python", profe_caro)

print(f'Curso: {curso.nombre}, profesor: {curso.profesor.nombre}')