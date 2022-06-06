class Carrera:
    __codigo = None
    __nombre = ''
    __titulo = ''
    __duracion = ''
    __nivel = ''
    
    def __init__(self, cod, nom, tit, dur, niv):
        self.__codigo = cod
        self.__nombre = nom
        self.__titulo = tit
        self.__duracion = dur
        self.__nivel = niv
    
    def getcod(self): return self.__codigo
    def getnom(self): return self.__nombre
    def gettit(self): return self.__titulo
    def getdur(self): return self.__duracion
    def getniv(self): return self.__nivel