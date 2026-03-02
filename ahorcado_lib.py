import random

def obtener_reglas():
    return """
    --- REGLAS DEL JUEGO ---
    1. Debes adivinar la palabra secreta letra por letra.
    2. Cada error te quitará una vida.
    3. Según el nivel, tendrás menos intentos.
    4. Si completas la palabra antes de morir, ¡ganas!
    ------------------------
    """

def configurar_dificultad(nivel):
    # Diccionario con: (Lista de palabras, Vidas)
    ajustes = {
        "1": (["casa", "perro", "sol", "luna"], 8),     # Fácil
        "2": (["computadora", "teclado", "python"], 6), # Medio
        "3": (["desoxirribonucleico", "algoritmo"], 4)  # Difícil
    }
    return ajustes.get(nivel, ajustes["2"]) # Por defecto nivel medio

def elegir_palabra(lista):
    return random.choice(lista).lower()

def mostrar_tablero(palabra, letras_adivinadas):
    representacion = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            representacion += letra + " "
        else:
            representacion += "_ "
    return representacion

def iniciar_partida(nombre, edad):
    print(f"\n--- Jugador: {nombre} ({edad} años) ---")
    print("Selecciona dificultad: 1.Fácil | 2.Medio | 3.Difícil")
    nivel = input("Opción: ")
    
    palabras, vidas = configurar_dificultad(nivel)
    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    letras_erradas = []

    while vidas > 0:
        print(f"\nVidas: {vidas}")
        print(f"Letras usadas: {', '.join(letras_erradas)}")
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))

        # Victoria
        if "_" not in mostrar_tablero(palabra_secreta, letras_adivinadas):
            print(f"¡Felicidades {nombre}! Ganaste.")
            break

        intento = input("Introduce una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Entrada no válida.")
            continue

        if intento in letras_adivinadas or intento in letras_erradas:
            print("Ya usaste esa letra.")
            continue

        if intento in palabra_secreta:
            letras_adivinadas.append(intento)
            print("¡Acierto!")
        else:
            letras_erradas.append(intento)
            vidas -= 1
            print("¡Fallo!")

    if vidas == 0:
        print(f"\nGAME OVER. La palabra era: {palabra_secreta}")
