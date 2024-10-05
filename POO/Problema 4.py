
#RECTÁNGULO
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo= largo
        self.ancho= ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

#CUADRADO (heredadado de RECTÁNGULO)
class CUADRADO(RECTANGULO):
    def __init__(self, lado):

        super().__init__(lado, lado)

#OBJETOS DE TIPO
rectangulo1= RECTANGULO(10, 5)
cuadrado1= CUADRADO(4)

area_rectangulo= rectangulo1.calcular_area()
area_cuadrado= cuadrado1.calcular_area()

print(f"El área del rectángulo es: {area_rectangulo}")
print(f"El área del cuadrado es: {area_cuadrado}")