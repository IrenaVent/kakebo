import csv

from . import FICHERO

# class Movimineto no se está usando
class Movimiento():
    def __init__(self, fecha, concepto, es_ingreso, cantidad):
        # debemos validar todos estos valores
        self.fecha = fecha
        self.concepto = concepto
        self.es_ingreso = es_ingreso
        self.cantidad = cantidad

class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer (self):
        self.movimientos = []
        fichero = open(FICHERO, "r")
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            # deberes hacer que genere un instancia de mMovimiento
            self.movimientos.append(linea)
        fichero.close()

    def escribir (self):
        if len(self.movimientos) == 0:
            return # no sigue 
        
        fichero = open(FICHERO, "w")
        nombres_campos = list(self.movimiento[0].keys()) #convertir en lista
        dwriter = csv.DictWriter(fichero, fieldnames = nombres_campos)

        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
        fichero.close()

