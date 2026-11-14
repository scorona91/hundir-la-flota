# Variable que indica el tamañana del tablero del juego (10x10).
TAMANO_TABLERO = 10

# Definición de los barcos y sus tamaños.
BARCOS = {"lancha_1": 1, "lancha_2": 1, "lancha_3": 1, "lancha_4": 1, 
          "crucero_1": 2, "crucero_2": 2, "crucero_3": 2, 
          "acorazado_1": 3, "acorazado_2": 3, "portaaviones": 4}

# Símbolos del tablero
AGUA = "~"
BARCO ="O"
BARCO_TOCADO = "X"
AGUA_DISPARADA = "*"

# Total de las casillas ocupadas por los barcos en el tablero.
TOTAL_BARCOS = sum(BARCOS.values())
print(TOTAL_BARCOS)

