"""
Hacer una función que reciba un string y que devuelva las posibles combinaciones de letras en un arreglo sin alterar
el orden de las letras.
Ejemplo:
nombreFuncion("hola")//Devuelve:
['h', 'o', 'l', 'a', 'ho', 'hol', 'hola', 'ol', 'ola', 'la']
"""
def combinaPalabra(palabra):
    combinacion = []
    resultado = []
    combinacion = list(palabra)
    indice_inicio = 0
    for i in range(len(palabra)):
        for j in range(len(palabra)+1):
            if palabra[i] != "":
                combinacion.append(palabra[indice_inicio:j])
        indice_inicio += 1
    for elemento in combinacion:
        if elemento not in resultado and elemento != "":
            resultado.append(elemento)
    return resultado

palabra= "Hola"

print(combinaPalabra(palabra))