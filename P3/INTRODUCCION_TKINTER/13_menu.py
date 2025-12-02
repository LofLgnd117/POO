from tkinter import *

ventana = Tk()
ventana.title("menu")
ventana.geometry("500x500")

#-------------------------------------------------- Función mostrar --------------------------------------------------
def mostrarestado(tipo):
    resultado.config(text=f"{tipo}" )
    if tipo == "Nuevo Archivo" or tipo == "Nuevo Archivo2":
        resultado.config(text="Has creado un nuevo archivo")
    elif tipo == "Guardar Archivo" or tipo == "Guardar Archivo2":
        resultado.config(text="Has guardado el archivo")
    elif tipo == "Salir" or tipo == "Salir2":
        ventana.quit()
#------------------------------------------------------- menu --------------------------------------------------------
menuBar = Menu(ventana)

ventana.config(menu=menuBar)
archivoMenu = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo", 
                        command=lambda: mostrarestado("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo", 
                        command=lambda: mostrarestado("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menuBar)
archivoMenu2 = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Archivo2", menu=archivoMenu2)
archivoMenu2.add_command(label="Nuevo Archivo2", 
                        command=lambda: mostrarestado("Nuevo Archivo2"))
archivoMenu2.add_command(label="Guardar Archivo2", 
                        command=lambda: mostrarestado("Guardar Archivo2"))
archivoMenu2.add_separator()
archivoMenu2.add_command(label="Salir2", command=ventana.quit)



resultado = Label(ventana, text="")
resultado.pack(pady=10)



ventana.mainloop()