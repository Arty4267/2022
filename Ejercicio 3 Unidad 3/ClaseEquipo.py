class Equipo:
    __nomb = ''
    __ciudad = ''

    def __init__(self, no, ci):
        self.__nomb = no
        self.__ciudad = ci
    
    def getnomb(self): return self.__nomb