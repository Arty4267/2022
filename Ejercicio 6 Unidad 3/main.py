from ObjectEncoder import ObjectEncoder
from Menu import Menu


if __name__ == "__main__":
    unObjectEncoder = ObjectEncoder()
    unMenu = Menu()
    d = unObjectEncoder.leerArchivojson("aparatoselectronicos.json")
    unaColeccionAparatos = unObjectEncoder.decodificarDiccionario(d)
    unMenu.ejecutarMenu(unaColeccionAparatos)
    d = unaColeccionAparatos.toJSON()
    unObjectEncoder.guardarArchivojson(d, "aparatoselectronicos.json")