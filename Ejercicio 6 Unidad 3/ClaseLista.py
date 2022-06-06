from ClaseNodo import Nodo
from zope.interface import implementer
from ClaseInterface import ArreInterface

@implementer(ArreInterface)

class ListaAparatos:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None
    
    def agregarElemento(self, descripcion):
        nodo = Nodo(descripcion)
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo = nodo

    def insertarElemento(self, descripcion):
        pass
    
    def mostrarElemento(self, descripcion):
        aux = self.__comienzo
        while aux != None:
            print(aux.getaparato())
            aux = aux.getSiguiente()

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
        comienzo = self.__comienzo,
        )
        )
        return d