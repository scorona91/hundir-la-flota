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

#Mensajes de instrucciones y errores
INSTRUCCIONES = f"""Bienvenido al juego de Hundir la Flota.
Instrucciones:
1. El objetivo del juego es hundir todos los barcos del oponente.
2. El tablero es de {TAMANO_TABLERO}x{TAMANO_TABLERO} y los barcos se colocan de manera aleatoria.
Cada jugador tiene {TOTAL_CASILLAS_BARCOS} casillas ocupadas por barcos.
3. Para disparar, ingresa las coordenadas en el formato fila, columna (por ejemplo 7,8).
4. Las filas y columnas van de 0 a {TAMANO_TABLERO - 1}.
5. Si aciertas el disparo, vuelves a disparar. Si das en el agua, es el turno del oponente.
6. Los simbolos en el tablero son los siguientes:
   {AGUA} : Agua (sin disparar)
   {BARCO} : Barco (sin disparar)
   {BARCO_TOCADO} : Barco tocado
   {AGUA_DISPARADA} : Agua donde ya se ha disparado previamente
7. El juego termina cuando un jugador hunde todos los barcos del oponente.
¡Buena suertey que comience el juego!"""

MENSAJE_COORDENADAS = "Ingresa las coordenadas de disparo (fila, columna): "
MENSAJE_ERROR = "Error: Por favor, ingresa las coordenadas en el formato 'fila, columna' (por ejemplo, 7,8)."
MENSAJE_FUERA = f"Error: Las coordenadas deben estar entre 0 y {TAMANO_TABLERO - 1}. Por favor, intenta de nuevo."