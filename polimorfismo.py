class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    
gato = Gato()
perro = Perro()

print(gato.sonido()) # Miau
print(perro.sonido()) # Guau

def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(perro)
hacer_sonido(gato)