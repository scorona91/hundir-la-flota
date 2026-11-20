# Variable que indica el tamaño del tablero del juego (10x10).
TAMANO_TABLERO = 10

# Definición de los barcos y sus tamaños.
BARCOS = {"lancha_1": 1, "lancha_2": 1, "lancha_3": 1, "lancha_4": 1,
          "crucero_1": 2, "crucero_2": 2, "crucero_3": 2,
          "acorazado_1": 3, "acorazado_2": 3, "portaaviones": 4}

# Símbolos del tablero
AGUA = "~"
BARCO = "O"
BARCO_TOCADO = "X"
AGUA_DISPARADA = "*"

# Total de las casillas ocupadas por los barcos en el tablero.
TOTAL_CASILLAS_BARCOS = sum(BARCOS.values())

# Variables que indican el resultado de un disparo.
RESULTADO_DISPARO_AGUA = "agua"
RESULTADO_DISPARO_TOCADO = "tocado"
RESULTADO_DISPARO_REPETIDO = "repetido"

# Orientaciones posibles para colocar los barcos en el tablero,
# nombre: (cambio de fila, cambio de columna).
ORIENTACIONES = {"norte": (-1, 0), "sur": (1, 0), "este": (0, 1), "oeste": (0, -1)}

# Identificadores de los jugadores.
ID_JUGADOR = "jugador"
ID_MAQUINA = "maquina"
