# PUNTO

class Punto:

    def __init__(self, x=0, y=0):
        self.x= x
        self.y= y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return ((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)**0.5

# Experimentación

puntoA= Punto(2, 3)
puntoB= Punto(5, 5)
puntoC= Punto(-3, -1)
puntoD= Punto(0, 0)

print(f"Punto A: {puntoA}")
print(f"Punto B: {puntoB}")
print(f"Punto C: {puntoC}")
print(f"Punto D: {puntoD}")

print(f"Cuadrante de A: {puntoA.cuadrante()}")
print(f"Cuadrante de C: {puntoC.cuadrante()}")
print(f"Cuadrante de D: {puntoD.cuadrante()}")

print(f"Vector AB: {puntoA.vector(puntoB)}")
print(f"Vector BA: {puntoB.vector(puntoA)}")

print(f"Distancia A-B: {puntoA.distancia(puntoB)}")
print(f"Distancia B-A: {puntoB.distancia(puntoA)}")

# Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen
distancias= {
    "A": puntoA.distancia(puntoD),
    "B": puntoB.distancia(puntoD),
    "C": puntoC.distancia(puntoD)
}

más_lejos= max(distancias, key=distancias.get)
print(f"El punto más lejos del origen es: {más_lejos}")