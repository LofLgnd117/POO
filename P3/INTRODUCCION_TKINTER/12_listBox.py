from tkinter import * 

ventana = Tk()
ventana.title("listBox")
ventana.geometry("500x500")

def mostrarEstado():
    seleccion = lista.get(lista.curselection())
    resultado.config(text=f"Seleccionaste: {seleccion}")

lista=Listbox(ventana, width=10, height=5, selectmode='single')
lista.pack()

opciones=['Amarillo','Rojo', 'Azul', 'Morado']
for i in opciones:
    lista.insert(END,i)

boton=Button(ventana, text="Mostrar seleccion del usuario", command=mostrarEstado)
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()