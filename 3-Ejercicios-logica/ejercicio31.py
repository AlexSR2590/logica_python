"""
Dado un número, hacer una función que devuelva el tipo de ángulo que es.
Ejemplo:
nombreFuncion("75")//Devuelve: Introduce valores correctos.
nombreFuncion(79)//Devuelve: 79° Ángulo agudo.
"""

def obtenerTipoAngulo(valor_angulo):
    resultado = ""
    if not isinstance(valor_angulo, int) or valor_angulo > 360 or valor_angulo < 0:
        resultado ="Introduce valores correctos."
    elif valor_angulo >= 0 and valor_angulo < 90:
        resultado =f"{valor_angulo}° Ángulo agudo"
    elif valor_angulo == 90:
        resultado = f"{valor_angulo}° Ángulo recto"
    elif valor_angulo > 90 and valor_angulo < 180:
        resultado = f"{valor_angulo}° Ángulo obtuso"
    elif valor_angulo == 180:
        resultado = f"{valor_angulo}° Ángulo llano"
    elif valor_angulo == 360:
        resultado = f"{valor_angulo}° Ángulo completo"
    elif valor_angulo > 180 and valor_angulo < 360:
        resultado = f"{valor_angulo}° Ángulo cóncavo"
    return resultado

print(obtenerTipoAngulo("391"))
print(obtenerTipoAngulo(75))
print(obtenerTipoAngulo(90))
print(obtenerTipoAngulo(155))
print(obtenerTipoAngulo(180))
print(obtenerTipoAngulo(360))
print(obtenerTipoAngulo(300))





