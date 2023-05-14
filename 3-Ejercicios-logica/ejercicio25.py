"""
Hacer una función que reciba una cadena de texto y que lo convierta en mayúsculas si la mayoría 
de los caracteres son mayúsculas o en minúsculas si la mayoría de los caracteres son minúsculas.
Ejemplo:
nombreFuncion("TexTo EN maYúSCuLAS")//Devuelve: TEXTO EN MAYÚSCULAS.
nombreFuncion("Texto En miNúsculas")//Devuelve: texto en minúsculas.
"""
def mayusculasMinusculas(texto):
    contar_mayusculas = 0
    contar_minusculas = 0
    for letra in texto:
        if letra.isupper():
            contar_mayusculas += 1
        elif letra.islower():
            contar_minusculas += 1
    if contar_mayusculas >= contar_minusculas:
        texto = texto.upper()
    else:
        texto = texto.lower()
    return texto

texto = "texto en miNÚSCULAS"
print(mayusculasMinusculas(texto))