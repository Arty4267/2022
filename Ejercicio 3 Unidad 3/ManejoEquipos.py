from ClaseEquipo import Equipo
import numpy as np
import csv

class ManejoEquipo:
    __equipos = np.empty()

    def __init__(self):
        self.__equipos = np.empty()
    
    def cargaequipo(self):
        band = False
        archivo = open('Equipos.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            if not band:
                self.__equipos = np.empty(fila[0])
                band = True
            else:
                equi = Equipo(fila[0], fila[1])
                np.append(equi)
        archivo.close()
    
    def buscaequipo(self, nomb):
        i = 0
        res = ''
        while (i < np.size(self.__equipos)) and self.__equipos[i].getnomb != nomb:
            i += 1
        if i >= np.size(self.__equipos):
            res = 0
        else:
            res = i
        return i
    
    def retornaequipo(self, nomb):
        i = self.buscaequipo(nomb)
        return self.__equipos[i]