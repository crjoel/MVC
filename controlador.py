import modelo
import vista


def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    try:
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("Precio inválido. Debe ser un número.")
        return

    nuevo = modelo.Producto(nombre, categoria, precio)
    modelo.guardar_producto(nuevo)
    print("Producto agregado correctamente.")


def listar_productos():
    lista = modelo.obtener_productos()
    vista.mostrar_productos(lista)
