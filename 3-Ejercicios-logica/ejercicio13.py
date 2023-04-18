"""
Crear una función que reciba un arreglo de números y un número, 
la función debe devolver un arreglo dividido en la cantidad de partes por el número proporcionado.
Ejemplo.
dividirArreglo([1, 2, 3, 4], 2)//Devolver: [1,2][3,4]
dividirArreglo([1, 2, 3, 4, 5], 2)//Devolver: [1,2][3,4][5]
dividirArreglo([1, 2, 3, 4, 5, 6], 2)//Devolver: [1,2][3,4][5,6]
"""
def dividirArreglo(arreglo, partir):
    arreglo_dividido = [arreglo[i:i + partir] for i in range(0, len(arreglo), partir)]
    return arreglo_dividido

arreglo = [1, 2, 3, 6,  8, 15]
dividir_partes = 2
print(dividirArreglo(arreglo, dividir_partes))