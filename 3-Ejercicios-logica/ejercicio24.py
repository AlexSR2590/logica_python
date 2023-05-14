"""
Hacer una función que reciba un arreglo de enteros y un número, 
la función tendrá que devolver True si el arreglo es una permutación 
del 1 al número recibido en la función o False en caso contrario.
Una permutación es una secuencia de números ordenada sin que falte o duplique un número.
Ejemplo:
nombreFuncion([1, 2, 3, 4, 5, 6, 7], 7)--->Devuelve: True
nombreFuncion([1, 2, 3, 4, 5, 7], 7)--->Devuelve: False
"""
def revisarPermutacion(secuencia, numero_fin):
    resultado = ""
    contador = 0
    if len(secuencia) == numero_fin:
        for numero in secuencia:
            contador += 1
            if numero == contador:
                resultado = True
            else:
                resultado = False
                break
    else:
        resultado = False
    return resultado

numeros = [1, 2, 3, 4, 5, 6, 7]
numero_fin = 7
print(revisarPermutacion(numeros, numero_fin))
