"""
Hacer una función que devuelva el Fibonacci de un número, y mostrar la sucesión de Fibonacci del 1 al 10.
La sucesión de Fibonacci se compone de la suma de los dos números anteriores.
Serie de números:|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |

                    0     1    0+1   1+1   1+2   2+3   3+5   5+8  8+13  13+21 21+34
Fibonacci:       |  0  |  1  |  1  |  2  |  3  |  5  |  8  |  13 |  21 |  34 |  55 |
"""
def fibonacci(numero):
    if numero < 2:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci( numero - 2)
    
numero = 10
for i in range(numero + 1):
    print(fibonacci(i))
