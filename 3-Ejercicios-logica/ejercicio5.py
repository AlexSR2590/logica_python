"""
Hacer una función que reciba dos números y que devuelva un mensaje, el x porciento de x número es : x.
Ejemplo:
25% de 350
porcentaje(25,350)//Devuelve: "El 25% de 350 es : 87.5
"""
def porcentaje(porcentaje, cantidad):
    resultado = ""
    if porcentaje <= 0 or cantidad <= 0:
        resultado = "Los números deben ser positivos."
    else: 
        resultado = f"El {porcentaje}% de {cantidad} es : {(porcentaje / 100) * cantidad}"
    return resultado

porciento = 25
cantidad = 350
print(porcentaje(porciento, cantidad))
