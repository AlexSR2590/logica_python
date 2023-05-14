"""
Hacer una función que reciba un objeto Usuario y un segundo parámetro (nombre de la propiedad) 
para comprobar si existe una propiedad en ese objeto.
Ejemplo:
nombreFuncion(usuario, "edad")//Devuelve:
El objeto contiene la propiedad.
El objeto no contiene la propiedad. (En caso que no tenga la propiedad)
"""

class Usuario():
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura


usuario1 = Usuario("Alejandro", 33, "1.70 metros")
usuario2 = Usuario("Diana", 30, "1.69 metros")

def compruebaPropiedad(objeto, propiedad):
    resultado = ""
    if hasattr(objeto, propiedad):
        resultado = f"El objeto contiene la propiedad {propiedad}"
    else:
        resultado = f"El objeto no contiene la propiedad {propiedad}"
    return resultado


nombre_propiedad = "edad"
nombre_propiedad2 = "apellido"

print(compruebaPropiedad(usuario1, nombre_propiedad))
print(compruebaPropiedad(usuario2, nombre_propiedad2))