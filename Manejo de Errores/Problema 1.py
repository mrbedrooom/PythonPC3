# Cuánto combustible tengo

def porcentaje_combustible():

    while True:

        try:
            fraction = input("Ingrese su fracción (X/Y): ")
            
            # Dividiendo la fracción en X e Y
            x, y = fraction.split('/')
            
            x = int(x)
            y = int(y)
            
            # Verificando si Y es igual a 0
            if y == 0:
                raise ZeroDivisionError
            
            # Verificando si X es mayor que Y
            if x > y:
                raise ValueError
            
            # Calculando el porcentaje
            porcentaje= (x / y) * 100
            
            # Aplicando las reglas
            if porcentaje < 1:
                return 'E'  # Menos del 1%
            elif porcentaje > 99:
                return 'F'  # Más del 99%
            else:
                return f"{round(porcentaje)}%"
            
        except ValueError:
            print("""Error: Ingrese números enteros válidos y asegúrese de
                   que X <= Y.""")
        except ZeroDivisionError:
            print("Error: Y no puede ser igual a 0.")

print(porcentaje_combustible())