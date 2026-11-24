# IMPORTACIONES
from clases import Tablero
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_maquina
from variables import ID_JUGADOR, ID_MAQUINA

# CREAR LOS TABLEROS
tablero_jugador = Tablero(ID_JUGADOR)
tablero_maquina = Tablero(ID_MAQUINA)

# COLOCAR LOS BARCOS ALEATORIAMENTE
tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()

# INICIO DE LA PARTIDA
print("\n¡BIENVENIDO A HUNDIR LA FLOTA!")

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

    if resultado == "repetido":
        print("Ya habías disparado en esa casilla. Inténtalo de nuevo.")
        continue

    elif resultado == "tocado":
        print("¡Has tocado un barco!")

    elif resultado == "agua":
        print("¡Agua! No has acertado.")

    # COMPROBAR SI EL JUGADOR HA GANADO
    if tablero_maquina.vidas == 0:
        break

    # TURNO DE LA MÁQUINA
    print("\n--- TURNO DE LA MÁQUINA ---")
    disparo = disparo_maquina(tablero_jugador.disparos)

    if disparo is None:
        print("La máquina no tiene más casillas disponibles.")
        break

    fila, columna = disparo
    print(f"La máquina dispara en la posición {fila}, {columna}")

    resultado = tablero_jugador.recibir_disparo(fila, columna)

    if resultado == "tocado":
        print("¡La máquina ha tocado uno de tus barcos!")

    elif resultado == "agua":
        print("La máquina ha fallado.")

    # MOSTRAR LOS TABLEROS ACTUALIZADOS
    print("\nTu tablero:")
    tablero_jugador.mostrar()

    print("\nTablero de la máquina:")
    tablero_maquina.mostrar(ocultar_barcos=True)

    # COMPROBAR SI LA MÁQUINA HA GANADO
    if tablero_jugador.vidas == 0:
        break

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

