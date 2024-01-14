# LSP - LISKOV'S SUBSTITUTION PRINCIPLE
# si la clase B es hija de la clase A, la clase A se deberia poder utilizar en cualquier parte que se use B

""" class Ave:
# Establecemos en la clase padre que todas las aves pueden volar
    def volar(self):
        return "Estoy volando"

# pero no es consistente en pinguino que no puede volar
class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"
    
def hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar(Pinguino())) # No puedo volar """

# Definimos todas las propiedades y metodos en comun de la clase padre
class Ave:
    pass

# Establecemos clases hijas, con sus diferencias de la clase padre
class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass