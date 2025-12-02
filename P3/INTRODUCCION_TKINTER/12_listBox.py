from tkinter import *

ventana = Tk()
ventana.title("listBox")
ventana.geometry("500x500")
#-------------------------------------------------- Función mostrar --------------------------------------------------
def mostrarestado():
    seleccion = lista.get(lista.curselection())
    seleccionado = lista.get(lista.curselection())
    resultado.config(text="Opción seleccionada: " + seleccion)
#-------------------------------------------------- listbox --------------------------------------------------

lista= Listbox(ventana, width=20, height=10, selectmode=SINGLE)
lista.pack(pady=20)

opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
for opcion in opciones:
    lista.insert(END, opcion)


lista = Listbox(ventana)
lista.insert(1, "Opción 1")
lista.insert(2, "Opción 2")
lista.insert(3, "Opción 3")
lista.insert(4, "Opción 4")
lista.pack(pady=20)

boton = Button(ventana, text="Mostrar seleccion", command=mostrarestado)
boton.pack(pady=10)

resultado = Label(ventana, text="")
resultado.pack(pady=10)

notificaciones = IntVar()


ventana.mainloop()