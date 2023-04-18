"""
Hacer una función que reciba un string y un número, y que devuelva el string, repetido el número de veces.
Ejemplo.
repetirCadena("Hola mundo", 3)//Devuelve: Hola mundoHola mundoHola mundo.
"""
def repetirCadena(texto, repetir):
    frase_repetida = texto * repetir
    return frase_repetida

frase = "Hola mundo"
num_repetir = 3
print(repetirCadena(frase, num_repetir))