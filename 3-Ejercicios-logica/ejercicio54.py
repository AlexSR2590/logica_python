"""
Crea una función que determine si un número es primo o no, si es primo devuelve True y False en caso contrario. 
Un número es primo si es divisible solo por 1 y por sí mismo.
Ejemplo:
nombreFuncion(7)//Devuelve: True
nombreFuncion(9)//Devuelve: False
"""

def numeroPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(numeroPrimo(7))
print(numeroPrimo(9))