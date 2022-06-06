from asyncore import read
from ClaseCalefactorElectrico import Electrico
from ClaseCalefactorGas import Gas
import numpy as np
import csv

class Coleccion:
    __calefactores = np.empty()

    def __init__(self):
        self.__calefactores = np.empty()
    
    def agregacalefactores(self):
        arre = int(input('Ingrese cantidad de calefactores a cargar: '))
        self.__calefactores = np.empty(arre)

        band = True
        arElectrico = open('calefactor-electrico.csv')
        reader = csv.reader(arElectrico,delimiter=';')
        fila = next(reader)
        while band:
            cal = Electrico(fila[0], fila[1], fila[2])
            self.__calefactores = np.append(cal)
            try:
                fila = next(reader)
            except StopIteration:
                band = False
        arElectrico.close
        
        band = True
        arGas = open('calefactor-a-gas.csv')
        reader = csv.reader(arGas,delimiter=';')
        fila1 = next(reader)
        while band:
            ga = Gas(fila[0], fila[1], fila[2], fila[3])
            self.__calefactores = np.append(ga)
            try:
                fila1 = next(reader)
            except StopIteration:
                band = False
        arGas.close
    
    def consultarconsumogas(self):
        min = 999999
        costo = int(input('Ingrese costo por m3: '))
        cant = int(input('Ingrese cantidad estimada a consumir por m3: '))
        print('Calefactores a gas con menor costo de consumo')
        for i in np.nditer(self.__calefactores):
            if type(self.__calefactores[i]) == Gas:
                tot = (self.__calefactores[i].getcalorias() / 10000) * (cant * costo)
                if tot < min:
                    min = tot
                    print(self.__calefactores[i])
    
    def consultarconsumoelectrico(self):
        min = 999999
        costo = int(input('Ingrese costo por KWs: '))
        cant = int(input('Ingrese cantidad estimada a consumir por KWs: '))
        print('Calefactores electricos con menor costo de consumo')
        for i in np.nditer(self.__calefactores):
            if type(self.__calefactores[i]) == Electrico:
                tot = (self.__calefactores[i].getportencia() / 10000) * (cant * costo)
                if tot < min:
                    min = tot
                    print(self.__calefactores[i])
    
    def listarminimos(self):
        minGas = 999999
        minElectrico = 999999
        print('Calefactores de menor consumo')
        for i in np.nditer(self.__calefactores):
            if type(self.__calefactores[i]) == Gas:
                totG = (self.__calefactores[i].getcalorias() / 10000)
                if totG == minGas:
                    minGas = totG
                    print(self.__calefactores[i])
            elif type(self.__calefactores[i]) == Electrico:
                totE = (self.__calefactores[i].getportencia() / 10000)
                if totE < minElectrico:
                    minElectrico = totE
                    print(self.__calefactores[i])
