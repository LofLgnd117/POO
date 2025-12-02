from controller import funciones
from tkinter import *

#Interfaz o View

def interfaz():
    ventana=Tk()
    ventana.title("...Calculadora Básica...")
    ventana.geometry("600x400")
    ventana.resizable(False,False)

    n1=DoubleVar()
    n2=DoubleVar()
    txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
    txt_numero1.pack(pady=5)

    txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
    txt_numero2.pack(pady=5)

    btn_suma=Button(ventana,text="+",command=lambda: funciones.operaciones("suma",n1.get(),n2.get()))
    btn_suma.pack()

    btn_resta=Button(ventana,text="-",command=lambda: funciones.operaciones("resta",n1.get(),n2.get()))
    btn_resta.pack()

    btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.operaciones("multiplicacion",n1.get(),n2.get()))
    btn_multiplicacion.pack()
    
    btn_division=Button(ventana,text="/",command=lambda: funciones.operaciones("division",n1.get(),n2.get()))
    btn_division.pack()

    btn_salir=Button(ventana,text="Salir",command=ventana.quit)
    btn_salir.pack(pady=10)

    ventana.mainloop()