""" HERENCIAS - EJERCICIO 2
Ejercicio de herencia y uso de super:
Crear un sistema para una escuela. En este sistema, vamos a tneer dos clases principales: Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y sun método que imprime el nombre y la edad de la persna. La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un métdo que imprimia el graod del estudiante. 
Deberas utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente. """

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ver_datos(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años de edad.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def ver_grado(self):
        print(F"Hago el grado {self.grado}")

est = Estudiante("Leonidas", 13, 9)
est.ver_datos()
est.ver_grado()

""" Ejercicio de herencia múltiple y MRO
 Imagania que estás modelando animales en un zoológico. Crear estas tres clases: "Animal", "Mamífero y "Ave". La clase "Animal" debe tener un método llamado "comer". La clase "Mamífero" debe tener un método llamado "amamantar" y la clase "Ave" un método llamado "volar".
 Ahora crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", ademas de "comer". 
 Finalmente, juega con el orden de herencia de la clase "Murcielago y observa cómo cambia el MRO y el comportamiento de los métodos al usar super()"""

class Animal:
    def __init__(self):
        pass

    def comer(self):
        print(f"Soy un Animal y voy a comer")

class Mamifero(Animal):
    def __init__(self):
        super().__init__()

    def comer(self):
        # print(f"Soy un Mamífero y voy a comer")
        return super().comer()

    def amamantar(self):
        print(f"Soy un Mamífero y puedo amamantar")

class Ave(Animal):
    def __init__(self):
        super().__init__()
    
    def comer(self):
        # print(f"Soy un Ave y voy a comer")
        return super().comer()

    def volar(self):
        print(f"Soy un Ave y puedo volar")

class Murcielago(Mamifero, Ave):
    def __init__(self):
        super().__init__()

    def comer(self):
        # print("Soy un Murcielago y voy a comer")
        return super().comer()

    def amamantar(self):
        # print("Soy un Murcielago y puedo amamantar")
        return super().amamantar()

    def volar(self):
        # print("Soy un Murcielago y puedo volar")
        return super().volar()


m = Murcielago()
m.comer()
m.amamantar()
m.volar()
print(Murcielago.mro())
