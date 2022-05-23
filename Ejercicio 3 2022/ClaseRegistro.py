from numpy import isin

#Atributos
class Registro:
    __temp = 0
    __hume = 0
    __pres = 0
#Metodos  
    def __init__(self, temp:float, hume, pres):
        if isinstance(temp, float) or isinstance(temp, int):
            self.__temp = temp
        if isinstance(hume, float) or isinstance(hume, int):
            self.__hume = hume
        if isinstance(pres, float) or isinstance(pres, int):
            self.__pres = pres
    
    def gettemp(self):
        return self.__temp
    
    def gethume(self):
        return self.__hume
    
    def getpres(self):
        return self.__pres
    
    def __str__(self):
        return "temp: {0}\nhume: {1}\npres: {2}".format(self.gettemp(), self.gethume(), self.getpres())