"""
Dada una cadena de texto, devolver el caracter más usado.
Ejemplo:
nombreFuncion("hola mundo desde python")//Devuelve: ['o', 'd']
"""
def contarLetrasRepetidas(texto):
    texto = texto.lower()
    texto = texto.replace(" ","")
    list(texto)
    letras = {letra: texto.count(letra) for letra in texto}
    letras_repetidas = [llave for llave, valor in letras.items() if valor == max(letras.values())]
    return f"Letra o letras más repetidas: {letras_repetidas}"


frase = "hola mundo desde python"

print(contarLetrasRepetidas(frase))

