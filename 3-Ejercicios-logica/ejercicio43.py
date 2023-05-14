"""
Hacer una función que reciba un arreglo de números enteros y que nos devuelva la media de todos ellos.
Ejemplo:
nombreFuncion([1, 4, 9, 21, 7, 41, 33, 5])//Devuelve:La media es: 15.125
"""

def obtenerMedia(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    media = suma / len(numeros)
    return f"La media es: {media}"


numeros = [1, 4, 9, 21, 7, 41, 33, 5]
print(obtenerMedia(numeros))


