import imp
from turtle import clear
from ClaseColeccion import Coleccion
import os

if __name__ == '__main__':
    Coleccion.agregacalefactores()
    print('=================== Menu ===================')
    print('1- Consultar calefactor de gas')
    print('2- Consultar calefactor electrico')
    print('3- Listar calefactores de menos consumo')
    print('4- Salir')
    print('============================================')
    op = int(input('---> '))

    if op == 1:
        print('1- Consultar calefactor de gas')
        Coleccion.consultarconsumogas()
        os.system(clear)
    
    if op == 2:
        print('2- Consultar calefactor electrico')
        Coleccion.consultarconsumoelectrico()
        os.system(clear)
    
    if op == 3:
        print('3- Listar calefactores de menos consumo')
        Coleccion.listarminimos()
        os.system(clear)

    while op != 4:
        print('=================== Menu ===================')
        print('1- Consultar calefactor de gas')
        print('2- Consultar calefactor electrico')
        print('3- Listar calefactores de menos consumo')
        print('4- Salir')
        print('============================================')
        op = int(input('---> '))