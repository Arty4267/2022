from Carrera import Carrera
from ManejadorCarreras import ManejoCarreras

class Facultad:
    __codigo = None
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = None
    __carreras = None

    def __init__(self, cod, nom, dir, loc, tele):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dir
        self.__localidad = loc
        self.__telefono = tele
        self.__carreras = ManejoCarreras()
    
    def agregarcarrera(self, carrera):
        self.__carreras.append(carrera)
    
    def getcod(self): return self.__codigo
    def getnombre(self): return self.__nombre
    def getlocalidad(self): return self.__localidad
    def gettelefono(self): return self.__telefono

    def getcarreras(self):
        cadena = "Nombre: {0}\n".format(self.__nombre)
        cadena +=("{0:50}{1}".format("Nombre de carrera", "Duracion"))
        for carr in self.__carreras:
            cadena += "\n{0:50}{1}".format(carr.getnom(), carr.getdur())
        return cadena
    
    def getfacultades(self, nomb):
        carr = self.__carreras.getnombcarrea(nomb)
        cadena = 'Codigo: {0}-{1}\n'.format(self.__codigo), carr.getcod()
        cadena += 'Nombre de la facultad: {0}\n'.format(self.__nombre)
        cadena += 'Localidad: {0}'.format(self.__localidad)
        return cadena