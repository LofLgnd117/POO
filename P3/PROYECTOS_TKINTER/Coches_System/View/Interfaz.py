from tkinter import *
from tkinter import ttk

class Vistas:
    def __init__(self, ventana):
        self.ventana = ventana

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    # --- MENU PRINCIPAL (Solo dibuja y asigna comandos que recibe) ---
    def pantalla_menu_principal(self, cmd_autos, cmd_camionetas, cmd_camiones, cmd_salir):
        self.borrarPantalla()
        Label(self.ventana, text=".:: Menu Principal ::.", font=("Arial", 20, "bold")).pack(pady=20)
        Button(self.ventana, text="1.- Coches", width=30, command=cmd_autos).pack(pady=5)
        Button(self.ventana, text="2.- Camionetas", width=30, command=cmd_camionetas).pack(pady=5)
        Button(self.ventana, text="3.- Camiones", width=30, command=cmd_camiones).pack(pady=5)
        Button(self.ventana, text="4.- Salir", width=30, bg="#FFCDD2", command=cmd_salir).pack(pady=20)

    # --- MENU ACCIONES ---
    def pantalla_menu_acciones(self, tipo, cmd_insertar, cmd_consultar, cmd_cambiar, cmd_borrar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text=f"Menu de {tipo}", font=("Arial", 18)).pack(pady=10)
        Button(self.ventana, text="1.- Insertar", width=20, command=cmd_insertar).pack(pady=5)
        Button(self.ventana, text="2.- Consultar", width=20, command=cmd_consultar).pack(pady=5)
        Button(self.ventana, text="3.- Actualizar", width=20, command=cmd_cambiar).pack(pady=5)
        Button(self.ventana, text="4.- Eliminar", width=20, command=cmd_borrar).pack(pady=5)
        Button(self.ventana, text="5.- Regresar", width=20, bg="#BBDEFB", command=cmd_volver).pack(pady=20)

    # --- INSERTAR AUTOS ---
    def pantalla_insertar_autos(self, cmd_guardar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Agregar coches", font=("Arial", 16)).pack(pady=10)
        
        vars_entry = [StringVar() for _ in range(6)]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        frm = Frame(self.ventana)
        frm.pack()

        for i, txt in enumerate(labels):
            Label(frm, text=txt).grid(row=i, column=0, sticky=E, padx=5, pady=5)
            Entry(frm, textvariable=vars_entry[i]).grid(row=i, column=1, padx=5, pady=5)

        Button(self.ventana, text="Guardar", bg="#C8E6C9", command=cmd_guardar).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=5)
        
        return vars_entry # Retornamos las variables para que el Controlador las lea

    # --- CONSULTAR AUTOS ---
    def pantalla_consultar_autos(self, datos, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Coches Agregados", font=("Arial", 16)).pack(pady=10)
        
        tree = ttk.Treeview(self.ventana, columns=("ID","Marca","Color","Modelo","Vel","Cab","Pla"), show='headings')
        for col in tree['columns']:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill=X, padx=20)

        # Insertamos los datos que nos mandó el controlador
        for fila in datos:
            tree.insert("", END, values=fila)

        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=10)

    # --- CAMBIAR AUTOS ---
    def pantalla_cambiar_autos(self, cmd_actualizar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Modificar Coche", font=("Arial", 16)).pack(pady=10)
        
        var_id = StringVar()
        vars_entry = [StringVar() for _ in range(6)]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]

        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="ID a modificar:").grid(row=0, column=0, sticky=E)
        Entry(frm, textvariable=var_id).grid(row=0, column=1)

        for i, txt in enumerate(labels):
            Label(frm, text=txt).grid(row=i+1, column=0, sticky=E, pady=2)
            Entry(frm, textvariable=vars_entry[i]).grid(row=i+1, column=1, pady=2)

        Button(self.ventana, text="Guardar Cambios", bg="#FFF9C4", command=cmd_actualizar).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=5)
        
        return var_id, vars_entry

    # --- BORRAR AUTOS ---
    def pantalla_borrar_autos(self, cmd_eliminar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Eliminar Coche", font=("Arial", 16)).pack(pady=10)
        
        var_id = StringVar()
        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="Ingrese ID:").pack(side=LEFT)
        Entry(frm, textvariable=var_id).pack(side=LEFT, padx=5)

        Button(self.ventana, text="Eliminar", bg="#FFCDD2", command=cmd_eliminar).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=5)
        
        return var_id