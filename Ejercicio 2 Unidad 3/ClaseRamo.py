from ClaseFlores import Flores

class Ramo:
    __tamaño = ''
    __flores = []

    def __init__(self, tam, flor):
        self.__tamaño = tam
        self.__flores.append(flor)
    
    def getlist(self): return self.__flores
    def gettam(self): return self.__tamaño