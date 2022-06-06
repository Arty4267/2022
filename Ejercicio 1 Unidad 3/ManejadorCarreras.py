from Carrera import Carrera

class ManejoCarreras:
    __carreras = None
    __actual = 0

    def __init__(self):
        self.__carreras = []
        self.__actual = 0

    def __iter__(self):
        self.__actual = 0
        return self
    
    def __next__(self):
        if self.__actual >= (len(self.__carreras)):
            raise StopIteration
        else:
            carr = self.__carreras[self.__actual]
            self.__actual += 1
            return carr

    def agregacarrera(self, carrera):
        if isinstance(carrera, Carrera):
            self.__carreras.append(carrera)
    
    def buscarcarrera(self, nomb):
        i = 0
        while i < (len(self.__carreras)) and self.__carreras[i].getnomb().lower() != nomb.lower():
            i += 1
        
        if i == len(self.__carrera):
            i = -1
        
        return i
    
    def getnombcarrea(self, nomb):
        car = None
        aux = self.buscarcarrera(nomb)
        if aux != -1:
            car = self.__carreras[aux]
        return car