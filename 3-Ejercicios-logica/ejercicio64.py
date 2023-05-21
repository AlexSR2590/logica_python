"""
Escribe una función que calcule el índice de masa corporal (IMC) de una persona dada su altura y peso.
Ejemplo:
peso = 68
altura_cm = 1.65
nombreFuncion(peso, altura_cm)//Devuelve: 24.98
"""

def calculaIMC(peso, altura_metros):
    masa_corporal = peso / (altura_metros ** 2)
    return masa_corporal


peso = 68
altura = 1.65
print(calculaIMC(peso, altura))