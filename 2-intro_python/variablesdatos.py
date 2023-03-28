"""Una variable se puede entender como un contenedor
 donde se almacena y recupera los datos de un programa,
el valor de una variable puede cambiar durante la ejecución 
de un programa."""

#Creando variables y asignando valor
texto = "Las cadenas de texto van entre comillas"
numero = 33 #Se declara la variable numero con un valor de 33
decimal = 9.5 #Tipo de dato flotante o punto decimal

#Mostrar las variables en pantalla
print(texto)
print(numero)
print(decimal)


print("---------Tipos de datos---------")
"""Tipos de datos en Python"""

nada = None #Tipo de dato None, (vacio/ sin contenido).
cadena = "Texto" #Cadena de caracteres o texto
entero = 28 #Número entero
flotante = 12.8 # Número flotante o punto decimal 
boleano = True # Solo puede tener dos valores, True o False 
boleano2 = False # Variable boleano con valor False
lista = [10, 20, 30, 40, 50, 60, 100] # Una lista de números
listaStrings = ["Lista", "de", "texto", 25] #La lista puede contener diferentes tipos de datos
tupla = ("Una", "tupla", "no", "cambia", "su", "valor")
diccionario = {
    "nombre": "Alexis",
    "apellido": "Solís",
    "edad": "33 años"
} #Diccionario, estructura de datos que almacena datos como paras de claves

"""Ahora vamos a imprimir las variables que declaramos"""
print(nada)
print(cadena)
print(entero)
print(flotante)
print(boleano)
print(boleano2)
print(lista)
print(listaStrings)
print(tupla)
print(diccionario)

# Imprimimos en pantalla el tipo de dato de cada variable con la función type()
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(boleano))
print(type(boleano2))
print(type(lista))
print(type(listaStrings))
print(type(tupla))
print(type(diccionario))

