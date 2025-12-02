from tkinter import *

def cambiarTexto():
    label_nombre.config(text="Flores Verdin Leonardo Javier")
    label_contrasena.config(text="1234")

ventana = Tk()
ventana.title("Uso de botones, Marcos, Etiquetas")
ventana.geometry("800x600")

frame_principal=Frame(ventana,)
frame_principal.config(
    width=800 ,
    height=100,
    border=2,
    relief=SOLID,
    bg="silver"
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_titulo = Label(frame_principal, text="Inicio de Secion")
label_titulo.config(
    bg="silver",
    height=50,
    font="Arial"
)
label_titulo.pack()

label_nombre = Label(frame_principal, text="Nombre: ...", COMMAND = cambiarTexto()).pack(pady=10)
label_contrasena = Label(frame_principal, text="Contraseña: ...").pack(pady=10)

boton_aceptar = Button(ventana, text="Aceptar").pack(pady=10)
ventana.mainloop()