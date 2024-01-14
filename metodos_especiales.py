# Métodos especiales __metodo__
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Metodo especial __str__ que redifine cuando se imprime la clase devolviendo un str
    def __str__(self):
        return(f"Persona(nombre={self.nombre}, edad={self.edad})")
    

    def __repr__(self) -> str:
        return f'Persona(nombre="{self.nombre}", edad={self.edad})'
    
    # Sobrecarga del operador de suma (+)
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
    
dalto = Persona("Lucas",21)
# sin redefinir __str__
# print(dalto) # <__main__.Persona object at 0x000001D7D6AEBE50>
# redefiniendo el método especial __str__
print(dalto) # Persona(nombre=Lucas, edad=21)

# __repr__ representacion del objeto
representacion = repr(dalto)

# sin modificar el método especial __repr__
# print(representacion) # <__main__.Persona object at 0x0000017CA62F0090>

# modificando __repr__
print(representacion) # Persona(nombre="Lucas", edad=21)

resultado = eval(representacion) # evaluacion de la representación del objeto
print(resultado) # Persona(nombre=Lucas, edad=21)
print(resultado.edad) # 21 - resultado es una representacion del objeto
print(resultado.nombre) # Lucas

# Sobrecarga de operadores
""" 
Aritméticos
__add__(self, other) : Sobrecarga el operador de la suma (+)
__sub__(self, other) : Sobrecarga el operador de la resta (-)
__mul__(self, other) : Sobrecarga el operador de la multiplicación (*)
__div__(self, other) : Sobrecarga el operador de la división (/)
__mod__(self, other) : Sobrecarga el operador de la módulo (%)
__pow__(self, other) : Sobrecarga el operador de la exponenciación (**)
Comparación
__eq__(self, other) : Sobrecarga el operador de la igualdad (==)
__ne__(self, other) : Sobrecarga el operador de la desigualdad (!=)
__lt__(self, other) : Sobrecarga el operador de menor que (<)
__gt__(self, other) : Sobrecarga el operador de mayor que (>)
__le__(self, other) : Sobrecarga el operador de menor o igual que (<=)
__ge__(self, other) : Sobrecarga el operador de mayor o igual que (>=)
Asignación
__iadd__(self, other) : Sobrecarga el operador de la suma en asignación (+=)
__isub__(self, other) : Sobrecarga el operador de la resta en asignación (-=)
__imul__(self, other) : Sobrecarga el operador de la multiplicación en asignación (*=)
__idiv__(self, other) : Sobrecarga el operador de la división en asignación (/=)
__imod__(self, other) : Sobrecarga el operador de la módulo en asignación (%=)
__ipow__(self, other) : Sobrecarga el operador de la exponenciación en asignación (**=)
Otros
__str__(self): Sobrecarga del operador str(). Devuelve una representación legible como cadena del objeto
__len__(self): Sobrecarga del operador len(). Devuelve la longitud del objeto.
__getitem__(self,index): Sobrecarga del operador de indexación ([]). Permite acceder a elementos del objeto por índice.
 """

# Usando metodo sobrecargado de suma (+) en la clase Persona(), que crea un nuevo objeto Persona con los nombres concatenados y las edades sumandas
dalto = Persona("Lucas", 21)
pedro = Persona("Pedro", 30)
nueva_persona = dalto + pedro
print(dalto) # Persona(nombre=Lucas, edad=21)
print(pedro) # Persona(nombre=Pedro, edad=30)
print(nueva_persona) # Persona(nombre=LucasPedro, edad=51)

maria = Persona("Maria", 18)
otra_nueva_persona = dalto + pedro + maria
print(otra_nueva_persona) # Persona(nombre=LucasPedroMaria, edad=69)

