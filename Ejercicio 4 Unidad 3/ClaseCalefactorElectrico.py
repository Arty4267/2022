from ClaseCalefactor import Calefactor

class Electrico(Calefactor):
    __potenciamax = 0

    def __init__(self, mar, mod, pote):
        super().__init__(mar, mod)
        self.__potenciamax = pote
    
    def getpotencia(self): return self.__potenciamax

    def __str__(self):
        cadena = super().__str__() + ' - ' + self.__potenciamax
        return cadena