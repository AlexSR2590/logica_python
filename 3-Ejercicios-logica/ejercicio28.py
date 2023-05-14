"""
Dado un número, hacer una función que devuelva el factorial.
El factorial de un número es el resultado de la multiplicación 
de todos los números anteriores hasta llegar al número que se quiere conocer su factorial.
factorial 4 = 1 x 2 x 3 x 4 
Ejemplo:
nombreFuncion(4)//Devuelve: 24
"""
def factorial(numero):
    resultado = 1
    for contador in range(1, numero):
        resultado += resultado * contador
    return resultado 

numero = 4
print(factorial(numero))