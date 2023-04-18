"""
Dado dos arreglos, hacer una comparación entre ambos y devolver en un arreglo los elementos en común.
Ejemplo:
elementosIguales([1, 2, 3, 8, 0], [4, 9, 1, 0, 7, 3])//Devuelve un arreglo: ["1","3","0"]
"""


def elementosIguales(arreglo1, arreglo2):
    valores_comun = []
    for valor in arreglo1:
        if valor in arreglo2:
            valores_comun.append(valor)
    return valores_comun


lista1 = [1, 2, 3, 8, 0]
lista2 = [4, 9, 1, 0, 7, 3]

print(elementosIguales(lista1, lista2))