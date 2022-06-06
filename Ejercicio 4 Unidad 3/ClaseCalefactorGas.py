from ClaseCalefactor import Calefactor

class Gas(Calefactor):
    __matricula = ''
    __calorias = 0
    def __init__(self, mar, mod, mat, cal):
        super().__init__(mar, mod)
        self.__matricula = mat
        self.__calorias = cal
    
    def getcalorias(self): return self.__calorias

    def __str__(self):
        cadena = super().__str__() + ' - ' + self.__matricula + ' - ' + self.__calorias
        return cadena