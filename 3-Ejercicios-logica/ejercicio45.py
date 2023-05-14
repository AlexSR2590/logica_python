"""
Hacer una función que reciba un arreglo de alumnos con nombre y nota, 
y que devuelva la cantidad de alumnos aprobados y la cantidad de alumnos reprobados. 
Considerando la calificación 6 aprobatoria.
Ejemplo:
nombreFuncion([["Carlos", 8], ["Laura", 9], ["Alex", 8], ["Erick", 7], ["Juan",5], ["Arely", 4]])//Devuelve:
Alumnos aprobados: 4
Alumnos reprobados: 2
"""

def aprobadosReprobados(notas_alumnos):
    aprobados = 0
    reprobados = 0
    for alumno in notas_alumnos:
        if alumno[1] >= 6:
            aprobados +=1
        else:
            reprobados += 1
    return f"Alumnos aprobados: {aprobados}\nAlumnos reprobados: {reprobados}"

notas_alumnos = [["Carlos", 8], ["Laura", 9], ["Alex", 8], ["Erick", 7], ["Juan",5], ["Arely", 4]]


print(aprobadosReprobados(notas_alumnos))