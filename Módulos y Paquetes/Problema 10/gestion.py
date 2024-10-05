# GESTIÓN

from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros= []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if 
                libro.titulo.lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if 
                libro.autor.lower() == autor.lower()]
