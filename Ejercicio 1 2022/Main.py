from ClaseEmail import Email
import csv

def test():
    archivo = open('correosTest.csv')
    reader = csv.reader(archivo,delimiter=',')

    for fila in reader:
        print('Test con correo: {}'.format(fila[0]))
        correo = Email()
        correo.crearCuenta(fila[0])
    archivo.close()
    
if __name__ == '__main__':
    #Ejecucion de funcion test
    op = input('Desea ejecutar la funcion test [S/N]: ')
    if(op.lower() == 's'):
        test()
    print('Punto 1')
    #Solicito nombre
    nombre = input('Ingrese nombre: ')

    miCorreo = Email()
    correo = input('Ingrese su correo: ')
    error = miCorreo.crearCuenta(correo)
    while(error):
        correo = input('Ingrese su correo: ')
        error = miCorreo.crearCuenta(correo) 

    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre,miCorreo.retornaEmail()))

    
    print('Modificar contraseña')
    miCorreo.changePass()

    print('Crear cuenta')
    nuevoCorreo = Email()
    nuevoCorreo.crearCuenta('informatica.fcefn@gmail.com')

    print('Comprobar cuenta duplicada')
    archivo = open('correos.csv')
    reader = csv.reader(archivo,delimiter=',')

    dominio = input('Ingrese un dominio: ')
    cont = 0 #contador de dominios
    bandera  = True
    for fila in reader:
        if bandera: #Salto el encabezado del archivo csv
            bandera = False
        else:
            correo = Email()
            correo.crearCuenta(fila[0],fila[1])
            miDominio = correo.getDominio()
            if dominio == miDominio:
                cont += 1
    archivo.close()

    print('Dominio {} esta repetido {} veces'.format(cont,dominio))
    
    

    