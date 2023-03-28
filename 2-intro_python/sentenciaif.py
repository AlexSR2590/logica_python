"""Si la expresión evaluada en la sentencia if 
es verdadera (True), ejecuta el código siguiente, 
de lo contrario si es falsa (False),
no ejecuta el código siguiente.

ejemplo sintaxis:

if condición:
    ejecuta código
"""
"""
# Función int convierte cadena de texto a entero.
# Función input recibimos datos de teclado.
edad = int(input("Escribe tu edad: "))

if edad >= 18: #Evalúa si la edad es mayor o igual a 18
    print("Eres mayor de edad.")#Si es True ejecuta el código
else: #Si la edad es menor a 18, False
    print("Eres menor de edad.") #Se ejecuta este código

"""

"""Sentencía elif, es usada cuando se requiere evaluar
más de una condición.

ejemplo sintaxis 

if primera condición:
    codigo
elif segunda condición:
    codigo
elif tercera condición:
    codigo
else:
    codigo
"""
#Identificar si una fruta es un cítrico.

#Pedimos al usuario que ingrese una fruta
#Se almacena en la variabe fruta
fruta = input("Escribe una fruta: ")

if fruta == "limón": #Se evalua primera condición
    print(f"La fruta {fruta} es un cítrico.")
elif fruta == "mandarina":#Se evalua segunda condicioón
    print(f"La fruta {fruta} es un cítrico.")
elif fruta == "naranja":#Se evalua tercera condición
    print(f"La fruta {fruta} es un cítrico.")
elif fruta == "lima":#Se evalua cuarta condición
    print(f"La fruta {fruta} es un cítrico.")
else:#si no se cumple ningúna condición anterior
    print(f"La fruta {fruta} no es un cítrico.")