"""
Dado un número, hacer una función que devuelva una lista 
con todos los números divisores del 1 hasta el número dado.
Ejemplo:
contarDivisores(15)//Devuelve:[1, 3, 5, 15]
"""
def contarDivisores(rango):
    numeros_divisores=[numero for numero in range(1, rango+1) if rango % numero ==0]
    return numeros_divisores


numero = 20
print(contarDivisores(numero))