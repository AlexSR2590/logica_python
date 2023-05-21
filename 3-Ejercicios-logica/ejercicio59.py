"""
Crea una función que lea una lista de números enteros y determine si la lista 
está ordenada de forma ascendente, descendente o si no está ordenada.
Ejemeplo:
nombreFuncion([1, 2, 3, 4])//Devuelve: Lista ordenada ascendente.
nombreFuncion([4, 3, 2, 1])//Devuelve: Lista ordenada descendente.
nombreFuncion([1, 4, 3, 2])//Devuelve: Lista no ordenada.
"""

def descendenteAscendente(numeros):
    ascendente = numeros.copy()
    ascendente.sort()
    descendente = numeros.copy()
    descendente.sort(reverse=True)
    resultado = ""
    if numeros == ascendente:
        resultado = "Lista ordenada ascendente"
    elif numeros == descendente:
        resultado = "Lista ordenada descendente"
    else:
        resultado = "Lista no ordenada"
    return resultado

descendente = [4, 3, 2, 1]
ascendente = [1, 2, 3, 4]
sin_orden = [1, 4, 3, 2]

print(descendenteAscendente(descendente))
print(descendenteAscendente(ascendente))
print(descendenteAscendente(sin_orden))
