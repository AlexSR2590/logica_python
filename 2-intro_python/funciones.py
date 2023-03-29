"""
Para declarar una función, se hace uso de la palabra reservada def,
seguida por el nombre de la función, unos paréntesis, dos puntos 
y el bloque de código a ejecutar dentro de la función.

Ejemplo:

def nombreFuncion():
    codigo función
"""
"""
def saludo():#Definimos una función sin parámetros.
    print("Hola desde una función.")#Código dentro de la función

saludo()#Llamada de la función

"""

def multiplica(num1, num2):#Declaramos la función multiplica con dos parámetros
    return num1 * num2 #hacemos la multiplicación y retornamos el valor con la palabra reservada return

#Llamamos a la función multiplica y pasamos por parámetros los valores 8 y 5 para la operación
#guardamos el valor de retorno en la variable resultado
resultado = multiplica(8,5)  
print(resultado)#Imprimimos la variable resultado, debe regresar el valor 40
