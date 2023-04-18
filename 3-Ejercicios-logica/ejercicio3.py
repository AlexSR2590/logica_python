"""
Hacer una función que reciba dos parámetros, palabra y frase, 
la función debe devolver el número de veces que se repite la palabra en esa frase.
Ejemplo.
buscarPalabra("esto es una frase", "frase") //Devuelve 1, por el número de veces encontrado la palabra "frase"
buscarPalabra("esto es una frase", "sol")// Devuelve 0, no se encontró la palabra "sol" en la frase
"""
def buscarPalabra(frase, palabra):
    frase_lower = frase.lower()
    lista_palabras = frase_lower.split()
    contador_palabras = lista_palabras.count(palabra)
    return contador_palabras

frase = "Me gusta la Mermelada de mango y la mermelada de fresa"
palabra = "mermelada"
print(buscarPalabra(frase, palabra))
