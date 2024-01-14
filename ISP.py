""" 
ISP - INTERFACE SEGREGATION PRINCIPLE
No forzar al cliente a usar interfaces que no va a usar
 """
from abc import ABC, abstractmethod

""" class Trabajador(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador):
    def comer(self):
        return "El humano está comiendo."
    
    def trabajar(self):
        return "El humano está trabajando."
    
    def dormir(self):
        return "El humano está durmiendo."
    
class Robot(Trabajador):    
    def trabajar(self):
        return "El robot está trabajando."
    
    # esto viola el principio ISP
    def comer(self):
        pass

    def dormir(self):
        pass """

# la clase abstracta me obliga a crear un robot que necesta comer y dormir
# robot = Robot() # TypeError: Can't instantiate abstract class Robot with abstract methods comer, dormir

""" Para solucionar este problema con las interfaces (en este ejemplo con python, las interfaces son las clases abstractas), la solución vendria en crear varias interfaces mas pequeñas  """

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano está comiendo.")
    
    def trabajar(self):
        print("El humano está trabajando.")
    
    def dormir(self):
        print("El humano está durmiendo.")
    
# Ahora la clase Robot solo utiliza las "interfaces" que necesita y nada mas.
class Robot(Trabajador):    
    def trabajar(self):
        print("El robot está trabajando.")

robot = Robot()
humano = Humano()
humano.trabajar()
robot.trabajar()
humano.comer()
humano.dormir()
# robot.comer() # AttributeError: 'Robot' object has no attribute 'comer'
    