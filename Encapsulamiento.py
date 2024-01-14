# Encapsulamiento: Crear una interfaz pública para modificar los atributos de un objeto
# _atributo (1 _: protegido o privado en python,  indica que no deberia acceder como publico, pero de todos modos python lo permite)
# __atributo (2 __: privado o super privado en python, no se puede accerder desde fuera)
class MiClase:
    def __init__(self) -> None:
        self.__atributo_privado = "Valor"

objeto = MiClase()
# print(objeto.__atributo_privado) # AttributeError: 'MiClase' object has no attribute '__atributo_privado'

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # _ indica que es privado, no debería accederse directamente
        self._edad   = edad
    
    def get_nombre(self):
        return self._nombre

dalto = Persona("Lucas", 21)
# print(dalto._nombre) # Lucas - No deberia usar esta forma de obtener el atributo, ya que esta indicado como privado: _nombre;  pero python lo permite aun asi lo permite
nombre = dalto.get_nombre() # usando getter's debe ser lo correcto
print(nombre) # Lucas

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # __ indica que es super privado
        self.__edad   = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
dalto = Persona("Lucas", 21)
# print(dalto.__nombre) # Error, no permite acceder directamente al atributo super privado desde afuera de la clase
nombre = dalto.get_nombre() # usando getter's puedo acceder a atributos super privados
print(nombre) # Lucas

dalto.set_nombre("Pepito") # usando setter's puedo modificar atributos privados y super privados
nombre = dalto.get_nombre()
print(nombre)
