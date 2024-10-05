# MENÚ CALCULADORA

from áreas import CIRCULO, RECTANGULO, CUADRADO

def mostrar_menu():
    print("\nMenú de Calculadora:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Error: El número debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Entrada no válida. Introduce un número.")

def calcular_area_circulo():
    radio = validar_numero_positivo("Introduce el radio del círculo: ")
    circulo = CIRCULO(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo es: {area:.2f}")

def calcular_area_rectangulo():
    largo = validar_numero_positivo("Introduce el largo del rectángulo: ")
    ancho = validar_numero_positivo("Introduce el ancho del rectángulo: ")
    rectangulo = RECTANGULO(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area:.2f}")

def calcular_area_cuadrado():
    lado = validar_numero_positivo("Introduce el lado del cuadrado: ")
    cuadrado = CUADRADO(lado)
    area = cuadrado.calcular_area()
    print(f"El área del cuadrado es: {area:.2f}")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()