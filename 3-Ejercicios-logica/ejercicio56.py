"""
Crea una función que calcule el área y el perímetro de un círculo a partir de su radio.
Ejemplo:
nombreFuncion(25)//Devuelve: {'Area': 1963.5, 'Perimetro': 157.08}
"""
def calculaAreaPerimetro(radio):
    area = 0
    perimetro = 0
    resultado = {'Area': 0, 'Perimetro': 0}
    area = 3.1416 * (radio ** 2)
    perimetro = (2 * 3.1416) * radio
    resultado['Area'] = area
    resultado['Perimetro'] = perimetro
    return resultado

radio = 25

print(calculaAreaPerimetro(radio))