import numpy as np

try:
    from variables import (
        TAMANO_TABLERO,
        BARCOS,
        AGUA,
        BARCO,
        BARCO_TOCADO,
        AGUA_DISPARADA,
        TOTAL_CASILLAS_BARCOS,
        RESULTADO_DISPARO_AGUA,
        RESULTADO_DISPARO_TOCADO,
        RESULTADO_DISPARO_REPETIDO,
        ORIENTACIONES,
    )
except ImportError:
    TAMANO_TABLERO = 10
    BARCOS = {"portaaviones": 5, "destructor": 3}
    AGUA = 0
    BARCO = 1
    BARCO_TOCADO = 2
    AGUA_DISPARADA = 3
    TOTAL_CASILLAS_BARCOS = sum(BARCOS.values())
    RESULTADO_DISPARO_AGUA = "agua"
    RESULTADO_DISPARO_TOCADO = "tocado"
    RESULTADO_DISPARO_REPETIDO = "repetido"
    ORIENTACIONES = {"HORIZONTAL": (0, 1), "VERTICAL": (1, 0)}


class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tamano = TAMANO_TABLERO
        self.tablero = np.full((self.tamano, self.tamano), AGUA)
        self.disparos = np.full((self.tamano, self.tamano), AGUA)
        self.barcos = BARCOS.copy()
        self.vidas = TOTAL_CASILLAS_BARCOS

    def mostrar(self, ocultar_barcos=False):
        print(f"\n--- TABLERO DE: {self.id_jugador} ---")
        for fila in range(self.tamano):
            linea = []
            for columna in range(self.tamano):
                if self.disparos[fila, columna] == BARCO_TOCADO:
                    simbolo = BARCO_TOCADO
                elif self.disparos[fila, columna] == AGUA_DISPARADA:
                    simbolo = AGUA_DISPARADA
                elif self.tablero[fila, columna] == BARCO and not ocultar_barcos:
                    simbolo = BARCO
                else:
                    simbolo = AGUA
                linea.append(str(simbolo))
            print(" ".join(linea))

    def recibir_disparo(self, fila, columna):
        if not (0 <= fila < self.tamano and 0 <= columna < self.tamano):
            return "invalido"
        if self.disparos[fila, columna] != AGUA:
            return RESULTADO_DISPARO_REPETIDO
        if self.tablero[fila, columna] == BARCO:
            self.disparos[fila, columna] = BARCO_TOCADO
            self.vidas -= 1
            return RESULTADO_DISPARO_TOCADO
        self.disparos[fila, columna] = AGUA_DISPARADA
        return RESULTADO_DISPARO_AGUA

    def colocar_barcos(self):
        for nombre, tamano in self.barcos.items():
            colocado = False
            while not colocado:
                fila = np.random.randint(0, self.tamano)
                columna = np.random.randint(0, self.tamano)
                orientacion = np.random.choice(list(ORIENTACIONES.keys()))
                cambio_fila, cambio_columna = ORIENTACIONES[orientacion]

                posiciones = []
                for i in range(tamano):
                    nueva_fila = fila + i * cambio_fila
                    nueva_columna = columna + i * cambio_columna
                    posiciones.append((nueva_fila, nueva_columna))

                dentro_tablero = all(
                    0 <= f < self.tamano and 0 <= c < self.tamano
                    for f, c in posiciones
                )

                if not dentro_tablero:
                    continue

                posiciones_libres = all(
                    self.tablero[f, c] == AGUA
                    for f, c in posiciones
                )

                if posiciones_libres:
                    for f, c in posiciones:
                        self.tablero[f, c] = BARCO
                    colocado = True

                
        
