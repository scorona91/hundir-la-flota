import numpy as np 
from variables import (TAMANO_TABLERO,BARCOS,AGUA,BARCO,BARCO_TOCADO,AGUA_DISPARADA,
                       TOTAL_CASILLAS_BARCOS,RESULTADO_DISPARO_AGUA,
                       RESULTADO_DISPARO_TOCADO,RESULTADO_DISPARO_REPETIDO

)
class Tablero:
    def__init__(self,id_jugador):         #Constructor de la clase Tablero, recibe el identificador del jugador 
        self.id_jugador = id_jugador
        self.tamano = TAMANO_TABLERO

        self.tablero = np.full((self.tamano,self.tamano),AGUA)
        self.disparos = np.full((self.tamano,self.tamano),AGUA)
    