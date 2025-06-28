import controlador
import vista

def main():
    while True:
        vista.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            controlador.agregar_producto()
        elif opcion == '2':
            controlador.listar_productos()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
