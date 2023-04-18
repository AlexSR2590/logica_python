"""
Hacer una función que reciba un texto y una búsqueda, si la búsqueda coincide en el texto, 
censurar todas las coincidencias con la palabra ***Censurado***.
Si el texto o la búsqueda están vacíos, mostrar un mensaje “No puedes leer el texto y la búsqueda”

"""

def censurarFrase(texto, busqueda):
    resultado = ""
    if texto  == "" or busqueda == "":
        resultado ="No puedes leer el texto y la búsqueda"
    elif palabra in texto:
        censurar = "***Censurado***"
        resultado = texto.replace(busqueda, censurar )
    return resultado

texto = "El que tiene un porqué para vivir puede soportar casi cualquier cómo"
palabra = "vivir"

print(censurarFrase(texto, palabra))