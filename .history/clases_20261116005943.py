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
        self.barcos = BARCOS.copy()   # se guardan los barcos y las vidas ,utilizo copy para no tocar la original de BARCOS
        self.vidas = TOTAL_CASILLAS_BARCOS 
     
    def mostrar(self, ocultar_barcos=False):
        print(f"/n--- TABLERO DE : {self.id_jugador} ---") #mostrar el titulo del tablero
        for fila in range(self.tamano):
            linea= []
            for columna in range(self.tamaño):
                if self.disparos[fila,columna] == BARCO_TOCADO:
                    simbolo = BARCO_TOCADO
                elif self.disparos[fila,columna]== AGUA_DISPARADA:
                    simbolo = AGUA_DISPARADA
                elif self.tablero[fila,columna] == BARCO and ocultar_barcos:
                    simbolo = BARCO
                else:
                    simbolo = AGUA
                    linea.append(simbolo)

             print(" ".join(linea))
            
    def recibir_disparo(self,fila,columna):
        if not (0 <= fila <self.tamano and 0 <= columna < self.tamano):  # comprobar que las coordenadas sean validas 
            return "invalido"     
        if self.disparos[fila,columna] != AGUA:  #COMPROBAR SI YA SE HA DISPARADO EN ESA CASILLA
            return RESULTADO_DISPARO_REPETIDO
        if self.tablero[fila,columna]==BARCO: # COMPRBAR SI HAY UN BARCO EN ESA CASILLA 
            self.disparos[fila,columna] = BARCO_TOCADO
            self.vidas -= 1
            return RESULTADO_DISPARO_TOCADO
        else: 
            self.disparos[fila,columna] = AGUA_DISPARADA
            return RESULTADO_DISPAROS_AGUA

        def colocar_barcos(self):     #recorrer todos los barcos y colocarlos en el tablero de forma aleatoria 
            for nombre,tamano in self.barcos.items():
                colocado = False
                while not colocado: 
                    fila = np.random.randint(0,self.tamano) #posicion aleatoria 
                    columna = np.random.randint(0,self.tamano)
                    orientacion = np.random.choice(list(ORIENTACIONES.keys())) #orientacion aleatoria
                    
               cambio_fila,cambio_columna = ORIENTACIONES[orientacion]
            
             #calcular las posiciones del barco segun el tamaño y la orientacion
            posiciones=[]
            for i in range(tamano): 
                nueva_fila = fila + i * cambio_fila
                nueva_columna = columna + i * cambio_columna
                posiciones.append((nueva_fila,nueva_columna))
    dentro_tablero= all(
        0<= f < self.tamano and 0<= c < self.tamano
        for f,c in posiciones)

        if not dentro_tablero: 
        continue 
        posiciones_libres = all (  self.tablero[f,c] == AGUA 
            for f,c in posiciones)  
        if

                
        
