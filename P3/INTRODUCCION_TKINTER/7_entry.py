from tkinter import *

def entrar():
    frame_bienvenido.config(
    width=500, 
    height=100, 
    bg="lightblue", 
    relief=SOLID, 
    border=2
    )
    label_bienvenido.config(
        text=f"Bienvenido al Sistema {entry_usuario.get()}"
    )

def borrar():
    entry_usuario.delete(0, END)
    entry_contrasena.delete(0, END)
    label_bienvenido.config(text="")
    frame_bienvenido.config(
        width=0, 
        height=0, 
        bg="lightblue", 
        relief=SOLID, 
        border=2
    )

ventana = Tk()
ventana.title("Entry")
ventana.geometry("500x500")

label_titulo=Label(ventana, text="Acceso al sistema")
label_titulo.pack()
label_titulo.config(
    font=("Arial", 18)
)

label_usuario=Label(ventana, text="Ingresa tu usuario")
label_usuario.pack()
label_usuario.config(
    font=("Arial", 12)
)

entry_usuario=Entry(ventana)
entry_usuario.pack()

label_contrasena=Label(ventana, text="Ingresa tu contraseña")
label_contrasena.pack()
label_contrasena.config(
    font=("Arial", 12)
)

entry_contrasena=Entry(ventana)
entry_contrasena.pack()

button_aceptar=Button(ventana, text="Aceptar", command= entrar)
button_aceptar.pack()

button_borrar=Button(ventana, text="Borrar", command= borrar)
button_borrar.pack()

frame_bienvenido=Frame(ventana)
frame_bienvenido.pack(pady=10)

label_bienvenido=Label(frame_bienvenido, text="")
label_bienvenido.pack(pady=25)
ventana.mainloop()