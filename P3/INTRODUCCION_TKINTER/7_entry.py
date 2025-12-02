from tkinter import *

def cambiar():

    lbl_resultado.config(text=f"Entraste al sistema {txt_nombre.get()}")

ventana = Tk()
ventana.title("Entrada de sistema")
ventana.geometry("1280x720")
#------------------------------------------------------------------------- Nombre y contraseña -------------------------------------------------------------------------
lbl_nombre = Label(ventana, text="Ingresa tu nombre: ")
lbl_nombre.pack(pady=20)

nombre = StringVar()
txt_nombre = Entry(ventana, textvariable=nombre)
txt_nombre.pack(pady=10)

lbl_contrasena = Label(ventana, text="Ingresa tu contraseña: ")
lbl_contrasena.pack(pady=20)

contrasena = StringVar()
txt_contrasena = Entry(ventana, textvariable=contrasena, show="*")
txt_contrasena.pack(pady=10)

#------------------------------------------------------------------------- Entrada al sistema -------------------------------------------------------------------------
btn_entrar = Button(ventana, text="Entrar al sistema", command=cambiar)
btn_entrar.pack(pady=20)
lbl_resultado = Label(ventana, text="")
lbl_resultado.pack(pady=10)

ventana.mainloop()