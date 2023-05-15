"""
Crea una función que lea una lista de nombres y devuelva
una lista con los nombres que comienzan con una letra específica.
Ejemplo:
nombreFuncion(["Andrea", "Carlos", "Alexis"])//Devuelve:
["Andrea", "Alexis"]
"""
def buscarNombresLetra(nombres, letra):
    letra = letra.upper()
    nombres_econtrados = []
    for nombre in nombres:
        if nombre[0].upper() == letra:
            nombres_econtrados.append(nombre)
    return nombres_econtrados

nombres = ["Andrea", "Carlos", "Alexis", "Alejandro", "Laura", "Erick", "Victor", "Manuel", "Anaid", "Grecia"]
print(buscarNombresLetra(nombres, "A"))