# Getter's, Setter's y Deletter's
# @property - hace pasar el método o función como una propiedad, ya no necesita ()
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad   = edad
    
    """
    @property 
    def get_nombre(self):
        return self.__nombre 
    """
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
dalto = Persona("Lucas", 21)
# ahora get_nombre luce como propiedad del objeto, no un metodo, pero sigue siendo un método.
# nombre = dalto.get_nombre # Lucas
nombre = dalto.nombre # cambio de get_nombre a simplemente nombre
print(nombre) # Lucas

dalto.nombre = "Pepe" # usando el setter nombre con el decorador @nombre.setter
nombre = dalto.nombre # usando el getter nombre con el decorador @property
print(nombre)

# del dalto.nombre # elimina la propiedad nombre gracias al deleter
# nombre = dalto.nombre #  AttributeError: 'Persona' object has no attribute '_Persona__nombre'
# print(nombre)