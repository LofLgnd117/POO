from tkinter import *


ventana = Tk()
ventana.title("checkbutton")
ventana.geometry("500x500")
#-------------------------------------------------- Función mostrar --------------------------------------------------

def mostrarestado():
    opcion = notificaciones.get()
    if opcion == 1:
        resultado.config(text="Notificaciones activadas")
    else:
        resultado.config(text="Notificaciones desactivadas")

boton = Button(ventana, text="Mostrar estado", command=mostrarestado)
boton.pack(pady=10)

resultado = Label(ventana, text="")
resultado.pack(pady=10)
                     
#-------------------------------------------------- Checkbutton --------------------------------------------------
notificaciones = IntVar()
chk_notificaciones = Checkbutton(ventana, text="Activar notificaciones", variable=notificaciones)
chk_notificaciones.pack(pady=20)

ventana.mainloop()