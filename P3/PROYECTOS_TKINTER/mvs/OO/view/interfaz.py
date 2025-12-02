from controller import funciones
from tkinter import *
from model import operaciones
from tkinter import ttk
from tkinter import messagebox 
#Interfaz o View

class Vistas:
    def __init__(self,ventana):
        ventana.title("...Calculadora Básica...")
        ventana.geometry("500x400")
        ventana.resizable(False,False)
        self.interfaz(ventana)

    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        txt_numero1.focus()
        txt_numero1.pack(pady=5)

        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        txt_numero2.pack(pady=5)

        btn_suma=Button(ventana,text="+",command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.Controladores.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()
        
        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("Division",n1.get(),n2.get(),"/"))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack(pady=10)

    def menuPrincipal(self,ventana):
        menuBar= Menu(ventana)
        ventana.config(menu=menuBar)
        archivoMenu=Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciónes", menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: self.interfaz(ventana))
        archivoMenu.add_command(label="Consultar", command=lambda: self.consultar(ventana))
        archivoMenu.add_command(label="Cambiar",command=lambda:"")
        archivoMenu.add_command(label="Borrar",command=lambda: self.eliminar(ventana))
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=ventana.quit)
    
    def consultar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        label_titulo=Label(ventana, text=".::Lista de las Operaciónes::.") 
        label_titulo.pack(pady=5)
        label_titulo.config(font=("Arial", 18))

        lista = operaciones.Operaciones.mostrar()
        if not lista:
            label_vacio = Label(ventana, text="No hay operaciones registradas.")
            label_vacio.pack(pady=5)
            label_vacio.config(font=("Arial", 12))
        else:
            n = 1
            for fila in lista:
                texto = f"Operacion: {n}  ID:{fila[0]}  Fecha de creacion: {fila[1]} \nOperación: {fila[2]}{fila[4]}{fila[3]}={fila[5]}"
                label_item = Label(ventana, text=texto)
                label_item.pack()
                label_item.config(font=("Arial", 11))
                n += 1

        boton_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        boton_volver.pack()
        
    def cambiar(self, ventana):
        self.borrarPantalla
        self.menuPrincipal

        label_titulo = Label (ventana, text="CAMBIAR UNA OPERACION", font=("Arial", 12, "bold"))
        label_titulo.pack(pady=15)
        # ID
        label_titulo = Label (ventana, text="ID Operacion", font=("Arial", 12, "bold"))
        label_titulo.pack(pady=(5, 0,))

        id_var = StringVar(value=0)
        entry_id = Entry(ventana, textvariable=id_var, justify="center", width=10, font=("Arial", 12))
        entry_id.pack(pady=5)

        # Numero 1
        label_titulo = Label (ventana, text="Nuevo Numero 1", font=("Arial", 12, "bold"))
        label_titulo.pack(pady=(5, 0,))

        id_var = StringVar(value=0)
        entry_id = Entry(ventana, textvariable=id_var, justify="center", width=10, font=("Arial", 12))
        entry_id.pack(pady=5)
        # Numero 2
        label_titulo = Label (ventana, text="Nuevo Numero 2", font=("Arial", 12, "bold"))
        label_titulo.pack(pady=(5, 0,))

        id_var = StringVar(value=0)
        entry_id = Entry(ventana, textvariable=id_var, justify="center", width=10, font=("Arial", 12))
        entry_id.pack(pady=5)
        # Nuevo Signo
        label_titulo = Label (ventana, text="Nuevo Signo", font=("Arial", 12, "bold"))
        label_titulo.pack(pady=(5, 0,))

        id_var = StringVar(value=0)
        entry_id = Entry(ventana, textvariable=id_var, justify="center", width=10, font=("Arial", 12))
        entry_id.pack(pady=5)
        # Nuevo Resultado
        label_titulo = Label (ventana, text="Nuevo Resultado", font=("Arial", 12, "bold"))
        label_titulo.pack(pady=(5, 0,))

        res_var = StringVar()
        entry_res = Entry(ventana, textvariable=res_var, justify="center", width=25)
        entry_res.pack(pady=5)

    def eliminar(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        label_titulo = Label(ventana, text=".::Borrar una Operación::.", font=("Arial", 18))
        label_titulo.pack(pady=5)

        label_id = Label(ventana, text="Ingrese ID a buscar:", font=("Arial", 12))
        label_id.pack(pady=5)

        id_var = IntVar()
        entry_id = Entry(ventana, textvariable=id_var, justify="right", width=10)
        entry_id.focus()
        entry_id.pack(pady=5)

        label_info = Label(ventana, text="", font=("Arial", 10))
        label_info.pack(pady=10)

        def eliminar_accion():
            if operaciones.Operaciones.eliminar(id_var.get()):
                messagebox.showinfo("Éxito", "Operación eliminada correctamente")
                label_info.config(text="")
                id_var.set(0)
                boton_eliminar.pack_forget()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")

        boton_eliminar = Button(ventana, text="Eliminar", command=eliminar_accion, bg="white")

        def buscar_accion():
            dato = operaciones.Operaciones.buscar(id_var.get())
            
            if dato:
                texto = f"Encontrado: {dato[2]} {dato[4]} {dato[3]} = {dato[5]}"
                label_info.config(text=texto)
                
                boton_eliminar.pack(pady=5) 
            else:
                messagebox.showerror("ID no encontrado")
                boton_eliminar.pack_forget()

        boton_buscar = Button(ventana, text="Buscar ID", command=buscar_accion)
        boton_buscar.pack(pady=5)

        boton_volver = Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        boton_volver.pack(side=BOTTOM, pady=20)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()