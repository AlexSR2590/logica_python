"""
Hacer una función que reciba el número y devuelva su tabla de multiplicar del 1 al 10
Ejemplo: 
funcionTabla(8) La función recibe como parámetro el número 8 y devolver la tabala de multiplocar del 8
------ Tabla del 8 ------
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72
8 X 10 = 80
"""
def tablaMultiplicar(numero): #Definición de función y recibe el número como parámetro
    resultado = f"------ Tabla de multiplicar del {numero} ------\n" #Encabezado
    for multiplicador in range(1, 11): #Bucle del 1 al 10
        resultado += f"{numero} X {multiplicador} = {numero * multiplicador}\n"
    return resultado

print(tablaMultiplicar(8))