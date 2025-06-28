def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Salir")


def mostrar_productos(lista):
    if not lista:
        print("No hay productos registrados.")
    else:
        print("\n--- Lista de Productos ---")
        for idx, producto in enumerate(lista, start=1):
            print(f"{idx}. {producto}")
