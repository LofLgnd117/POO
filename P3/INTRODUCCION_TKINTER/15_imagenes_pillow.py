from tkinter import * 
import os

ventana = Tk()
ventana.title("images_pillow")
ventana.geometry("500x500")

def mensaje(tipo):
    resultado.config(text=f"{tipo}")


# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "image/bufalos.png")

#1ra de agregar imagenes con la libreria de Tkinter ya ncluidas
#PhotoImages solo permite archivos con extension .png, .gif y .pgm/ .ppm
imagen = PhotoImage(file=ruta_imagen)

#Incluir o mostrar la imagen, dentro de un label y el boton
etiqueta = Label(ventana, text="Somos Bufalos", image=imagen)
etiqueta.image = imagen  # mantener referencia
etiqueta.pack()

boton = Button(ventana, image=imagen, command=lambda: mensaje("Hola python"))
boton.image = imagen  # mantener referencia
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()