# TIENDA DE AUTOPARTES

# PRODUCTO
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre= nombre
        self.precio= precio
        self.año= año

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Año: {self.año}"

# CATÁLOGO
class Catálogo:
    def __init__(self):
        self.productos= []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

    def producto_más_caro(self):
        if not self.productos:
            return None
        return max(self.productos, key=lambda p: p.precio)


catalogo= Catálogo()

producto1= Producto("Filtro de aceite", 15.99, 2022)
producto2= Producto("Batería", 99.99, 2023)
producto3= Producto("Neumático", 129.00, 2023)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Todos los productos:")
catalogo.mostrar_productos()

print("\nProductos del año 2022:")
for p in catalogo.filtrar_por_año(2022):
    print(p)

print("\nProducto más caro:")
print(catalogo.producto_más_caro())