from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor
from ClaseLavarropas import Lavarropas
from ClaseLista import ListaAparatos
import json

class Coleccion:
    __aparatos = None

    def __init__(self):
        self.__aparatos = ListaAparatos()
    
    def cargalista(self, aparato):
        marca = input('Ingrese marca de aparato: ')
        modelo = input('Ingrese modelo del aparato: ')
        ListaAparatos.agregarElemento(aparato)
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,aparatos=[Aparatos.toJSON()for Aparatos in self.__aparatos]
        )
        return d