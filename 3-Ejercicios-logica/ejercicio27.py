"""
Dado un número, hacer una función que muestre su equivalencia en años, meses y días.
Ejemplo:
nombreFuncion(560)//Devuelve:
Años: 1
Meses: 6
Días: 15
"""
import math

def calculaDiaMesAnio(dias):
    resultado = ""
    dias_anio = 365
    mes = 30
    anios = dias / dias_anio
    resto_year = dias % dias_anio
    anios_redondeado = math.floor(anios)
    meses = resto_year / mes
    dias = resto_year % 30
    meses_redondeado = math.floor(meses)
    resultado = f"Años: {anios_redondeado}\nMeses: {meses_redondeado}\nDías: {dias}"
    return resultado


dias_total = 560
print(calculaDiaMesAnio(dias_total))
