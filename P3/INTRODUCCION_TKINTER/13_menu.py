from tkinter import * 

def mostrarEstado(tipo):
    if tipo == "nuevo":   
        resultado.config(text=f"Nuevo Archivo")
    elif tipo == "guardar":
        resultado.config(text=f"Guardar Archivo")
    elif tipo == "copiar":
        resultado.config(text=f"Archivo Copiado")
    elif tipo == "recortar":
        resultado.config(text=f"Archivo recortado")

ventana = Tk()
ventana.title("menu")
ventana.geometry("500x500")

menuBar= Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu=Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mostrarEstado("nuevo"))
archivoMenu.add_command(label="Guardar Archivo",command=lambda: mostrarEstado("guardar"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

archivoMenu2=Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Edición", menu=archivoMenu2)
archivoMenu2.add_command(label="Copiar",command=lambda: mostrarEstado("copiar"))
archivoMenu2.add_command(label="Recortar",command=lambda: mostrarEstado("recortar"))
archivoMenu2.add_separator()
archivoMenu2.add_command(label="Salir", command=ventana.quit)

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()