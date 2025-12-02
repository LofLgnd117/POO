from tkinter import * 
import os

ventana = Tk()
ventana.title("images_pillow")
ventana.geometry("500x500")

def mensaje(tipo):
    resultado.config(text=f"{tipo}")


ruta_base = os.path.dirname(os.path.abspath(__file__))

ruta_imagen = os.path.join(ruta_base, "image/bufalos.png")

imagen = PhotoImage(file=ruta_imagen)

etiqueta = Label(ventana, text="Somos Bufalos", image=imagen)
etiqueta.image = imagen 
etiqueta.pack()

boton = Button(ventana, image=imagen, command=lambda: mensaje("Hola python"))
boton.image = imagen
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop() 