"""
Hacer una función que reciba un número y que pinte un triángulo con * 
con el número de filas que recibe la función.
Ejemplo:
nombreFuncion(5)//Devuelve:
         *
        ***
       *****
      *******
     *********
"""
def triangulo(niveles):
    resultado = ""
    punta = "*"
    for i in range(niveles):
        resultado += punta.center(50, " ") + "\n"
        punta += "**"
    return resultado

numero_filas = 5
print(triangulo(numero_filas))