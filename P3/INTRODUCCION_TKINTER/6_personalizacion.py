from tkinter import *

ventana = Tk()

ventana.title("Perzonalizar widgets u objetos")
ventana.geometry("500x500")

def cambiarValores():
    etiqueta.config(
        text="POO con Python",
        bg="green",
        fg="red",
        cursor="spider",
    )
def regresarValores():
    etiqueta.config(
        text="Bienvenidos a Tkinter",
        bg="lightblue",
        fg="darkblue",
    )

etiqueta = Label(ventana, text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica", 30, "italic"),
    relief=SOLID,
    border=2
)
etiqueta.pack(pady=25)

boton1 = Button(ventana, text="Haz clic ...", command=cambiarValores)
boton1.config(
    fg="white",
    width=15,
    font=("Arial", 20, "bold"),
    relief=GROOVE,
    border=2,
    activeforeground="yellow",
)
boton1.pack(pady=15)

boton2 = Button(ventana, text="Regresar Valores ...", command=regresarValores)
boton2.config(
    fg="black",
    width=15,
    font=("Arial", 20, "bold"),
    relief=GROOVE,
    border=2,
    activeforeground="red",
)
boton2.pack(pady=15)
ventana.mainloop()