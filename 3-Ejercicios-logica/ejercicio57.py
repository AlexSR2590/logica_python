"""
Crea una función que lea una lista de números enteros y devuelva la suma de los números que son múltiplos de 3 o 5.
Ejemplo:
nombreFuncion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])//Devuelve: 33

"""
def sumaMultiplosTresCinco(numeros):
    resultado = 0
    suma = 0
    for numero in numeros:
        if numero % 3 == 0 or numero % 5 == 0:
            suma += numero
    return suma


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sumaMultiplosTresCinco(numeros))