'''
Created on 24 ene. 2017

@author: luciod
'''

from datetime import datetime

def calcularPrecio(tarifa, tiempoDeServicio):
    print("Tarifa: ", tarifa)
    print(tiempoDeServicio[0])
    print(tiempoDeServicio[1])
    deltaTiempo = tiempoDeServicio[1] - tiempoDeServicio[0]
    print(deltaTiempo.total_seconds()/3600)
    
if __name__ == '__main__':
    tarifa = 1
    inicio = datetime.now()
    assert type(inicio) is datetime, "inicio no es una fecha"
    fin = datetime.strptime("24 Jan 2017 06:30", "%d %b %Y %H:%M")
    tiempo = [inicio, fin]
    calcularPrecio(tarifa, tiempo)