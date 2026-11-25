# IMPORTACIONES
import random
from variables import (TAMANO_TABLERO, AGUA, INSTRUCCIONES,
                       MENSAJE_COORDENADAS, MENSAJE_ERROR, MENSAJE_FUERA)


# REGLAS DEL JUEGO
def mostrar_instrucciones():
    """Imprimir las instrucciones del juego"""
    print(INSTRUCCIONES)


# COORDENADAS DEL JUGADOR
def pedir_coordenadas():
    """Solicitar al jugador que ingrese las coordenadas de disparo en formato "fila, columna".
    Validar las coordenadas ingresadas y repetir la pregunta hasta que se ingresen coordenadas válidas.
    Returns:
        tuple: Coordenadas (fila, columna) ingresadas por el jugador."""

    while True:
        try:
            coordenadas = input(MENSAJE_COORDENADAS)
            fila, columna = coordenadas.split(",")
            fila = int(fila)
            columna = int(columna)

            if 0 <= fila < TAMANO_TABLERO and 0 <= columna < TAMANO_TABLERO:
                return fila, columna

            print(MENSAJE_FUERA)

        except ValueError:
            print(MENSAJE_ERROR)


# DISPAROS DE LA MÁQUINA
def disparo_maquina(disparos):
    """Genera una coordenada aleatoria para el disparo de la máquina, asegurándose de que no haya sido disparada previamente.
    Args:
        disparos (list): Lista que representa el estado del tablero de disparos de la máquina.
        Returns:
        tuple: Coordenadas (fila, columna) del disparo de la máquina."""

    casillas_libres = []

    for fila in range(TAMANO_TABLERO):
        for columna in range(TAMANO_TABLERO):
            if disparos[fila, columna] == AGUA:
                casillas_libres.append((fila, columna))

    if len(casillas_libres) == 0:
        return None

    return random.choice(casillas_libres)
