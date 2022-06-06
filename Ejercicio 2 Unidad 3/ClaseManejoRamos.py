from typing import List
from ClaseManejoRamos import ManejoRamos
from ClaseFlores import Flores
from ClaseRamo import Ramo
from ClaseManejoFlores import ManejoFlores

class ManejoRamos:
    __listaramos = None
    __regisflores = None

    def __init__(self):
        self.__listaramos = []
        self.__regisflores:List[int] = [0 for i in ManejoFlores.getlen()]
    
    def regisramo(self):
        print("============ Lista de flores a elejir ============")
        ManejoFlores.muestralista()
        print("==================================================")
        print("-Seleccione tipo de ramo ('0' para terminar)-")
        tam = input("Chico(2) - Mediano(3) - Grande(4) --> ")
        while tam != 0:
            if tam == 'Chico':
                for i in 2:
                    cod = int(input("Ingrese codigo de la flor: "))
                    f = ManejoFlores.buscarflor(cod-1)
                    if f != 0:
                        ramo = Ramo(tam, f)
                        self.__listaramos.append(ramo)
                        self.__regisflores[cod] += 1
                        print("Ramo registrado")
                    else: print("Flor no encontrada")
            elif tam == 'Mediano':
                for i in 3:
                    cod = int(input("Ingrese codigo de la flor: "))
                    f = ManejoFlores.buscarflor(cod-1)
                    if f != 0:
                        ramo = Ramo(tam, f)
                        self.__listaramos.append(ramo)
                        self.__regisflores[cod] += 1
                        print("Ramo registrado")
                    else: print("Flor no encontrada")
            elif tam == 'Grande':
                for i in 4:
                    cod = int(input("Ingrese codigo de la flor: "))
                    f = ManejoFlores.buscarflor(cod-1)
                    if f != 0:
                        ramo = Ramo(tam, f)
                        self.__listaramos.append(ramo)
                        self.__regisflores[cod] += 1
                        print("Ramo registrado")
                    else: print("Flor no encontrada")

            print("============ Lista de flores a elejir ============")
            ManejoFlores.muestralista()
            print("==================================================")
            print("-Seleccione tipo de ramo ('None' para terminar)-")
            tam = input("Chico(2) - Mediano(3) - Grande(4) --> ")
    
    def contarflores(self):
        mayores = []
        for i in 5:
            max = 0
            num = 0
            for j in range(len(self.__regisflores)):
                if self.__regisflores[j] > max:
                    max = self.__regisflores[j]
                    num = j
            mayores.append(j + 1)
            self.__regisflores[num] = 0
        print("Las 5 flores mas pedidas: ")
        for num in mayores:
            flor = ManejoFlores.buscarflor(num)
            print(flor)
    
    def consultaramo(self):
        print('Flores de ramos vendidos\n')
        for i in range(len(self.__listaramos)):
            print('Ramo nro: {} - Tamaño: {}\n'.format(i + 1, self.__listaramos[i].gettam()))
            flores = self.__listaramos[i].getlist()
            for j in len(flores):
                print(flores[j])