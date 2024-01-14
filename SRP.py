""" 
S - SRP
Una clase debe tener una sola responsabilidad 
"""

# La clase Auto tiene muchas responsabilidades (mover, agregar combustible, etc)
""" class Auto():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100

    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print("No hay suficiente combustible.")

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible """

# Se recomienda dividir la clase Auto, para que solo mueva el auto
class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente.")
        else:
            print("No hay suficiente combustible.")

    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def obtener_combustible(self):
        return self.combustible
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
    
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(20)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())