'''
Created on 24 ene. 2017

@author: luciod
'''

from datetime import datetime
import unittest

class Prueba(unittest.TestCase):
    def test_calcularPrecio1Hora(self):
        tarifa = 1.0
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("1 Jan 2017 14:00", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), 1.0)
        
    def test_calcularPrecioTarifaInvalida(self):
        tarifa = 0
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("1 Jan 2017 14:00", "%d %b %Y %H:%M")
        t = [t1, t2]
        with self.assertRaises(Exception):
            calcularPrecio(tarifa, t)
        
    def test_calcularPrecioTiempoMuyLargo(self):
        tarifa = 10.0
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("8 Jan 2017 14:00", "%d %b %Y %H:%M")
        t = [t1, t2]
        with self.assertRaises(Exception):
            calcularPrecio(tarifa, t)
    
    def test_calcularPrecioValido(self):
        tarifa  = 15.0
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("1 Jan 2017 13:15", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), tarifa*1)
        t1 = datetime.strptime("1 Jan 2017 13:00", "%d %b %Y %H:%M")
        t2 = datetime.strptime("2 Jan 2017 13:15", "%d %b %Y %H:%M")
        t = [t1, t2]
        self.assertEqual(calcularPrecio(tarifa, t), tarifa*25)

def calcularPrecio(tarifa, tiempoDeServicio):
    """Funcion para calcular el precio a pagar segun una tarifa y un tiempo de servicio, retorna none si hay un error"""
    if (not(type(tarifa) is float and tarifa > 0)):
        raise Exception('Tarifa Invalida')
    if (not(type(tiempoDeServicio[0]) is datetime and type(tiempoDeServicio[1]) is datetime)):
        raise Exception
    deltaTiempo = tiempoDeServicio[1] - tiempoDeServicio[0]
    minutos = deltaTiempo.total_seconds()/60
    if (not minutos >= 15):
        raise Exception
    horas = minutos//60
    minutos = minutos - horas*60
    if(minutos > 0):
        horas = horas + 1
    if (not horas < 7*24):
        raise Exception
    return tarifa * horas

unittest.main()









