"""Bucle for nos permite iterar (recorrer sus elemento uno a uno) n cantidad de veces sobre 
una variable; tupla, listas, diccionarios, conjuntos...

Sintaxis del bucle for

la variable elemento, toma el valo de la variable_iterable cada vez que el bucle
se ejecuta

for <elemento> in <variable_iterable>:
    <codigo dentro de for> 

"""
"Hagamos un ejemplo usando una lista de números y ver el funcionamiento del bucle for"
#numeros = [2, 4, 6, 8, 10] #Declaramos la variable numeros tipo lista con los numeros 2, 4, 6, 8, 10

#for elemento in numeros: #Elemento toma un valor de la variable numeros
#    print(elemento)#Imprimimos el valor de la variable elemento


"""Bucle while es una estructura de control que itera o repite un código 
mientras la condición es verdadera"""

"""Hagamos un ejemplo con el bucle while con un programa que nos imprima del 1 hasta el 20"""

contador = 1 #Declaramos la variable contador con valor de 1, nos ayudará para detener el bucle
while contador <= 20: #Mientras contador es menor o igual (<=) a 20
    print(contador)
    contador += 1
