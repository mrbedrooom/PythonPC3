
# CÍRCULO
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio**2)

# Objetos de tipo círculo
circulo1= CIRCULO(7.5)
circulo2= CIRCULO(100)

# Área de cada círculo
area_circulo1= circulo1.calcular_area()
area_circulo2= circulo2.calcular_area()

print(f"El área del círculo 1 es: {area_circulo1}")
print(f"El área del círculo 2 es: {area_circulo2}")