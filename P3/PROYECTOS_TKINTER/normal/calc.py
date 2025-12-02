"""
Crear una calculadora:
1.- Dos campos de texto
2.- Cuatro botones para las Operaciones
3.- Mostrar el resultado en una alerta
"""
from tkinter import messagebox
from tkinter import *

def operaciones(operacion, numero1, numero2):
    if operacion == "suma":
        resultado = numero1 + numero2
        simbolo = "+"
        titulo = "Suma"
    elif operacion == "resta":
        resultado = numero1 - numero2
        simbolo = "-"
        titulo = "Resta"
    elif operacion == "multiplicacion":
        resultado = numero1 * numero2
        simbolo = "x"
        titulo = "Multiplicación"
    elif operacion == "division":
        resultado = numero1 / numero2
        simbolo = "/"
        titulo = "División"
    messagebox.showinfo(icon="info", title=titulo, message=f"{numero1} {simbolo} {numero2} = {resultado}")

# Interfaz o view
ventana = Tk()
ventana.title("...Calculadora Básica...")
ventana.geometry("600x400")
ventana.resizable(False, False)


n1 = IntVar()
n2 = IntVar()

txt_numero1 = Entry(ventana, textvariable=n1, width=10, justify="right")
txt_numero1.pack(pady=5)

txt_numero2 = Entry(ventana, textvariable=n2, width=10, justify="right")
txt_numero2.pack(pady=5)

btn_suma = Button(ventana, text="+", width=6, command=lambda: operaciones("suma", n1.get(), n2.get()))
btn_suma.pack(pady=2)

btn_resta = Button(ventana, text="-", width=6, command=lambda: operaciones("resta", n1.get(), n2.get()))
btn_resta.pack(pady=2)

btn_multiplicacion = Button(ventana, text="x", width=6, command=lambda: operaciones("multiplicacion", n1.get(), n2.get()))
btn_multiplicacion.pack(pady=2)

btn_division = Button(ventana, text="/", width=6, command=lambda: operaciones("division", n1.get(), n2.get()))
btn_division.pack(pady=2)

btn_salir = Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack(pady=10)

ventana.mainloop()