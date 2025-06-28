class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - S/ {self.precio:.2f}"


productos = []  # Lista para almacenar productos


def guardar_producto(producto):
    productos.append(producto)


def obtener_productos():
    return productos
