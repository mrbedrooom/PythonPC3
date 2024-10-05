# CÁLCULOS

import operaciones

def main():
    print(operaciones.sumar(10, 5))
    print(operaciones.restar(10, 5))
    print(operaciones.multiplicar(10, 5))
    print(operaciones.dividir(10, 5))

    # Pruebas de manejo de errores
    print(operaciones.sumar("10", 5))  # Error de tipo
    print(operaciones.dividir(10, 0))  # Error de división por cero

if __name__ == "__main__":
    main()