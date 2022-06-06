from ClaseFlores import Flores
import csv

class ManejoFlores:
    __listaflores = []

    def __init__(self):
        self.__listaflores = []
    
    def cargaflores(self):
        archivo = open('Flores.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            f = Flores(fila[0], fila[1], fila[2], fila[3])
            self.__listaflores.append(f)
        archivo.close()
    
    def muestralista(self):
        for i in range(self.__listaflores.count):
            print(self.__listaflores[i])
    
    def getlen(self): return len(self.__listaflores)
    
    def buscarflor(self, cod):
        if cod <= self.__listaflores.count:
            return self.__listaflores[cod]
        else: return None
    
    """def getlista(self): return self.__listaflores"""