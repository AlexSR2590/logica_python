"""
Hacer una función que reciba dos números y devuelva un número aleatorio entre los dos números.
Ejemplo:
nombreFuncion(1, 30)//Devuelve: 21
"""
import random

def aleatorio(num_inicial, num_final):
    resultado = 0
    if num_inicial <= num_final:
        resultado = random.randint(num_inicial, num_final)
    else:
        resultado = random.randint(num_final, num_inicial)
    return resultado


print(aleatorio(1, 30))
