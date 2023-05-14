"""
Hacer una función que reciba un número y que devuelva una cadena texto 
contando del 1 hasta el número recibido. Sustituyendo los números múltiplos de 3 por la palabra “Hola”, 
los múltiplos de 5 por la palabra “mundo” y por los números múltiplos de 3 y 5 por la frase “¡Hola mundo!”.
Ejemplo:
holaMundo(20)//Devuelve:
1
2
Hola
4
mundo
hola
"""
def serieHolaMundo(rango):
    serie_numeros = ""
    for numero in range(1, rango + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            serie_numeros += "!Hola mundo!\n"
        elif numero % 3 == 0:
            serie_numeros += "Hola\n"
        elif numero % 5 == 0:
            serie_numeros += "mundo\n"
        else:
            serie_numeros += str(numero) + "\n"
    return serie_numeros


numero = 20

print(serieHolaMundo(numero))