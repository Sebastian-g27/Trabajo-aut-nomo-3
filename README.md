# Juego del Ahorcado - Python Modular

Este proyecto consiste en una versión clásica del juego "El Ahorcado", desarrollada en Python. El programa aplica conceptos de **programación modular**, separando la lógica del motor del juego de la interfaz de usuario para mejorar la organización y escalabilidad.

---

## Objetivo del Programa
El objetivo principal es proporcionar una experiencia de juego interactiva por consola donde el usuario pueda poner a prueba su vocabulario. Técnicamente, el proyecto busca demostrar el uso de:
*   Importación de librerías personalizadas.
*   Manejo de estructuras de control (bucles y condicionales).
*   Gestión de datos a través de diccionarios y listas.

---

## Funcionalidades Principales

1.  **Programación Modular:** El código se divide en una librería lógica (`motor_juego.py`) y un ejecutable principal (`main.py`).
2.  **Gestión de Usuario:** El sistema solicita y almacena temporalmente el nombre y la edad del jugador para personalizar la partida.
3.  **Sistema de Dificultades:** 
    *   **Fácil:** Palabras cortas y 8 vidas.
    *   **Medio:** Palabras de longitud media y 6 vidas.
    *   **Difícil:** Palabras complejas y solo 4 vidas.
4.  **Menú Interactivo:** Navegación fluida entre ver reglas, iniciar el juego o terminar el programa.
5.  **Validaciones:** El sistema detecta si el usuario ingresa números, caracteres especiales o letras repetidas para evitar errores en la partida.

---

## Estructura del Proyecto

*   `main.py`: Punto de entrada del programa. Contiene el menú y la gestión de la interfaz de usuario.
*   `ahorcado_lib.py`: Librería que contiene la lógica, las palabras secretas y el control de vidas.

---

## 🔧 Cómo ejecutarlo
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python 3.x instalado.
3. Ejecuta el archivo principal desde tu terminal:
   ```bash
   python main.py
