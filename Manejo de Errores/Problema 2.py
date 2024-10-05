# Calificaciones de alumnos

def obtener_calificaciones():

    while True:

        try:
            
            ingreso_calificaciones= input("Ingrese una lista de " 
                                          "calificaciones separadas por comas: ")
            
            lista_calificaciones= ingreso_calificaciones.split(',')
            
            calificaciones= [int(calificaciones.strip()) for calificaciones 
                             in lista_calificaciones]
            
            return calificaciones
        
        except ValueError:
            print("""Error: Por favor, asegúrese de que todas las
                   calificaciones sean números enteros válidos.""")

print(obtener_calificaciones())