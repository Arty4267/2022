from turtle import clear
from ManejadorCarreras import ManejoCarreras
from ManejadorFacultad import ManejoFacultad
import os

if __name__ == '__main__':
    print('=================== Menu ===================')
    print('1- Mostrar carreras por codigo de facultad')
    print('2- Mostrar facultad de una carrera')
    print('3- Salir')
    print('===========================================')
    op = int(input('----> '))
    while op != 3:

        if op == 1:
            print('1- Mostrar carreras por codigo de facultad')
            ManejoFacultad.muestrafacultad()
            os.system(clear)
        
        if op == 2:
            print('2- Mostrar facultad de una carrera')
            ManejoFacultad.muestracarreras()
            os.system(clear)

        print('=================== Menu ===================')
        print('1- Mostrar carreras por codigo de facultad')
        print('2- Mostrar facultad de una carrera')
        print('3- Salir')
        print('===========================================')
        op = int(input('----> '))