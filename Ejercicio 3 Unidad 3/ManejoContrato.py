from csv import writer
import csv
from datetime import datetime
from venv import create
from ClaseContrato import Contrato
from ManejoJugadores import ManejoJugador
from ManejoEquipos import ManejoEquipo
import numpy as np

class ManejoContrato:
    __contratos = np.empty()

    def __init__(self):
        self.__contratos = np.empty()

    def crearcontrato(self):
        Contrato.addfechainicio()
        fechafin = input('Ingrese fecha de finalizacion dd/mm/aa: ')
        fechafin = datetime.strftime(fechafin, '%d/%m/%y')
        pago = int(input('Ingrese pago mensual: '))
        jug = ManejoJugador.agregajugador()
        nequip = input('Ingrese nombre del equipo: ')
        equip = ManejoEquipo.retornaequipo(nequip)
        contr = Contrato(fechafin, pago, equip, jug)
        np.append(contr)
        print('Contrato realizado')

    def consultajugador(self):
        dni = int(input('Ingrese DNI: '))
        for i in np.nditer(self.__contratos):
            jug = self.__contratos[i].getjugador()
            if dni == jug.getdni():
                eq = self.__contratos[i].getequipo()
                print('{} {} {}'.format(eq.getnomb(), self.__contratos[i].getfechafin()))
            else:
                print('El jugador no esta contratado')
    
    def consultarcontrato(self):
        nomb = input('Ingrese nombre del equipo: ')
        for i in np.nditer(self.__contratos):
            if (self.__contratos[i].getfechainicio().year - self.__contratos[i].getfechafin().year) * 12 + self.__contratos[i].getfechainicio().month - self.__contratos[i].getfechafin().month == 6:
                eq = self.__contratos[i].getequipo()
                if eq.getnomg() == nomb:
                    jug = self.__contratos[i].getjugador()
                    print(jug)
    
    def calcularimporte(self):
        cont = 0
        nomb = input('Ingrese nombre del equipo: ')
        for i in np.nditer(self.__contratos):
            eq = self.__contratos[i].getequipo()
            if eq.getnomb() == nomb:
                cont += self.__contratos[i].getpago()
    
    def guardarcontrato(self):
        archivo = create('Contratos.csv', 'w')
        writer = csv.writer(archivo,delimiter=';')
        