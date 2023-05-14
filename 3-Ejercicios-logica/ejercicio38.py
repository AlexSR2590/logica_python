"""
Hacer una función que reciba un número entero y que devuelva una lista con
todos los números al cuadrado del 1 hasta el número dado.
Ejemplo:
nombreFuncion(10)//Devuelve: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
def cuadradosLista(valor):
    resultado = ""
    if type(valor) == int:
        resultado = [numero*numero for numero in range(1, valor + 1)]
    else:
        resultado = "Error, introduce números enteros"
    return resultado

print(cuadradosLista(10))