class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando.")

nombre = input("Digame su nombre: ")
edad = input("Ahora su edad: ")
grado = input("Por último, su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n\
    Nombre: {estudiante.nombre}
    Edad: {estudiante.edad}
    Grado: {estudiante.grado}
""")

estudiante.estudiar()