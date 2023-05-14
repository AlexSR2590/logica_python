"""
Hacer una función que reciba un arreglo de números enteros, devolver una lista con los 
números elevados al cuadrado, eliminando cualquier caracter que no sea un número entero.
Ejemplo:
nombreFuncion([1, 2, 3, "s", 4, "%", 5]")//Devuelve [1, 4, 9, 16, 25]
"""
def elevarCuadradoArreglo(numeros_arreglo):
    arre_cuadrado = [numero*numero for numero in numeros_arreglo if isinstance(numero, int)]
    return arre_cuadrado

numeros = [1, 2, 3, "s", 4, "%", 5]
print(elevarCuadradoArreglo(numeros))