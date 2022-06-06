from ClaseAparatos import Aparatos
import json
from pathlib import Path

class Televisor(Aparatos):
    __tipopantalla = ''
    __pulgadas = 0
    __tipodefinicion = ''
    __conexionInternet = None

    def __init__(self, mar, mod, col, pais, pre, pant, pulg, defi, conex):
        super().__init__(mar, mod, col, pais, pre)
        self.__tipopantalla = pant
        self.__pulgadas = pulg
        self.__tipodefinicion = defi
        self.__conexionInternet = conex
    
    def calculaimporte(self):
        importe = super().__preciobase

        if self.__tipodefinicion == 'SD':
            importe += (1 * super().__preciobase) / 100
        elif self.__tipodefinicion == 'HD':
            importe += (2 * super().__preciobase) / 100
        elif self.__tipodefinicion == 'FULL HD':
            importe += (3 * super().__preciobase) / 100
        
        if self.__conexionInternet:
            importe += (10 * super().__preciobase) / 100

        return importe
    
    def __str__(self) -> str:
        cadena = super().__str__() + ' - ' + self.__tipopantalla + ' - ' + self.__pulgadas + ' - ' + self.__tipodefinicion
        return cadena
    
    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
            marca = super().__marca,
            modelo = super().__modelo,
            color = super().__color,
            paisFabricacion = super().__paisFabricacion,
            preciobase = super().__preciobase,
            tipopantalla = self.__tipopantalla,
            pulgadas = self.__pulgadas,
            tipodefinicion = self.__tipodefinicion,
            conexionInternet = self.__conexionInternet
        )
        )
        return d