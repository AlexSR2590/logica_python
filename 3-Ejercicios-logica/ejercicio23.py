"""
Dada una cadena de texto, hacer una función que devuelva en mayúscula la primera letra de cada palabra.
Ejemplo:
nombreFuncion("Me gusta la mermelada de fresa")-->Devuelve: "Me Gusta La Mermelada De Fresa"
"""
def mayusculaPalabra(texto):
    nuevo_texto = texto.title()
    return nuevo_texto

def primeraLetraMayuscula(texto):
    contador = 0
    nuevo_texto = ""
    for letra in texto:
        if texto[contador - 1]== " " or texto.find(letra) == 0 :
            nuevo_texto += letra.upper()
        else:
            nuevo_texto += letra
        contador += 1
    return nuevo_texto

frase = "Me gusta la mermelada de fresa"
frase2 = "la pizza de champiñones es mi favorita"

print(mayusculaPalabra(frase))
print(primeraLetraMayuscula(frase2))