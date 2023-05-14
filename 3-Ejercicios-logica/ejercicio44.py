"""
Dado un arreglo de strings, regresar un nuevo arreglo con strings que estén formados por más de dos palabras.
Ejemplo:
nombreFuncion()
"""

def dosPalabras(palabras):
    resultado = []
    for palabra in palabras:
        if " " in palabra:
            resultado.append(palabra)
    return resultado

palabras = ["lógica de programación", "python", "hola mundo"]

print(dosPalabras(palabras))