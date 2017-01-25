'''
Created on 24 ene. 2017

@author: luciod
'''

from datetime import datetime

import unittest
from __builtin__ import str
from _ast import Str

class Prueba(unittest.TestCase):
    def test_calcularPrecio(self):
        tarifa = 1.0
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("1 Jan 2017 14:00", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), 1.0)
        tarifa = 0
        self.assertEqual(calcularPrecio(tarifa, t), None)
        tarifa = 10.0
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("8 Jan 2017 14:00", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), None)
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("1 Jan 2017 13:15", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), 10.0)
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("2 Jan 2017 13:15", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), tarifa*25)

def calcularPrecio(tarifa, tiempoDeServicio):
    """Funcion para calcular el precio a pagar segun una tarifa y un tiempo de servicio, retorna none si hay un error"""
    if (not(type(tarifa) is float and tarifa > 0)):
        return None
    if (not(type(tiempoDeServicio[0]) is datetime and type(tiempoDeServicio[1]) is datetime)):
        return None
    deltaTiempo = tiempoDeServicio[1] - tiempoDeServicio[0]
    minutos = deltaTiempo.total_seconds()/60
    if (not minutos >= 15):
        return None
    horas = minutos//60
    minutos = minutos - horas*60
    if(minutos > 0):
        horas = horas + 1
    if (not horas < 7*24):
        return None
    return tarifa * horas

# if __name__ == '__main__':
#     tarifa = 10.0
#     inicio = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
#     fin = datetime.strptime("1 Jan 2017 14:15", "%d %b %Y %H:%M")
#     tiempo = [inicio, fin]
#     total = calcularPrecio(tarifa, tiempo)
#     print("Total: " + repr(total))

unittest.main()









