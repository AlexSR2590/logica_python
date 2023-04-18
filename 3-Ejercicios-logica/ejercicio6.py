"""
Dibujar un cuadrado hueco con asteriscos (*)
el número de * por lado lo debe de recibir la función como parámetro.
Ejemplo.
cuadrado(5)//Devuleve.
*****
*   *
*   *
*   *
*****
"""
def cuadrado(numero):
    for lado_sup in range(numero):
        print("* ", end="")
    print()

    for izquierdo in range(numero - 2):
        print("* ", end="")
        for espacio in range(numero - 2):
            print("  ", end="")
        print("*")
    for lado_inf in range(numero):
        print("* ", end="")

numero = 5
cuadrado(numero)