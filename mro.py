# Método de Resolución de Orden
class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")

d = D()

d.hablar() # Hola desde D
""" Si no encuentra el método hablar() en D, usa B (primer padre)
Si no encuentra en B, usa C (segundo padre)
Si no encuentra en C, usa A (clase padre de todas) 
d.hablar() # Hola desde B
d.hablar() # Hola desde C
d.hablar() # Hola desde A
"""
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Llamar a los metodos de clases padres desde subclases
C.hablar(d) # Hola desde C