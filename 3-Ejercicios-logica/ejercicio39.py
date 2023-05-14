"""
Hacer una función que valide si un correo electrónico está escrito correctamente o no.
Ejemplo:
nombreFuncion("alex@gmail.com")//Devuelve: True
nombreFunciin("@ale@,com")//Devuelve: False
"""
import re

def validarCorreo(correo):
    resultado = ""
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):
        resultado = True
    else:
        resultado = False
    return resultado

correo = "alex@hotmail.com"
correo_invalido = "@lex@gmail,com"

print(validarCorreo(correo))
print(validarCorreo(correo_invalido))