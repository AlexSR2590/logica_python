"""
Hacer una función que reciba una palabra y nos devuelva si es un palíndromo, 
la función no debe tener en cuenta espacios en blancos ni símbolos o números.

Ejemplo
palindromo("bob") // Es palíndromo
palindromo("Hola")// No es palíndromo
"""
def limpiarString(frase):
    frase = ''.join(filter(str.isalnum, frase))#Elimina caracteres especiales
    frase = ''.join([caracter for caracter in frase if not caracter.isdigit()])#Elimina números
    return list(frase)

def palindromo(frase):
    resultado = ""
    frase_limpia = limpiarString(frase)
    frase_invertida = list(reversed(frase_limpia))
    if frase_limpia == frase_invertida:
        resultado = "Es un palíndromo"
    else:
        resultado = "No es un palíndromo"
    return resultado

#frase = "%#/$(anita .184lava la tina456884"
frase = "25#&b58#&/ob454%&/"
print(palindromo(frase))


    