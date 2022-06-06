from ClaseAparatos import Aparatos

class Lavarropas(Aparatos):
    __capacidadlavado = 0
    __rpm = 0
    __cantprogramas = 0
    __tipocarga = ''

    def __init__(self, mar, mod, col, pais, pre, caplav, rp, cant, tip):
        super().__init__(mar, mod, col, pais, pre)
        self.__capacidadlavado = caplav
        self.__rpm = rp
        self.__cantprogramas = cant
        self.__tipocarga = tip
    
    def calculaimporte(self):
        importe = super().__preciobase

        if self.__capacidadlavado <= 5:
            importe += (1 * super().__preciobase) / 100
        elif self.__capacidadlavado > 5:
            importe += (3 * super().__preciobase) / 100
        
        return importe
    
    def __str__(self):
        cadena = super().__str__() + self.__capacidadlavado + ' - ' + self.__rpm + ' - ' + self.__cantprogramas + ' - ' + self.__tipocarga
        return cadena
    
    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
            marca = super().__marca,
            modelo = super().__modelo,
            color = super().__color,
            paisFabricacion = super().__paisFabricacion,
            preciobase = super().__preciobase,
            capacidadlavado = self.__capacidadlavado,
            rpm = self.__rpm,
            cantprogramas = self.__cantprogramas,
            tipocarga = self.__tipocarga
        )
        )
        return d