"""
Hacer una función que reciba dos números y devuelva un mensaje mostrando el numero mayor y el número menor y
mostrar un mensaje si ambos números son iguales.  
Ejemplo:
menorMayor(9, 4)//Devuelve:
El número mayor es: 9
El número menor es: 4
menorMayor(7, 7)
Los números 7 son iguales. 
"""
def menorMayor(num_mayor, num_menor):
    mensaje = ""
    if num_mayor > num_menor:
        mensaje = f"El número mayor es: {num_mayor}\nEl número menor es: {num_menor}"
    elif num_mayor < num_menor:
        mensaje = f"El número mayor es: {num_menor}\nEl número menor es: {num_mayor}"
    elif num_mayor == num_menor:
        mensaje = f"Los números {num_mayor} son iguales."
    return mensaje

print(menorMayor(9,4))
print(menorMayor(7,7))