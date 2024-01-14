# Decorador: Agrega un código o funcionalidad extra (decoración) a una función existente. 
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada()

# Función sin decorador
""" def saludo():
    print("Hola Dalto!") """

# saludo() # Hola Dalto!

# se crea una nueva "variable" que actua como función decoradora y se ejecuta el decorador
# saludo_modificado = decorador(saludo) 

# usando @decorador: forma corta de aplicar la funcion decorador
@decorador
def saludo():
    print("Hola Dalto!")
