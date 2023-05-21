"""
Escribe una función que calcule la potencia de un número entero dado elevado a otro número entero dado.
Ejemplo:
nombreFuncion(4, 3)//Devuelve: 64
nombreFuncion(5, 2)//Devuelve: 25
"""
def calculaPotencia(numero, potencia):
    if type(numero) == int and type(potencia)== int:
        resultado = numero ** potencia
    else:
        resultado = "Ingrese números enteros."
    return resultado


numero = 5
potencia = 2
print(calculaPotencia(numero, potencia))