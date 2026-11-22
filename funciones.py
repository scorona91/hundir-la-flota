# IMPORTACIONES
import random
from variables import (TAMANO_TABLERO, CASILLA_VACIA, INSTRUCCIONES,
                       MENSAJE_COORDENADAS, MENSAJE_ERROR, MENSAJE_FUERA)


# REGLAS DEL JUEGO
def mostrar_instrucciones():
    print(INSTRUCCIONES)


# COORDENADAS DEL JUGADOR
def pedir_coordenadas():
    while True:
        try:
            coordenadas = input(MENSAJE_COORDENADAS)
            fila, columna = coordenadas.split(",")
            fila = int(fila)
            columna = int(columna)

            if fila >= 0 and fila < TAMANO_TABLERO:
                if columna >= 0 and columna < TAMANO_TABLERO:
                    return fila, columna

            print(MENSAJE_FUERA)

        except ValueError:
            print(MENSAJE_ERROR)


# DISPAROS DE LA MÁQUINA
def disparo_maquina(disparos):
    casillas_libres = []

    for fila in range(TAMANO_TABLERO):
        for columna in range(TAMANO_TABLERO):
            if disparos[fila, columna] == CASILLA_VACIA:
                casillas_libres.append((fila, columna))

    if len(casillas_libres) == 0:
        return None

    return random.choice(casillas_libres)
