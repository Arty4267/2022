from ClaseAparatos import Aparatos

class Nodo:
    __aparato = None
    __siguiente = None
    
    def __init__(self, aparato):
        self.__aparato = aparato
        self.__siguiente = None
    
    def setsiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getaparato(self):
        self.__aparato