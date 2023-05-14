"""
Hacer una función que reciba un string y que devuelva un lista con una sublista 
de todos los caracteres que aparecen una vez en el string , y el segundo elemento 
con la letra que comienza el string. 
Ejemeplo:
nombreFuncion("hola mundo hola")//Devuelve: [['m', 'u', 'n', 'd'], 'm']
"""
def sinRepetirLetras(frase):
    sin_espacio = frase.replace(" ","")
    iterar_letras = list(sin_espacio)
    primera_letra = 0
    letras_sin_repetir = []
    resultado = []
    for letra in sin_espacio:
        if iterar_letras.count(letra) < 2 and primera_letra == 0:
            letras_sin_repetir.append(letra)
            primera_letra = letra
        elif iterar_letras.count(letra) < 2:
            letras_sin_repetir.append(letra)
    resultado.append(letras_sin_repetir)
    resultado.append(primera_letra)
    return resultado

texto = "hola mundo hola"
print(sinRepetirLetras(texto))