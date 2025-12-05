from tkinter import messagebox
import sys
import os

# Ajuste de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- CORRECCIÓN IMPORTANTE AQUÍ ---
# Importamos directamente la CLASE desde el archivo.
# from Carpeta.Archivo import Clase
from Model.Autos import Autos
from Model.Camionetas import Camionetas
from Model.Camiones import Camiones

class Controlador:
    def __init__(self, ventana):
        self.ventana = ventana
        # Importamos la vista aquí dentro para evitar problemas de importación circular si los hubiera
        from View import Interfaz
        self.vista = Interfaz.Vistas(self.ventana)
        self.menu_principal()

# Menu
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

# Camionetas
    def insertar_camionetas(self):
        def guardar():
            datos = [v.get() for v in vars_entry] 
            cerrada = var_cerrada.get()
            
            if Camionetas.insertar(*datos, cerrada):
                messagebox.showinfo("Éxito", "Camioneta guardada")
                self.menu_acciones("Camionetas")
            else:
                messagebox.showerror("Error", "No se pudo guardar")

        vars_entry, var_cerrada = self.vista.pantalla_insertar_camionetas(
            cmd_guardar=guardar,
            cmd_volver=lambda: self.menu_acciones("Camionetas")
        )

    def consultar_camionetas(self):

        datos = Camionetas.consultar()
        self.vista.pantalla_consultar_camionetas(
            datos=datos,
            cmd_volver=lambda: self.menu_acciones("Camionetas")
        )

    def cambiar_camionetas(self):
        def actualizar():
            id_val = var_id.get()
            datos = [v.get() for v in vars_entry]
            cerrada = var_cerrada.get()

            if not id_val:
                messagebox.showwarning("Alerta", "Ingrese un ID")
                return

            if Camionetas.actualizar(id_val, *datos, cerrada):
                messagebox.showinfo("Éxito", "Camioneta actualizada")
                self.menu_acciones("Camionetas")
            else:
                messagebox.showerror("Error", "Error al actualizar")

        var_id, vars_entry, var_cerrada = self.vista.pantalla_cambiar_camionetas(
            cmd_actualizar=actualizar,
            cmd_volver=lambda: self.menu_acciones("Camionetas")
        )

    def borrar_camionetas(self):
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar Camioneta?"):
                if Camionetas.eliminar(var_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Camionetas")
                else:
                    messagebox.showerror("Error", "Fallo al eliminar")

        var_id = self.vista.pantalla_borrar_generico(
            titulo="Eliminar Camioneta",
            cmd_eliminar=eliminar,
            cmd_volver=lambda: self.menu_acciones("Camionetas")
        )

# Camiones
    def insertar_camiones(self):
        def guardar():
            datos = [v.get() for v in vars_entry]
            
            if Camiones.insertar(*datos):
                messagebox.showinfo("Éxito", "Camión guardado")
                self.menu_acciones("Camiones")
            else:
                messagebox.showerror("Error", "No se pudo guardar")

        vars_entry = self.vista.pantalla_insertar_camiones(
            cmd_guardar=guardar,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )

    def consultar_camiones(self):
        
        datos = Camiones.consultar()
        self.vista.pantalla_consultar_camiones(
            datos=datos,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )

    def cambiar_camiones(self):
        def actualizar():
            id_val = var_id.get()
            datos = [v.get() for v in vars_entry]
            if not id_val: return
            
            if Camiones.actualizar(id_val, *datos):
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
                if Camiones.eliminar(var_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Camiones")
                else:
                    messagebox.showerror("Error", "Fallo al eliminar")

        var_id = self.vista.pantalla_borrar_generico(
            titulo="Eliminar Camión",
            cmd_eliminar=eliminar,
            cmd_volver=lambda: self.menu_acciones("Camiones")
        )

# Autos
    def insertar_autos(self):
        def guardar():
            datos = [v.get() for v in vars_entry]
            if Autos.insertar(*datos):
                messagebox.showinfo("Éxito", "Auto guardado")
                self.menu_acciones("Autos")
            else: messagebox.showerror("Error", "Error al guardar")

        vars_entry = self.vista.pantalla_insertar_autos(guardar, lambda: self.menu_acciones("Autos"))

    def consultar_autos(self):
        datos = Autos.consultar()
        self.vista.pantalla_consultar_autos(datos, lambda: self.menu_acciones("Autos"))

    def cambiar_autos(self):
        def actualizar():
            if Autos.actualizar(var_id.get(), *[v.get() for v in vars_entry]):
                messagebox.showinfo("Éxito", "Actualizado")
                self.menu_acciones("Autos")
            else: messagebox.showerror("Error", "Error al actualizar")
        var_id, vars_entry = self.vista.pantalla_cambiar_autos(actualizar, lambda: self.menu_acciones("Autos"))

    def borrar_autos(self):
        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar?"):
                if Autos.eliminar(var_id.get()):
                    messagebox.showinfo("Éxito", "Eliminado")
                    self.menu_acciones("Autos")
                else: messagebox.showerror("Error", "Error al eliminar")
        
        var_id = self.vista.pantalla_borrar_generico("Eliminar Auto", eliminar, lambda: self.menu_acciones("Autos"))