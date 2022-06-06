from turtle import clear
from ManejoContrato import ManejoContrato
from ManejoEquipos import ManejoEquipo
import os

if __name__ == '__main__':
    ManejoEquipo.cargaequipo()
    print('================ Menu ================')
    print('1- Crear contrato')
    print('2- Consultar jugadores contratados')
    print('3- Consultar contratos')
    print('4- Obtener importe de contratos')
    print('5- Guardar contratos')
    print('6- Salir')
    print('======================================')
    op = int(input('---> '))
    while op != 6:

        if op == 1:
            print('1- Crear contrato')
            ManejoContrato.crearcontrato()
            input('ENTER para continuar')
            os.system(clear)
        
        if op == 2:
            print('2- Consultar jugadores contratados')
            ManejoContrato.consultajugador()
            input('ENTER para continuar')
            os.system(clear)
        
        if op == 3:
            print('3- Consultar contratos')
            ManejoContrato.consultarcontrato()
            input('ENTER para continuar')
            os.system(clear)
        
        if op == 4:
            print('4- Obtener importe de contratos')
            ManejoContrato.calcularimporte()
            input('ENTER para continuar')
            os.system(clear)

        if op == 5:
            print('5- Guardar contratos')
            
            input('ENTER para continuar')
            os.system(clear)

        print('================ Menu ================')
        print('1- Crear contrato')
        print('2- Consultar jugadores contratados')
        print('3- Consultar contratos')
        print('4- Obtener importe de contratos')
        print('5- Guardar contratos')
        print('6- Salir')
        print('======================================')
        op = int(input('---> '))