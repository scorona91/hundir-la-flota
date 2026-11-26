# IMPORTACIONES
from clases import Tablero
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_maquina
from variables import (
    ID_JUGADOR,
    ID_MAQUINA,
    RESULTADO_DISPARO_AGUA,
    RESULTADO_DISPARO_TOCADO,
    RESULTADO_DISPARO_REPETIDO
)

# CREAR LOS TABLEROS
tablero_jugador = Tablero(ID_JUGADOR)
tablero_maquina = Tablero(ID_MAQUINA)

# COLOCAR LOS BARCOS ALEATORIAMENTE
tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()

# INICIO DE LA PARTIDA
mostrar_instrucciones()

print("\nTu tablero:")
tablero_jugador.mostrar()

print("\nTablero de la máquina:")
tablero_maquina.mostrar(ocultar_barcos=True)

# DESARROLLO DE LA PARTIDA
while True:

    # TURNO DEL JUGADOR
    print("\n--- TU TURNO ---")
    fila, columna = pedir_coordenadas()

    resultado = tablero_maquina.recibir_disparo(fila, columna)

    if resultado == RESULTADO_DISPARO_REPETIDO:
        print("Ya habías disparado en esa casilla. Inténtalo de nuevo.")
        continue

    if resultado == RESULTADO_DISPARO_TOCADO:
        print("¡Has tocado un barco!")
        tablero_maquina.mostrar(ocultar_barcos=True)

        if tablero_maquina.vidas == 0:
            break

        continue

    if resultado == RESULTADO_DISPARO_AGUA:
        print("¡Agua! No has acertado.")

    # TURNO DE LA MÁQUINA
    print("\n--- TURNO DE LA MÁQUINA ---")
    maquina_sin_disparos = False

    while True:
        disparo = disparo_maquina(tablero_jugador.disparos)

        if disparo is None:
            print("La máquina no tiene más casillas disponibles.")
            maquina_sin_disparos = True
            break

        fila, columna = disparo
        print(f"La máquina dispara en la posición {fila}, {columna}")

        resultado = tablero_jugador.recibir_disparo(fila, columna)

        if resultado == RESULTADO_DISPARO_TOCADO:
            print("¡La máquina ha tocado uno de tus barcos!")
            tablero_jugador.mostrar()

            if tablero_jugador.vidas == 0:
                break

            continue

        if resultado == RESULTADO_DISPARO_AGUA:
            print("La máquina ha fallado.")

        break

    # COMPROBAR SI LA PARTIDA HA TERMINADO
    if tablero_jugador.vidas == 0 or maquina_sin_disparos:
        break

    # MOSTRAR LOS TABLEROS ACTUALIZADOS
    print("\nTu tablero:")
    tablero_jugador.mostrar()

    print("\nTablero de la máquina:")
    tablero_maquina.mostrar(ocultar_barcos=True)

# FINAL DE LA PARTIDA
print("\n--- FIN DE LA PARTIDA ---")

if tablero_maquina.vidas == 0:
    print("¡ENHORABUENA! Has hundido todos los barcos. ¡HAS GANADO!")

elif tablero_jugador.vidas == 0:
    print("La máquina ha hundido todos tus barcos. ¡HAS PERDIDO!")
else:
    print("La partida ha terminado porque no quedan disparos disponibles.")

# MOSTRAR EL ESTADO FINAL DE LOS TABLEROS
print("\nTu tablero final:")
tablero_jugador.mostrar()

print("\nTablero final de la máquina:")
tablero_maquina.mostrar()

