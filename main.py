import ahorcado_lib as juego

def mostrar_menu():
    print("\n==========================")
    print("   BIENVENIDO AL AHORCADO ")
    print("==========================")
    print("1. Iniciar Juego")
    print("2. Ver Reglas")
    print("3. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Tu nombre: ")
            edad = input("Tu edad: ")
            juego.iniciar_partida(nombre, edad)
        elif opcion == "2":
            print(juego.obtener_reglas())
        elif opcion == "3":
            print("Saliendo del juego... ¡Adiós!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_programa()
