from zope.interface import Interface
from zope.interface import implementer

class ArreInterface(Interface):
    def insertarElemento(descripcion):
        pass

    def agregarElemento(descripcion):
        pass

    def mostrarElemento(descripcion):
        pass