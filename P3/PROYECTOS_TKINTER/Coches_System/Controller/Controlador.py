from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from View import Interfaz
from Model import Autos, Camionetas, Camiones

class Controlador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.vista = Interfaz.Vistas(self.ventana)
        self.menu_principal()

#   Menus -----------------------------------------------------------------------------------------------------------------------

    def menu_principal(self):
        self.vista.pantalla_menu_principal(
            cmd_autos=lambda: self.menu_acciones("Autos"),
            cmd_camionetas=lambda: self.menu_acciones("Camionetas"), 
            cmd_camiones=lambda: self.menu_acciones("Camiones"),     
            cmd_salir=self.ventana.quit
        )

    def menu_acciones(self, tipo):
        if tipo == "Autos":
            funcs = (self.insertar_autos, self.consultar_autos, self.cambiar_autos, self.borrar_autos)
        elif tipo == "Camionetas":
            funcs = (self.insertar_camionetas, self.consultar_camionetas, self.cambiar_camionetas, self.borrar_camionetas)
        elif tipo == "Camiones":
            funcs = (self.insertar_camiones, self.consultar_camiones, self.cambiar_camiones, self.borrar_camiones)
        self.vista.pantalla_menu_acciones(
            tipo=tipo,
            cmd_insertar=funcs[0],
            cmd_consultar=funcs[1],
            cmd_cambiar=funcs[2],
            cmd_borrar=funcs[3],
            cmd_volver=self.menu_principal
        )

    # ------------------------------------------------------------------
    # 1. Autos
    # ------------------------------------------------------------------
    def insertar_autos(self):
        def guardar():
            datos = [v.get() for v in vars_entry]
            if Autos.Autos.insertar(*datos):
                messagebox.showinfo("Éxito", "Auto guardado")
                self.menu_acciones("Autos")
            else: messagebox.showerror("Error", "Error al guardar")

        vars_entry = self.vista.pantalla_insertar_autos(guardar, lambda: self.menu_acciones("Autos"))

    def consultar_autos(self):
        datos = Autos.Autos.consultar()
        self.vista.pantalla_consultar_autos(datos, lambda: self.menu_acciones("Autos"))

    def cambiar_autos(self):
        def actualizar():
            if Autos.Autos.actualizar(var_id.get(), *[v.get() for v in vars_entry]):
                messagebox.showinfo("Éxito", "Actualizado")
                self.menu_acciones("Autos")
            else: messagebox.showerror("Error", "Error al actualizar")
        var_id, vars_entry = self.vista.pantalla_cambiar_autos(actualizar, lambda: self.menu_acciones("Autos"))

    def borrar_autos(self):
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar?"):
                if Autos.Autos.eliminar(var_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Autos")
                else: messagebox.showerror("Error", "Error al eliminar")
        
        var_id = self.vista.pantalla_borrar_generico("Eliminar Auto", eliminar, lambda: self.menu_acciones("Autos"))

    # ------------------------------------------------------------------
    # 2. Camionetas
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 3. Camiones
    # ------------------------------------------------------------------
    def insertar_camiones(self):
        def guardar():
            datos = [v.get() for v in vars_entry]
            if Camiones.Camiones.insertar(*datos):
                messagebox.showinfo("Éxito", "Camión guardado")
                self.menu_acciones("Camiones")
            else:
                messagebox.showerror("Error", "No se pudo guardar")

        vars_entry = self.vista.pantalla_insertar_camiones(
            cmd_guardar=guardar,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )

    def consultar_camiones(self):
        datos = Camiones.Camiones.consultar()
        self.vista.pantalla_consultar_camiones(
            datos=datos,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )

    def cambiar_camiones(self):
        def actualizar():
            id_val = var_id.get()
            datos = [v.get() for v in vars_entry]
            if not id_val: return
            
            if Camiones.Camiones.actualizar(id_val, *datos):
                messagebox.showinfo("Éxito", "Camión actualizado")
                self.menu_acciones("Camiones")
            else:
                messagebox.showerror("Error", "Error al actualizar")

        var_id, vars_entry = self.vista.pantalla_cambiar_camiones(
            cmd_actualizar=actualizar,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )

    def borrar_camiones(self):
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar Camión?"):
                if Camiones.Camiones.eliminar(var_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Camiones")
                else:
                    messagebox.showerror("Error", "Fallo al eliminar")

        var_id = self.vista.pantalla_borrar_generico(
            titulo="Eliminar Camión",
            cmd_eliminar=eliminar,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )