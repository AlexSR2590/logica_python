"""
Hacer una función que reciba un arreglo y que devuelva un arreglo con el primer y último elemento del arreglo original.
Ejemplo:
nombreFuncion([200, 100, 20, 950, 359])//Devuelve: [200, 359]
"""
def arregloPrimeroUltimo(arreglo):
    nuevo_arreglo = []
    nuevo_arreglo.append(arreglo[0])
    nuevo_arreglo.append(arreglo[-1])
    return nuevo_arreglo

numeros= [200, 100, 20, 950, 359]
print(arregloPrimeroUltimo(numeros))