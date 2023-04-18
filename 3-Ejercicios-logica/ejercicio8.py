"""
Hacer una función que reciba un número entero y que lo invierta y devuelva el número entero.
Ejemplo.
invertirNumero(152)//Devuelve: 251
"""
def invertirNumero(cifra):
    resultado = ""
    if not isinstance(cifra, int):
        resultado ="Introduce números enteros"
    else:
        numero_invertido = ""
        cifra_texto = str(cifra)
        for numero in cifra_texto[:: -1]:
            numero_invertido += numero
            resultado = int(numero_invertido)
    return resultado


numero = 123456789
print(invertirNumero(numero))
