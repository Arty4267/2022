class Ventana:
    __titulo = ''
    __supX = 0
    __supY = 0
    __infX = 500
    __infY = 500
    
    def __init__(self, tit = '', sx = 0, sy = 0, ix = 500, iy = 500):
        self.__titulo = tit
        self.__supX = sx
        self.__supY = sy
        self.__infX = ix
        self.__infY = iy
    
    def mostrar(self):
        print("{} SUP({},{}) INF ({}, {})".format(self.__titulo, self.__supX, self.__supY, self.__infX, self.__infY))
    
    def getTitulo(self): return self.__titulo
    
    def alto(self):
        a = "(" + "{}".format(self.__supY) + ", " + "{}".format(self.__infY) + ")"
        """print("({}, {})".format(self.__supY, self.__infY))"""
        return a
    
    def ancho(self):
        a = "(" + "{}".format(self.__supX) + ", " + "{}".format(self.__infX) + ")"
        return a
        """print("({}, {})".format(self.__supX, self.__infX))"""
        
    def moverDerecha(self, x):
        aX = self.__supX  + x
        aY = self.__infX + x
        if aX >= 0 and aX <= 500:
            if aY >= 0 and aY <= 500:
                self.__supX = aX
                self.__infX = aY
            else:
                print("Error: No se puede mover a la derecha")
                
    def moverIzquierda(self, x):
        aX = self.__supX  - x
        aY = self.__infX - x
        if aX >= 0 and aX <= 500:
            if aY >= 0 and aY <= 500:
                self.__supX = aX
                self.__infX = aY
            else:
                print("Error: No se puede mover a la Izquierda")
                
    def bajar(self, y = 1):
        aX = self.__supY  - y
        aY = self.__infY - y
        if aX >= 0 and aX <= 500:
            if aY >= 0 and aY <= 500:
                self.__supY = aX
                self.__infY = aY
            else:
                print("Error: No se puede bajar")
                
    def subir(self, y = 1):
        aX = self.__supY  + y
        aY = self.__infY + y
        if aX >= 0 and aX <= 500:
            if aY >= 0 and aY <= 500:
                self.__supY = aX
                self.__infY = aY
            else:
                print("Error: No se puede subir")