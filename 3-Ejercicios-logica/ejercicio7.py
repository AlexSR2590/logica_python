"""
Dado dos números, hacer una función que reciba como parámetro 
los dos números y que devuelva la cantidad de números impares entre esos números.
Ejemplo.
contarImpares(1, 25)//Devuelve: 13 números impares
"""
import math

def contarImpares(num_inicio, num_fin):
    contador_impar = 0
    resultado = ""
    if not isinstance(numero1, int) or not isinstance(numero2, int):
        resultado = "Los números deben ser enteros."
    elif num_inicio <= num_fin:
        for numero in range(num_inicio, num_fin +1):
                if numero % 2 != 0:
                    contador_impar += 1
        resultado = f"Total números impares: {contador_impar}"
    elif num_fin <= num_inicio:
        for numero in range(num_fin, num_inicio +1):
                if numero % 2 != 0:
                    contador_impar += 1
        resultado = f"Total números impares: {contador_impar}"
    
    return resultado
    

numero1 = 1
numero2 = 25
print(contarImpares(numero1, numero2))


