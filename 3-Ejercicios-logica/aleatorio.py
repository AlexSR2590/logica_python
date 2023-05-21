"""
hacer un programa que genere unos números aleatorios del 1 al 65, 
será para ordenar los ejercicios que tenemos en la lista
guardar los números en una lista sin que se repita el número.
"""
import random
ejercicios = []
contador = 0
for i in range(1, 1500):
    numero = random.randrange(1, 66)
    if numero not in ejercicios:
        ejercicios.append(numero)    
    if len(ejercicios) == 65:
        break
print(ejercicios)
print(len(ejercicios))