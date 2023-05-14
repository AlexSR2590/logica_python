"""
Hacer una función que reciba un texto y devuelva cuantas letras son consonantes y cuantas letras son vocales. 
Ejemplo:
nombreFuncion("Lógica de programación con python")//Devuelve:
Vocales: 11
Consonantes: 18
"""
def contarLetras(texto):
    texto_minusculas = texto.lower()
    texto_minusculas = ''.join(filter(str.isalnum, texto_minusculas))
    texto_minusculas = ''.join([letra for letra in texto_minusculas if not letra.isdigit()])
    vocales = 0
    consonantes = 0
    for letra in texto_minusculas:
        if letra in "aeiouáéíóú":
            vocales += 1
        else:
            consonantes += 1
    return f"vocales: {vocales}\nConsonantes: {consonantes}"


frase = "Lógica de programación con python"

print(contarLetras(frase))