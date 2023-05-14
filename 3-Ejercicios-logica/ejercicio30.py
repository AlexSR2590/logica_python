"""
Hacer una función que reciba una lista de números y que devuelva una nueva lista de números 
sin elementos duplicados, si en la lista encuentra algún string, eliminarlo de la lista nueva.
Ejemplo:
nombreFuncion([1, 8, 3, 3, 9, 1, 7, 's', 2, 'k'])//Devuelve: [1, 8, 3, 9, 7, 2]
"""

def limpiarLista(numeros_letras):
    lista_limpia = []
    for contenido in numeros_letras:
        if isinstance(contenido, int) and contenido not in lista_limpia:
            lista_limpia.append(contenido)
    return lista_limpia

lista = [1, 8, 3, 3, 9, 1, 7, 's', 2, 'k']

print(limpiarLista(lista))