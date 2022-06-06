from datetime import datetime

class Contrato:
    __fechainicio = ''
    __fechafin = ''
    __pagomensual = 0
    __equipo = ''
    __jugador = ''

    def __init__(self, fef, pa, eq, ju):
        self.__fechafin = fef
        self.__pagomensual = pa
        self.__equipo = eq
        self.__jugador = ju
    
    @classmethod
    def addfechainicio(cls):
        cls.__fechainicio = datetime.today().strftime('%d-%m-%y')
    
    @classmethod
    def getfechainicio(cls): return cls.__fechainicio
    
    def getjugador(self): return self.__jugador
    def getequipo(self): return self.__equipo
    def getfechafin(self): return self.__fechafin
    def getpago(self): return self.__pagomensual