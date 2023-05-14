"""
Dado un arreglo o un texto, hacer una función que devuelva el elemento más repetido. 
Ejemplo:
nombreFuncion("Hola mundo, Hola ")//Devuelve: hola
nombreFuncion([1, 5, 4, 1, 3, 9])//Devuelve: 1
"""
import string

def valorRepetido(datos_arreglo):
    resultado = ""
    if type(datos_arreglo) == str:
        texto_minus = datos_arreglo.lower()
        texto_minus = ''.join(letra for letra in texto_minus if letra not in string.punctuation)#Elimina signos puntuación
        texto_lista = texto_minus.split(' ')
        palabras_repetidas = dict((palabra, texto_lista.count(palabra))for palabra in texto_lista)
        palabra_mas_usada = max(palabras_repetidas, key=palabras_repetidas.get)
        resultado = palabra_mas_usada
    else:
        numeros_repetidos = dict((numero, datos_arreglo.count(numero))for numero in datos_arreglo)
        numero_mas_usado = max(numeros_repetidos, key=numeros_repetidos.get)
        resultado = numero_mas_usado
    return resultado


numeros = [1, 5, 4, 1, 3, 9]
texto = "Hola mundo, hola"
print(valorRepetido(texto))
print(valorRepetido(numeros))

