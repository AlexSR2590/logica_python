"""
Crea una función que lea una lista de números enteros y devuelva la suma de los números pares.
Ejemplo:
nombreFuncion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])//Devuelve: 42
"""
def sumarPares(numeros):
    suma = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma += numero
    return suma

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(sumarPares(lista_numeros))