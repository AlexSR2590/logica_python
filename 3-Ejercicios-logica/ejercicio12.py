"""
Hacer una función que reciba un número y contar del 0 al número recibido con intervalo de 5 en 5, 
mostrando el resultado en una lista con el siguiente formato n°0, n°5, n°10……
Ejemplo.
serieEnCinco(30)//Devuelve: ["n°0", "n°5", "n°10", "n°15", "n°20", "n°25", "n°30"]
"""

def serieEnCinco(rango):
    lista_numeros= []
    contador = 0
    valor = 0
    while valor < rango:
        valor = contador * 5
        lista_numeros.append(str(f"n°{valor}"))
        contador += 1
    return lista_numeros

print(serieEnCinco(30))


