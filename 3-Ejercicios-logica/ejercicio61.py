"""
Crea una función que lea una lista de números enteros y determine 
si todos los números son pares, impares o si hay números de ambos tipos.
Ejemplo:
nombreFuncion([2, 4, 6, 8, 10, 12, 14, 16])//Devuelve: Los números son pares.
nombreFuncion([1, 3, 5, 7, 9, 11, 13, 15])//Devuelve: Los números son impares.
nombreFuncion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])//Devuelve: Los números son pares e impares.
"""
def sonParesImpares(numeros):
    pares = []
    impares = []
    resultado = ""
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    if pares and impares:
        resultado = "Los números son pares e impares."
    elif pares:
        resultado = "Los números son pares."
    elif impares:
        resultado = "Los números son impares." 
    else:
        resultado = "La lista está vacia."
    return resultado

pares = [2, 4, 6, 8, 10, 12, 14, 16]
impares = [1, 3, 5, 7, 9, 11, 13, 15]
ambos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
vacia = []
print(sonParesImpares(pares))
print(sonParesImpares(impares))
print(sonParesImpares(ambos))
print(sonParesImpares(vacia))
