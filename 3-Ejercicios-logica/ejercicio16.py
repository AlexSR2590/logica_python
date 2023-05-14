"""
Crea una función que reciba una cadena de texto y que devuelva 
un mensaje con el número de vocales que tiene el texto.
Ejemplo:
contarVocales("murcielago")//Devuelve: "Número de vocales: 5"
"""
def contarVocales(texto):
    contador_vocal = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador_vocal += 1
    return f"Número de vocales: {contador_vocal}"



texto = "Me encantan las pizzas y las hamburguesas"
print(contarVocales(texto))