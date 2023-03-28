"""Vamos a crear unas variables y concatenar esas variables 
y mostrarlas en pantalla en una sola línea """
nombre = "Alexis"
pais = "México"

"""
La función str() cambia el tipo de dato de una variable a un string o cadena de texto (str) 
y almacena el resultado en otra variable, en este caso de un int a str, 33 a "33" y se guardará en la variable
edad_texto.
"""
edad = 33
#Cambiamos el tipo de dato de la variable edad y se guarda el resultado en la variable edad_texto
edad_texto= str(edad)

#Dando formato escribiendo la letra f antes de las dobles comillas y las variables van dento de Paréntesis{}
print (f"Mi nombre es {nombre} vivo en {pais} y tengo {edad_texto} años") 
print (8 ** 3)