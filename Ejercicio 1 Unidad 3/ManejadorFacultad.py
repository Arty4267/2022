from Facultad import Facultad
from Carrera import Carrera
import csv

class ManejoFacultad:
    __facultades = None

    def __init__(self):
        self.__facultades = []
    
    def agregarfacultad(self, facu):
        if isinstance(facu, Facultad):
            self.__facultades.append(facu)
    
    def cargarfacultades(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=';')
        band = True
        filaf = next(reader)
        while band:
            facu = Facultad(filaf[0], filaf[1], filaf[2], filaf[3], filaf[4])
            self.agregarfacultad(facu)
            try:
                filac = next(reader)
            except StopIteration:
                band = False
            while band and filac[0] == filaf[0]:
                carr = Carrera(filac[0], filac[1], filac[2], filac[3], filac[4])
                facu.agregarcarrera(carr)
                try:
                    filac = next(reader)
                except StopIteration:
                    band = False
                filaf = filac[0:-1]
        archivo.close()
    
    def buscafacultad(self, cod):
        i = 0
        while i < (len(self.__facultades)) and self.__facultades[i].getcod() != cod:
            i += 1
        
        if i == len(self.__facultades):
            i = -1
        
        return i
    
    def muestrafacultad(self):
        cod = int(input('Ingrese codigo de facultad: '))
        aux = self.buscafacultad(cod)
        if aux != -1:
            print(self.__facultades[aux].getfacultades())
        else:
            print('Facultad no encontrada')
    
    def muestracarreras(self):
        nomb = input('Ingrese nombre de la carrera: ')
        i = 0
        band = True
        while i < (len(self.__facultades)) and band:
            cadena = self.__facultades[i].getcarreras()
            if cadena == None:
                i += 1
            else:
                band = False
        
        if i == len(self.__facultades):
            print('Carrera no encontrada')
        else:
            print(cadena)