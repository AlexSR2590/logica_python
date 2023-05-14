"""
Hacer una función que reciba un número y devuelva una escalera 
con el número de niveles que recibe la función como parámetro con los caracteres siguientes "[-]". 
Ejemplo:
construirEscalera(4)//Devuleve:
[--]
[--][--]
[--][--][--]
[--][--][--][--]
"""
def dibujarEscalera(niveles):
    escalon = "[--]"
    escalera = ""
    for nivel in range(0, niveles):
        escalera += f"{escalon * (1 + nivel)} \n"
    return escalera

print(dibujarEscalera(4))