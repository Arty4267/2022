import json
from pathlib import Path

class Aparatos:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisFabricacion = ''
    __preciobase = 0

    def __init__(self, mar, mod, col, pais, pre):
        self.__marca = mar
        self.__modelo = mod
        self.__color = col
        self.__paisFabricacion = pais
        self.__preciobase = pre
    
    def getmarca(self): return self.__marca
    
    def __str__(self):
        cadena = self.__marca + ' - ' + self.__modelo + ' - ' + self.__color + ' - ' + self.__paisFabricacion + ' - ' + self.__preciobase
        return cadena