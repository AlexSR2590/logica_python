"""
Hacer una función que reciba un número y que nos indique si es un número capicúa o no. 
El número capicúa se lee igual de derecha a izquierda y viceversa.
Ejemplo:
nombreFuncion(3003)//Devuelve: Es capicúa
nombreFuncion(2023)//Devuelve: No es capicúa
"""
def verificaCapicua(numero):
    resultado = ""
    numero_invertido = ""
    cadena_numero  = str(numero)
    for contador in cadena_numero[::-1]:
        numero_invertido += contador  
    es_capicua = int(numero_invertido)
    if es_capicua == numero:
        resultado = "Es capicúa."
    else:
        resultado = "No es capicúa."
    return resultado

numero = 2002
numero2 = 2023
print(verificaCapicua(numero))
print(verificaCapicua(numero2))