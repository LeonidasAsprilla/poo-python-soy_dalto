class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad   = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola! me llamo {self.nombre}, estoy hablando un poco.")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self):
        print(f"Hola! me llamo {self.nombre}, soy {self.trabajo} y estoy hablando un poco.")

leonidas = Empleado("Leonidas", 42, "colombiano", "Programador", 1000000)
# leonidas.hablar()

# Herencia simple
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

class Artista: 
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return(f"Mi habilidad es: {self.habilidad}")

# Herencia multiple
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario

    """ def mostrar_habilidad(self):
        print("No tengo... jajaja") """

    def presentarse(self):
        return(f"Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
        #return (f"{super().mostrar_habilidad()}") # accedo al metodo de la clase padre
        #return (f"{self.mostrar_habilidad()}") # accedo al metodo propio sobreescrito
    
roberto = EmpleadoArtista("Roberto", 43, "argentino", "Cantar", "Google", 1000000)
print(roberto.presentarse())

# Saber si hay herencia (subclases)
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia) # True
herencia = issubclass(Artista, Persona)
print(herencia) # False

# Instancia: Saber si un objeto es una instancia de una clase
instancia = isinstance(roberto, EmpleadoArtista)
print(instancia) # True - roberto es una subclase de EmpleadoArtista
instancia = isinstance(roberto, Artista)
print(instancia) # True - porque hereda de Artista
instancia = isinstance(roberto, Persona)
print(instancia) # True - porque hereda de Persona
instancia = isinstance(roberto, Empleado)
print(instancia) # False 

carlos = Artista("Pintor")

instancia = isinstance(carlos, Artista)
print(instancia) # True
instancia = isinstance(carlos, Persona)
print(instancia) # False
instancia = isinstance(carlos, Empleado)
print(instancia) # False
instancia = isinstance(carlos, EmpleadoArtista)
print(instancia) # False

