"""Un operador relacional sirve para comparar y establecer relaciones entre valores"""
numero1 = 100
numero2 = 75
# El operador > devuelve True si el valor de la izquierda es mayor que el de la derecha, de lo contrario regresa False
mayor_que = numero1 > numero2
print(f"{numero1} > {numero2} : {mayor_que} contrario {numero2} > {numero1} : {numero2 > numero1}")

#El operador < devuelve True si el valor de la izquierda es menor que el de la derecha, de lo contrario regresa False
menor_que = numero2 < numero1
print(f"{numero2} < {numero1} : {menor_que} contrario {numero1} < {numero2} : {numero1 < numero2}")

# El operador == devuelve True si ambos valores son iguales
#Igualamos ambas variables 
numero1 = 45
numero2 = 45
iguales = numero1 == numero2
print(f"{numero1} == {numero2} : {iguales} contrario {45} == {46} : {45 == 46}")

# El operador >= devuelve True si el operador de la izquierda es mayor o igual que el de la derecha
numero1 = 35
numero2 = 21
mayor_igual_que = numero1 >= numero2
print(f"{numero1} >= {numero2} : {mayor_igual_que} contrario {numero2} >= {numero1} : {numero2 >= numero1}")

# El operador <= devuelve True si el operador de la izquierda es menor o igual que el de la derecha
menor_igual_que = numero2 <= numero1
print(f"{numero2} <= {numero1} : {menor_igual_que} contrario {numero1} <= {numero2} : {numero1 <= numero2}")

# El operador != devuelve True si ambos valores son distintos
diferente = numero1 != numero2
print(f"{numero1} != {numero2} : {diferente} contrario {35} != {35} : {35 != 35}")

