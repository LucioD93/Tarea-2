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
        

def calcularPrecio(tarifa, tiempoDeServicio):
    """Funcion para calcular el precio a pagar segun una tarifa y un tiempo de servicio, retorna none si hay un error"""
    if (not(type(tarifa) is float and tarifa > 0)):
        return None
    if (not(type(tiempoDeServicio[0]) is datetime and type(tiempoDeServicio[1]) is datetime)):
        return None
    deltaTiempo = tiempoDeServicio[1] - tiempoDeServicio[0]
    minutos = deltaTiempo.total_seconds()/60
    if (not minutos > 15):
        return None
    if (not minutos/60 < 7*24):
        return None
    return tarifa * (minutos/60)

# if __name__ == '__main__':
#     tarifa = 1
#     inicio = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
#     fin = datetime.strptime("1 Jan 2017 14:00", "%d %b %Y %H:%M")
#     tiempo = [inicio, fin]
#     total = calcularPrecio(tarifa, tiempo)
#     print("Total: " + repr(total))

unittest.main()









