"""
Crea una función que lea una cadena de caracteres y determine si es un pangrama, si lo es devuelve True,
en caso contrario devuelve False. 
Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez.
Ejemplo:
nombreFuncion("hola mundo")//Devuelve: False
nombreFuncion("abcdefghijklmnopqrstuvwxyz")//Devuelve: True
"""
import string

def esPangrama(texto):
    texto = texto.lower()
    alfabeto = string.ascii_lowercase
    for letra in alfabeto:
        if letra not in texto:
            return False
        
    return True

no_pangrama = "Hola mundo"
pangrama = "abcdefghijklmnopqrstuvwxyz"
print(esPangrama(no_pangrama))
print(esPangrama(pangrama))
