"""
Hacer una función que reciba un arreglo de números enteros y separe los números pares e impares 
en arreglos diferente y devolver un arreglo de los números pares e impares separados.
Ejemplo:
nombreFuncion([1, 2, 3, 4, 5, 6, 7])//Devuelve:[[2, 4, 6], [1, 3, 5, 7]]

"""
def separaParesImpares(numeros):
    pares = []
    impares = []
    resultado = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    resultado.append(pares)
    resultado.append(impares)
    return resultado

lista_numeros = [1, 2, 3, 4, 5, 6, 7]


print(separaParesImpares(lista_numeros))
