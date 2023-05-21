"""
Hacer una función que reciba un arreglo de objetos tipo usuarios y que devuelva 
un diccionario de los pasatiempos de los usuarios y el número de personas con el mismo pasatiempo.
Ejemeplo:
nombreFuncion([user1, user2, user3, user4, user5, user6, user7])//Devuelve:
{'Leer': 3, 'Bailar': 1, 'Correr': 1, 'Cocinar': 2}
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
user4 = Usuario("Arturo", "Cocinar")
user5 = Usuario("Diana", "Leer")
user6 = Usuario("Karen", "Cocinar")
user7 = Usuario("Victor", "Leer")


lista_usuarios = [user1, user2, user3, user4, user5, user6, user7]

print(contarPasatiempos(lista_usuarios))