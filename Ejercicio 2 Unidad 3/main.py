from turtle import clear
from ClaseManejoFlores import ManejoFlores
from ClaseManejoRamos import ManejoRamos
import os

if __name__ == '__main__':
    print("============== Menu ==============")
    print("1- Registrar ramo")
    print("2- Lista de flores mas vendidas")
    print("3- Consultar ramo vendido")
    print("4- Salir")
    print("==================================")
    op = int(input("---> "))
    while op != 4:

        if op == 1:
            print("1- Registrar ramo")
            ManejoRamos.regisramo()
            input("ENTER para continuar")
            os.system(clear)
        
        if op == 2:
            print("2- Lista de flores mas vendidas")
            ManejoRamos.contarflores()
            input("ENTER para continuar")
            os.system(clear)

        if op == 3:
            print("3- Consultar ramo vendido")
            ManejoRamos.consultaramo()
            input("ENTER para continuar")
            os.system(clear)

        print("============== Menu ==============")
        print("1- Registrar ramo")
        print("2- Lista de flores mas vendidas")
        print("3- Consultar ramo vendido")
        print("4- Salir")
        print("==================================")
        op = int(input("---> "))