"""
Hacer una función que reciba dos números y que devuelva las operaciones 
básicas entre los dos números (sumar, restar, multiplicar y dividir).
Ejemplo:
nombreFuncion(4,2)//Devuelve:
suma: 4 + 2 = 6
resta: 4 - 2 = 2
multiplicación: 4 x 2 = 8
división: 4 / 2 = 2
"""
def operacionesBasicas(primer_num, segundo_num):
    mensaje = "Error!!, introduce los datos correctos"
    resultado = ""
    if type(primer_num)== str or type(segundo_num)==str:
        resultado = mensaje
    elif (primer_num or primer_num ==0) and segundo_num and segundo_num != 0:
        resultado += f"Suma: {primer_num} + {segundo_num} = {primer_num + segundo_num}\n"
        resultado += f"Resta: {primer_num} - {segundo_num} = {primer_num - segundo_num}\n"
        resultado += f"Multiplicación: {primer_num} x {segundo_num} = {primer_num * segundo_num}\n"
        resultado += f"División: {primer_num} / {segundo_num} = {primer_num / segundo_num}"
    elif primer_num and segundo_num == 0:
        resultado += f"Suma: {primer_num} + {segundo_num} = {primer_num + segundo_num}\n"
        resultado += f"Resta: {primer_num} - {segundo_num} = {primer_num - segundo_num}\n"
        resultado += f"Multiplicación: {primer_num} x {segundo_num} = {primer_num * segundo_num}\n"
        resultado += f"División: {mensaje}"
    return resultado



num1 = 4
num2 = 2

print(operacionesBasicas(num1, num2))

