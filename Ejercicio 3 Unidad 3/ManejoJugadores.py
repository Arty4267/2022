from ClaseJugador import Jugador

class ManejoJugador:
    __jugadores = []

    def __init__(self):
        self.__jugadores = []
    
    def agregajugador(self):
        nomb = input('Ingrese nombre: ')
        dni = int(input('Ingrese DNI: '))
        ciudad = input('Ingrese ciudad natal: ')
        paisorigen = input('Ingrese pais de origen: ')
        fechanacimiento = input('Ingrese fecha de nacimiento: ')
        jug = Jugador(nomb, dni, ciudad, paisorigen, fechanacimiento)
        self.__jugadores.append(jug)
        return jug
