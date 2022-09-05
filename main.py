import csv

from Provincia import Provincia
from ListaEncadenada import ListaEncadenada
from ListaEncadenadaPorContenido import ListaEncadenadaPorContenido

def mostrar_provincia(unaProvincia: Provincia):
    print("{0:<20}{1:>10.2f}".format(unaProvincia.nombre, unaProvincia.superficie))




if __name__ == "__main__":
    unaLista = ListaEncadenada()
    nombreArchivo = "superficie-afectada-por-incendios-forestales.csv"
    archivo = open(nombreArchivo, encoding="cp1252")
    reader = csv.reader(archivo, delimiter=";")
    next(reader)
    for fila in reader:
        if fila[3] != "" and fila[6] != "":
            unaProvincia = Provincia(fila[3], float(fila[6]))
            i = 1
            while i <= unaLista.cantidad() and unaLista.recuperar(i).nombre != unaProvincia.nombre:
                i += 1
            if i > unaLista.cantidad():
                unaLista.insertar(unaProvincia, unaLista.cantidad() + 1)
            else:
                otraProvincia = unaLista.suprimir(i)
                otraProvincia.superficie += unaProvincia.superficie
                unaLista.insertar(otraProvincia, i)
    
    otraLista = ListaEncadenadaPorContenido()
    
    cantidad = unaLista.cantidad()

    for i in range(cantidad):
        otraLista.insertar(unaLista.suprimir(1))
    
    otraLista.recorrer(mostrar_provincia)