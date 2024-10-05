
#ALUMNO

class Alumno:

    def __init__(self, nombre, num_registro):
        self.nombre= nombre
        self.num_registro= num_registro
        self.edad= None
        self.nota= None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.num_registro}")
        if self.edad:
            print(f"Edad: {self.edad}")
        if self.nota:
            print(f"Nota: {self.nota}")

    def setAge(self, edad):
        self.edad= edad

    def setNota(self, nota):
        self.nota= nota


alumno = Alumno("Ana Paula", "22190042")

alumno.setAge(21)
alumno.setNota(17)

alumno.display()