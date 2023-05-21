"""
Crea una función que lea una lista de números enteros y devuelva la lista ordenada de forma descendente.
Ejemplo:
nombreFuncion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])//Devuelve: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""
def ordenarDescendente(numeros):
    numeros.sort(reverse = True)
    return numeros

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(ordenarDescendente(numeros))