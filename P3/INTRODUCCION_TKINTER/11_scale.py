from tkinter import *

ventana = Tk()
ventana.title("scale")
ventana.geometry("500x500")
#-------------------------------------------------- Función mostrar --------------------------------------------------

def mostrarestado():
    resultado.config(text=f"Opción seleccionada: {valor.get()}")

#-------------------------------------------------- scale --------------------------------------------------
valor = IntVar()
escala = Scale(ventana, from_=0, to=100, orient=HORIZONTAL, variable=valor)
escala.pack(pady=20)

boton = Button(ventana, text="Mostrar valor", command=mostrarestado)
boton.pack(pady=10)

resultado = Label(ventana, text="")
resultado.pack(pady=10)

ventana.mainloop()