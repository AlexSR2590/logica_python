"""
De una cadena de texto, invertir el orden de sus caracteres, 
sin usar métodos propios del lenguaje, únicamente estructuras de control.
Ejemplo:
invertirTexto("soy un texto")//Devuelve: otxet nu yos
"""

def invertirTexto(texto):
    texto_invertido = ""
    for caracter in texto[:: -1]:
        texto_invertido += caracter
    return texto_invertido

#texto = "Invertir el texto"
texto = "Alexis Arturo Solis Rodriguez"

print(invertirTexto(texto))