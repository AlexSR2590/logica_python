"""
Escribe una función que calcule el volumen de una esfera a partir de su radio en cm.
Ejemplo:
nombreFuncion(3)//Devuelve: 113.09
"""
def calculaVolumenEsfera(radio_cm):
    volumen = (4/3) * (3.1416) * (radio_cm ** 3)
    return volumen

radio = 3

print(calculaVolumenEsfera(radio))