"""
Dada una cadena de texto y un número a una función, 
devolver una cadena mostrando los primeros números de caracteres que indica el número.
Ejemplo:
recortarTexto("Hola mundo desde Python", 7)//Devuelve: "Hola mu" 
"""
def recortarTexto(texto, cortar_letras):
    if isinstance(texto, str) and isinstance(cortar_letras, int):
        texto_cortado = texto[:cortar_letras]
    else:
        texto_cortado = "Introduce los datos correctos"
    return texto_cortado
texto = "Hola mundo desde Python"
cortar = 7

print(recortarTexto(texto, cortar))