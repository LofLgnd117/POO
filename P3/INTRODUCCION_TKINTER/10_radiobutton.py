from tkinter import *


ventana = Tk()
ventana.title("radiokbutton")
ventana.geometry("500x500")
#-------------------------------------------------- Función mostrar --------------------------------------------------

def mostrarestado():
    resultado.config(text="Opción seleccionada: " + opcion.get())



#-------------------------------------------------- radiobutton --------------------------------------------------
opcion = StringVar()
radioBoton  = Radiobutton(ventana, text="Opcion 1", variable=opcion, value="Opcion 1").pack(pady=5)

radioBoton2 = Radiobutton(ventana, text="Opcion 2", variable=opcion, value="Opcion 2").pack(pady=5)

radioBoton3 = Radiobutton(ventana, text="Opcion 3", variable=opcion, value="Opcion 3").pack(pady=5)

radioBoton4 = Radiobutton(ventana, text="Opcion 4", variable=opcion, value="Opcion 4").pack(pady=5)


boton = Button(ventana, text="Selecciona una opcion", command=mostrarestado)
boton.pack(pady=10)
resultado = Label(ventana, text="")
resultado.pack(pady=10)                     
notificaciones = IntVar()

ventana.mainloop()