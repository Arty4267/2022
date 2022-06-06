class Calefactor:
    __marca = ''
    __modelo = ''

    def __init__(self, mar, mod):
        self.__marca = mar
        self.__modelo = mod
    
    def __str__(self):
        cadena = self.__marca + ' - ' + self.__modelo
        return cadena