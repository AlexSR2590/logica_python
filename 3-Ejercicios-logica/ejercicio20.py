"""
Dada dos cadenas de texto, hacer una función que compruebe si son anagramas, 
devuelve True si es anagrama y False si no es un anagrama. 
Un anagrama es cuando las cadenas de texto usan los mismos caracteres en la misma cantidad.
Ejemplo:
comprobarAnagrama("riesgo", "riegos")//Devuelve: True
comprobarAnagrama("riesgos", "riegos")//Devuelve: False
"""
def limpiarString(texto):
    texto = ''.join(filter(str.isalnum, texto))#Elimina caracteres especiales
    texto = ''.join([caracter for caracter in texto if not caracter.isdigit()])#Elimina números
    return list(texto)

def comprobarAnagrama(texto1, texto2):
    texto1_minusculas = texto1.lower()
    texto2_minusculas = texto2.lower()
    texto1_minusculas = limpiarString(texto1_minusculas)
    texto2_minusculas = limpiarString(texto2_minusculas)
    texto1_minusculas.sort()
    texto2_minusculas.sort()
    if texto1_minusculas == texto2_minusculas:
        return True
    else:
        return False    

frase1 = "riegos"
frase2 = "riesgo"

print(comprobarAnagrama(frase1, frase2))



