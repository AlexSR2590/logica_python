"""
Hacer un reloj digital que muestre la hora actualizada.
"""

import tkinter 
from datetime import datetime

actualizar_reloj_intervalo = 300 #mili segundos


def obtenerHoraActual():
    return datetime.now().strftime("%H:%M:%S")

def actualizarReloj():
    hora_actual.set(obtenerHoraActual())
    ventana.after(actualizar_reloj_intervalo, actualizarReloj)

ventana = tkinter.Tk()
hora_actual = tkinter.StringVar(ventana, value=obtenerHoraActual())
ventana.etiqueta = tkinter.Label(
    ventana, textvariable = hora_actual, font=f"Consolas 60")
ventana.etiqueta.pack(side="top")
app = tkinter.Frame()
ventana.title("Reloj con Python")
actualizarReloj()
app.pack()
app.mainloop()


