"""
hacer una función que reciba un número y que devuelva el número de los bucles 
que contiene la cifra, ejemplo: 9 = un bucle, 6 = un bucle, 8 = dos bucles.
Ejemplo: 
nombreFuncion(1968)//Devuelve: 4
nombreFuncion(1235)//Devuelve: 0 
"""

def contarBuclesCifra(cifra):
    cifra = str(cifra)
    contador_bucles = 0
    for numero in cifra:
        if numero =="0" or numero == "4" or numero == "6" or numero == "9":
            contador_bucles += 1
        elif numero == "8":
            contador_bucles += 2
    return contador_bucles

numero1 = 1968
numero2 = 1235
print(contarBuclesCifra(numero1)) 
print(contarBuclesCifra(numero2))


