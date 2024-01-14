# Clases abstractas - clase plantilla que no se puede instanciar
""" 
modulo abc - Abstract Base Classes (ABCs) - permite crear clases abstractas
clase ABC - Clase auxiliar que permite crear clases abstractas por herencia
(class) abstractclassmethod - A decorator indicating abstract classmethods.

 """
from abc import ABC, abstractclassmethod

class Persona(ABC): 
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

# No se puede instanciar de una clase abstracta, ni con metodos abstractos
# dalto = Persona("Lucas", 21, "Masculino", "Programador") # TypeError: Can't instantiate abstract class Persona with abstract methods __init__, trabajar

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

dalto = Estudiante("Lucas", 21, "Masculino", "Programación")
dalto.presentarse()
dalto.hacer_actividad()

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")

pedrito = Trabajador("Pedrito", 25, "No binario", "Programación")
pedrito.presentarse()
pedrito.hacer_actividad()


