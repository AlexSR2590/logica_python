"""
Escribe una función que genere una lista de números primos en un rango dado.
Ejemeplo:
nombreFuncion(1, 50)//Devuelve: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""
def generarNumerosPrimos(rango_inicio, rango_fin):
    numeros_primos = []
    for numero in range(rango_inicio, rango_fin + 1):
        if esPrimo(numero):
            numeros_primos.append(numero)
    return numeros_primos


def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5)+1):
            if numero % i == 0:
                return False
    return True


inicio = 1
fin = 50
print(generarNumerosPrimos(inicio, fin))