# MENÚ BIBLIOTECA

from gestion import GestionBiblioteca
from libro import Libro

def mostrar_menu():
    print("\nMenú de Biblioteca:")
    print("1. Agregar un libro")
    print("2. Listar los libros")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por autor")
    print("5. Salir")

def main():
    gestion= GestionBiblioteca()

    while True:
        mostrar_menu()
        opcion= input("\nSelecciona una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print(f"\nLibro '{titulo}' agregado con éxito.")
        elif opcion == '2':
            print("\nListado de libros:")
            gestion.listar_libros()
        elif opcion == '3':
            titulo = input("Título del libro a buscar: ")
            libros = gestion.buscar_por_titulo(titulo)
            if libros:
                print(f"\nLibros encontrados con el título '{titulo}':")
                for libro in libros:
                    print(libro)
            else:
                print(f"\nNo se encontraron libros con el título '{titulo}'.")
        elif opcion == '4':
            autor = input("Autor del libro a buscar: ")
            libros = gestion.buscar_por_autor(autor)
            if libros:
                print(f"\nLibros encontrados del autor '{autor}':")
                for libro in libros:
                    print(libro)
            else:
                print(f"\nNo se encontraron libros del autor '{autor}'.")
        elif opcion == '5':
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()