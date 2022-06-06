from operator import eq


class Jugador:
    __nomb = ''
    __dni = 0
    __ciudadnatal = ''
    __paisorigen = ''
    __fechanacimiento = ''

    def __init__(self, no, dn, ci, pa, fe):
        self.__nomb = no
        self.__dni = dn
        self.__ciudadnatal = ci
        self.__paisorigen = pa
        self.__fechanacimiento = fe
    
    def getdni(self): return self.__dni

    def __str__(self):
        cadena = self.__dni + ' - ' + self.__nomb + ' - ' + self.__ciudadnatal + ' - ' + self.__paisorigen + ' - ' + self.__fechanacimiento
        return cadena