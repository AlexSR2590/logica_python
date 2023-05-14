"""
Hacer una función que reciba un arreglo de objetos tipo usuarios y que devuelva 
un diccionario de los pasatiempos de los usuarios y el número de personas con el mismo pasatiempo.
Ejemeplo:
nombreFuncion()//Devuelve:
{'Leer': 3, 'Bailar': 2, 'Correr': 2, 'cocinar': 1, 'Jugar videojuegos': 2, 'Cocinar': 1, 'Senderismo': 1, 'Cantar': 1}
"""
class Usuario():
    def __init__(self, nombre, pasatiempo):
        self.nombre = nombre
        self.pasatiempo = pasatiempo


def contarPasatiempos(usuarios):
    resultado = {}
    for usuario in usuarios:
        if usuario.pasatiempo in resultado:
            valor_num_persona = resultado[usuario.pasatiempo]
            valor_num_persona += 1
            resultado[usuario.pasatiempo] = valor_num_persona
        else: 
            resultado[usuario.pasatiempo] = 1
    return resultado


user1 = Usuario("Carlos", "Leer")
user2 = Usuario("Alejandro", "Bailar")
user3 = Usuario("Grecia", "Correr")
user4 = Usuario("Arturo", "cocinar")
user5 = Usuario("Erika", "Jugar videojuegos")
user6 = Usuario("Diana", "Leer")
user7 = Usuario("Karen", "Leer")
user8 = Usuario("Victor", "Cocinar")
user9 = Usuario("Miriam", "Jugar videojuegos")
user10 = Usuario("Cesar", "Correr")
user11 = Usuario("Juan", "Bailar")
user12 = Usuario("Tere", "Senderismo")
user13 = Usuario("Laura", "Cantar")

lista_usuarios = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13]

print(contarPasatiempos(lista_usuarios))