from ClaseAparatos import Aparatos
import json
from pathlib import Path

class Heladera(Aparatos):
    __capacidad = 0
    __freezer = None
    __ciclica = None

    def __init__(self, mar, mod, col, pais, pre, capa, free, cic):
        super().__init__(mar, mod, col, pais, pre)
        self.__capacidad = capa
        self.__freezer = free
        self.__ciclica = cic
    
    def calculaimporte(self):
        importe = super().__preciobase

        if not self.__freezer:
            importe += (1 * super().__preciobase) / 100
        elif self.__freezer:
            importe += (5 * super().__preciobase) / 100
        if self.__ciclica:
            importe += (10 * super().__preciobase) / 100
        
        return importe
    
    def __str__(self):
        cadena = super().__str__() + ' - ' + self.__capacidad
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
            capacidad = self.__capacidad,
            freezer = self.__freezer,
            ciclica = self.__ciclica
            )
        )
        return d