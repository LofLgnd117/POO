from tkinter import *
from tkinter import ttk

class Vistas:
    def __init__(self, ventana):
        self.ventana = ventana

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    # Menus
    def pantalla_menu_principal(self, cmd_autos, cmd_camionetas, cmd_camiones, cmd_salir):
        self.borrarPantalla()
        Label(self.ventana, text=".:: Menu Principal ::.", font=("Arial", 20, "bold")).pack(pady=20)
        Button(self.ventana, text="1.- Autos", width=30, command=cmd_autos).pack(pady=5)
        Button(self.ventana, text="2.- Camionetas", width=30, command=cmd_camionetas).pack(pady=5)
        Button(self.ventana, text="3.- Camiones", width=30, command=cmd_camiones).pack(pady=5)
        Button(self.ventana, text="4.- Salir", width=30, bg="#FFCDD2", command=cmd_salir).pack(pady=20)

    def pantalla_menu_acciones(self, tipo, cmd_insertar, cmd_consultar, cmd_cambiar, cmd_borrar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text=f"Menu de {tipo}", font=("Arial", 18)).pack(pady=10)
        Button(self.ventana, text="1.- Insertar", width=20, command=cmd_insertar).pack(pady=5)
        Button(self.ventana, text="2.- Consultar", width=20, command=cmd_consultar).pack(pady=5)
        Button(self.ventana, text="3.- Actualizar", width=20, command=cmd_cambiar).pack(pady=5)
        Button(self.ventana, text="4.- Eliminar", width=20, command=cmd_borrar).pack(pady=5)
        Button(self.ventana, text="5.- Regresar", width=20, bg="#BBDEFB", command=cmd_volver).pack(pady=20)

    # cosos
    def _crear_formulario(self, labels, vars_entry):
        frm = Frame(self.ventana)
        frm.pack()
        for i, txt in enumerate(labels):
            Label(frm, text=txt).grid(row=i, column=0, sticky=E, padx=5, pady=5)
            Entry(frm, textvariable=vars_entry[i]).grid(row=i, column=1, padx=5, pady=5)
        return frm

    # Autos
    def pantalla_insertar_autos(self, cmd_guardar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Agregar Auto", font=("Arial", 16)).pack(pady=10)
        vars_e = [StringVar() for _ in range(6)]
        self._crear_formulario(["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"], vars_e)
        Button(self.ventana, text="Guardar", bg="#C8E6C9", command=cmd_guardar).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack()
        return vars_e

    def pantalla_consultar_autos(self, datos, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Autos", font=("Arial", 16)).pack(pady=10)
        cols = ("ID","Marca","Color","Modelo","Vel","Cab","Pla")
        self._crear_tabla(cols, datos)
        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=10)

    def pantalla_cambiar_autos(self, cmd_act, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Modificar Auto", font=("Arial", 16)).pack(pady=10)
        v_id, vars_e = self._crear_form_actualizar(["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"])
        Button(self.ventana, text="Actualizar", bg="#FFF9C4", command=cmd_act).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack()
        return v_id, vars_e

    # Camionetas

    # Camiones
    def pantalla_insertar_camiones(self, cmd_guardar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Agregar Camión", font=("Arial", 16)).pack(pady=10)
        vars_e = [StringVar() for _ in range(8)]
        self._crear_formulario(["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Carga"], vars_e)
        Button(self.ventana, text="Guardar", bg="#C8E6C9", command=cmd_guardar).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack()
        return vars_e

    def pantalla_consultar_camiones(self, datos, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Camiones", font=("Arial", 16)).pack(pady=10)
        cols = ("ID","Marca","Color","Modelo","Vel","Cab","Pla","Ejes","Carga")
        self._crear_tabla(cols, datos)
        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=10)

    def pantalla_cambiar_camiones(self, cmd_act, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text="Modificar Camión", font=("Arial", 16)).pack(pady=10)
        v_id, vars_e = self._crear_form_actualizar(["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Carga"])
        Button(self.ventana, text="Actualizar", bg="#FFF9C4", command=cmd_act).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack()
        return v_id, vars_e

    # Iguales
    def pantalla_borrar_generico(self, titulo, cmd_eliminar, cmd_volver):
        self.borrarPantalla()
        Label(self.ventana, text=titulo, font=("Arial", 16)).pack(pady=10)
        var_id = StringVar()
        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="Ingrese ID:").pack(side=LEFT)
        Entry(frm, textvariable=var_id).pack(side=LEFT, padx=5)
        Button(self.ventana, text="Eliminar", bg="#FFCDD2", command=cmd_eliminar).pack(pady=10)
        Button(self.ventana, text="Volver", command=cmd_volver).pack(pady=5)
        return var_id

    def _crear_tabla(self, columnas, datos):
        tree = ttk.Treeview(self.ventana, columns=columnas, show='headings')
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=80)
        tree.pack(fill=X, padx=20)
        for d in datos:
            tree.insert("", END, values=d)

    def _crear_form_actualizar(self, labels):
        var_id = StringVar()
        vars_entry = [StringVar() for _ in range(len(labels))]
        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="ID a modificar:").grid(row=0, column=0, sticky=E)
        Entry(frm, textvariable=var_id).grid(row=0, column=1)
        for i, txt in enumerate(labels):
            Label(frm, text=txt).grid(row=i+1, column=0, sticky=E, pady=2)
            Entry(frm, textvariable=vars_entry[i]).grid(row=i+1, column=1, pady=2)
        return var_id, vars_entry