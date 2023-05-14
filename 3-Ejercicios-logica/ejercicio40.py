"""
Dado un arreglo de números, hacer una función que nos devuelva el valor más alto y el valor más bajo.
Ejemplo:
nombreFuncion([5, 4, 9, 25, 16, 22, 1])//Devuelve:
valor más alto: 25
valor más bajo: 1
"""
def mayorMenor(numeros):
    numeros.sort()
    minimo = numeros[0]
    maximo = numeros[-1]
    return f"Valor más alto: {maximo}\nValor más bajo: {minimo}"

numeros = [5, 4, 9, 25, 16, 22, 1]

print(mayorMenor(numeros))
