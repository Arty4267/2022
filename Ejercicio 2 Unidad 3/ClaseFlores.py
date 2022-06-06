class Flores:
    __cod = 0
    __nombre = ''
    __color = ''
    __descripcion = ''

    def __init__(self, cod, nomb, col, des):
        self.__cod = cod
        self.__nombre = nomb
        self.__color = col
        self.__descripcion = des
    
    def getcod(self): return self.__cod
    def getnomb(self): return self.__nombre
    def getcolor(self): return self.__color
    def getdescrip(self): return self.__descripcion
    
    def __str__(self):
        cadena = self.__cod + ' - ' + self.__nombre + ' - ' + self.__color + ' - ' + self.__descripcion
        return cadena