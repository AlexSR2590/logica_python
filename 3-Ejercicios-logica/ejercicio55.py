"""
Crea una función que lea una lista de números y elimine los números duplicados.
Ejemplo:
nombreFuncion([1, 2, 3, 1, 5, 9, 2, 8, 10, 4, 3])//Devuelve: [1, 5, 9, 2, 8, 10, 4, 3]

"""

def eliminaNumerosDuplicados(numeros):
    copia_lista = numeros
    for i in copia_lista:
        for j in numeros:
            if numeros.count(i) > 1:
                numeros.pop(i)
    return numeros


numeros = [1, 2, 3, 1, 5, 9, 2, 8, 10, 4, 3]
print(eliminaNumerosDuplicados(numeros))