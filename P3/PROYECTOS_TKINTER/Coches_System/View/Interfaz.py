from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# Importamos los modelos
from Model import Autos, Camiones, Camionetas

class Vistas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("900x600")
        self.ventana.title("Coches System MVC")
        self.menu_principal()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    # ------------------------------------------------------------------
    #                           MENUS
    # ------------------------------------------------------------------
    def menu_principal(self):
        self.borrarPantalla()
        Label(self.ventana, text=".:: Menu Principal ::.", font=("Arial", 20, "bold")).pack(pady=20)
        
        Button(self.ventana, text="1.- Autos", width=30, height=2, 
               command=lambda: self.menu_acciones("Autos")).pack(pady=10)
        
        Button(self.ventana, text="2.- Camionetas", width=30, height=2,
               command=lambda: self.menu_acciones("Camionetas")).pack(pady=10)
        
        Button(self.ventana, text="3.- Camiones", width=30, height=2,
               command=lambda: self.menu_acciones("Camiones")).pack(pady=10)
        
        Button(self.ventana, text="4.- Salir", width=30,
               command=self.ventana.quit).pack(pady=20)

    def menu_acciones(self, tipo):
        self.borrarPantalla()
        Label(self.ventana, text=f"Menu de {tipo}", font=("Arial", 18)).pack(pady=10)
        
        # Definir comandos dinámicamente según el tipo
        cmd_insertar = getattr(self, f"insertar_{tipo.lower()}")
        cmd_consultar = getattr(self, f"consultar_{tipo.lower()}")
        cmd_cambiar = getattr(self, f"cambiar_{tipo.lower()}")
        cmd_borrar = getattr(self, f"borrar_{tipo.lower()}")

        Button(self.ventana, text="1.- Insertar", width=20, command=cmd_insertar).pack(pady=5)
        Button(self.ventana, text="2.- Consultar", width=20, command=cmd_consultar).pack(pady=5)
        Button(self.ventana, text="3.- Actualizar", width=20, command=cmd_cambiar).pack(pady=5)
        Button(self.ventana, text="4.- Eliminar", width=20, command=cmd_borrar).pack(pady=5)
        Button(self.ventana, text="5.- Regresar", width=20, command=self.menu_principal).pack(pady=20)

    # ------------------------------------------------------------------
    #                           AUTOS
    # ------------------------------------------------------------------
    def insertar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="Insertar Auto", font=("Arial", 16)).pack(pady=10)
        
        vars_auto = [StringVar() for _ in range(6)] # marca, color, modelo, velocidad, cab, plazas
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        
        frm = Frame(self.ventana)
        frm.pack()
        
        for i, lab in enumerate(labels):
            Label(frm, text=lab).grid(row=i, column=0, padx=10, pady=5, sticky=E)
            Entry(frm, textvariable=vars_auto[i]).grid(row=i, column=1, padx=10, pady=5)

        def guardar():
            res = Autos.Autos.insertar(*[v.get() for v in vars_auto])
            if res: messagebox.showinfo("Éxito", "Auto guardado"); self.menu_acciones("Autos")
            else: messagebox.showerror("Error", "No se pudo guardar")

        Button(self.ventana, text="Guardar", command=guardar).pack(pady=15)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def consultar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Autos", font=("Arial", 16)).pack(pady=10)
        
        tree = ttk.Treeview(self.ventana, columns=("ID","Marca","Color","Modelo","Vel","Cab","Pla"), show='headings')
        for col in tree['columns']: tree.heading(col, text=col); tree.column(col, width=100)
        tree.pack(pady=10, fill=X, padx=20)

        datos = Autos.Autos.consultar()
        for d in datos: tree.insert("", END, values=d)

        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack(pady=10)

    def cambiar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="Actualizar Auto", font=("Arial", 16)).pack(pady=10)
        
        # ID y Datos
        v_id = StringVar()
        vars_auto = [StringVar() for _ in range(6)]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        
        frm = Frame(self.ventana)
        frm.pack()
        
        Label(frm, text="ID a modificar:").grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Entry(frm, textvariable=v_id).grid(row=0, column=1, padx=5, pady=5)
        
        for i, lab in enumerate(labels):
            Label(frm, text=lab).grid(row=i+1, column=0, padx=5, pady=5, sticky=E)
            Entry(frm, textvariable=vars_auto[i]).grid(row=i+1, column=1, padx=5, pady=5)

        def actualizar():
            res = Autos.Autos.actualizar(v_id.get(), *[v.get() for v in vars_auto])
            if res: messagebox.showinfo("Éxito", "Auto actualizado"); self.menu_acciones("Autos")
            else: messagebox.showerror("Error", "Error al actualizar")

        Button(self.ventana, text="Actualizar", command=actualizar).pack(pady=15)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def borrar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="Borrar Auto", font=("Arial", 16)).pack(pady=10)
        v_id = StringVar()
        
        frm = Frame(self.ventana)
        frm.pack()
        Label(frm, text="Ingrese ID:").pack(side=LEFT, padx=5)
        Entry(frm, textvariable=v_id).pack(side=LEFT, padx=5)
        
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar?"):
                res = Autos.Autos.eliminar(v_id.get())
                if res: messagebox.showinfo("Éxito", "Eliminado"); self.menu_acciones("Autos")
                else: messagebox.showerror("Error", "No existe ID")

        Button(self.ventana, text="Eliminar", command=eliminar).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    # ------------------------------------------------------------------
    #                           CAMIONETAS
    # ------------------------------------------------------------------
    def insertar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="Insertar Camioneta", font=("Arial", 16)).pack(pady=10)
        
        vars_c = [StringVar() for _ in range(7)] # Marca...Traccion
        v_cerrada = BooleanVar()
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción"]
        
        frm = Frame(self.ventana)
        frm.pack()
        
        for i, lab in enumerate(labels):
            Label(frm, text=lab).grid(row=i, column=0, sticky=E, pady=5)
            Entry(frm, textvariable=vars_c[i]).grid(row=i, column=1, pady=5)
        
        Checkbutton(frm, text="¿Es Cerrada?", variable=v_cerrada).grid(row=7, column=1, sticky=W)

        def guardar():
            res = Camionetas.Camionetas.insertar(*[v.get() for v in vars_c], v_cerrada.get())
            if res: messagebox.showinfo("Éxito", "Camioneta guardada"); self.menu_acciones("Camionetas")
            else: messagebox.showerror("Error", "Error al guardar")

        Button(self.ventana, text="Guardar", command=guardar).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def consultar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Camionetas", font=("Arial", 16)).pack(pady=10)
        
        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Trac", "Cerrada")
        tree = ttk.Treeview(self.ventana, columns=cols, show="headings")
        for c in cols: tree.heading(c, text=c); tree.column(c, width=80)
        tree.pack(fill=X, padx=20, pady=10)

        datos = Camionetas.Camionetas.consultar()
        for d in datos:
            # Convertir el 1/0 de la BD a Si/No para visualización
            lista_d = list(d)
            lista_d[8] = "Si" if lista_d[8] == 1 else "No"
            tree.insert("", END, values=lista_d)

        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack(pady=10)

    def cambiar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="Actualizar Camioneta", font=("Arial", 16)).pack(pady=10)
        
        v_id = StringVar()
        vars_c = [StringVar() for _ in range(7)]
        v_cerrada = BooleanVar()
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción"]

        frm = Frame(self.ventana)
        frm.pack()
        
        Label(frm, text="ID a modificar:").grid(row=0, column=0, sticky=E)
        Entry(frm, textvariable=v_id).grid(row=0, column=1)
        
        for i, lab in enumerate(labels):
            Label(frm, text=lab).grid(row=i+1, column=0, sticky=E, pady=2)
            Entry(frm, textvariable=vars_c[i]).grid(row=i+1, column=1, pady=2)
        Checkbutton(frm, text="¿Es Cerrada?", variable=v_cerrada).grid(row=8, column=1, sticky=W)

        def actualizar():
            res = Camionetas.Camionetas.actualizar(v_id.get(), *[v.get() for v in vars_c], v_cerrada.get())
            if res: messagebox.showinfo("Éxito", "Actualizado"); self.menu_acciones("Camionetas")
            else: messagebox.showerror("Error", "Error al actualizar")

        Button(self.ventana, text="Actualizar", command=actualizar).pack(pady=15)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def borrar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="Borrar Camioneta", font=("Arial", 16)).pack(pady=10)
        v_id = StringVar()
        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="ID:").pack(side=LEFT); Entry(frm, textvariable=v_id).pack(side=LEFT)
        
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar?"):
                if Camionetas.Camionetas.eliminar(v_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Camionetas")
                else: messagebox.showerror("Error", "Fallo al eliminar")

        Button(self.ventana, text="Borrar", command=eliminar).pack(pady=10)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    # ------------------------------------------------------------------
    #                           CAMIONES
    # ------------------------------------------------------------------
    def insertar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="Insertar Camión", font=("Arial", 16)).pack(pady=10)
        
        vars_k = [StringVar() for _ in range(8)]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Carga"]
        frm = Frame(self.ventana); frm.pack()
        
        for i, lab in enumerate(labels):
            Label(frm, text=lab).grid(row=i, column=0, sticky=E, pady=5)
            Entry(frm, textvariable=vars_k[i]).grid(row=i, column=1, pady=5)
            
        def guardar():
            res = Camiones.Camiones.insertar(*[v.get() for v in vars_k])
            if res: messagebox.showinfo("Éxito", "Camión guardado"); self.menu_acciones("Camiones")
            else: messagebox.showerror("Error", "Error al guardar")

        Button(self.ventana, text="Guardar", command=guardar).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def consultar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Camiones", font=("Arial", 16)).pack(pady=10)
        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Ejes", "Carga")
        tree = ttk.Treeview(self.ventana, columns=cols, show="headings")
        for c in cols: tree.heading(c, text=c); tree.column(c, width=80)
        tree.pack(fill=X, padx=20, pady=10)
        
        datos = Camiones.Camiones.consultar()
        for d in datos: tree.insert("", END, values=d)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack(pady=10)

    def cambiar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="Actualizar Camión", font=("Arial", 16)).pack(pady=10)
        v_id = StringVar()
        vars_k = [StringVar() for _ in range(8)]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Carga"]
        
        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="ID a modificar:").grid(row=0, column=0, sticky=E)
        Entry(frm, textvariable=v_id).grid(row=0, column=1)
        
        for i, lab in enumerate(labels):
            Label(frm, text=lab).grid(row=i+1, column=0, sticky=E, pady=2)
            Entry(frm, textvariable=vars_k[i]).grid(row=i+1, column=1, pady=2)

        def actualizar():
            res = Camiones.Camiones.actualizar(v_id.get(), *[v.get() for v in vars_k])
            if res: messagebox.showinfo("Éxito", "Actualizado"); self.menu_acciones("Camiones")
            else: messagebox.showerror("Error", "Error al actualizar")

        Button(self.ventana, text="Actualizar", command=actualizar).pack(pady=15)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def borrar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="Borrar Camión", font=("Arial", 16)).pack(pady=10)
        v_id = StringVar()
        frm = Frame(self.ventana); frm.pack()
        Label(frm, text="ID:").pack(side=LEFT); Entry(frm, textvariable=v_id).pack(side=LEFT)
        
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar?"):
                if Camiones.Camiones.eliminar(v_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Camiones")
                else: messagebox.showerror("Error", "Fallo al eliminar")

        Button(self.ventana, text="Borrar", command=eliminar).pack(pady=10)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()