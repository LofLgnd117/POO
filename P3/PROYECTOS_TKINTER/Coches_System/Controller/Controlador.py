from tkinter import messagebox
import sys
import os

# Ajuste de rutas para importar Model y View
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from View import Interfaz
from Model import Autos

class Controlador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.vista = Interfaz.Vistas(self.ventana) # Referencia a la vista
        self.menu_principal() # Iniciar en el menú principal

    # ------------------------------------------------------------------
    # 1.1 MENU PRINCIPAL
    # ------------------------------------------------------------------
    def menu_principal(self):
        # El controlador le dice a la vista: "Dibuja el menú principal"
        # y le pasa las funciones (comandos) que deben ejecutar los botones.
        self.vista.pantalla_menu_principal(
            cmd_autos=lambda: self.menu_acciones("Autos"),
            cmd_camionetas=lambda: print("Falta implementar Camionetas en el Controlador"), # Pendiente
            cmd_camiones=lambda: print("Falta implementar Camiones en el Controlador"), # Pendiente
            cmd_salir=self.ventana.quit
        )

    # ------------------------------------------------------------------
    # 1.2 MENU ACCIONES (Genérico o específico para Autos)
    # ------------------------------------------------------------------
    def menu_acciones(self, tipo):
        if tipo == "Autos":
            self.vista.pantalla_menu_acciones(
                tipo="Autos",
                cmd_insertar=self.insertar_autos,
                cmd_consultar=self.consultar_autos,
                cmd_cambiar=self.cambiar_autos,
                cmd_borrar=self.borrar_autos,
                cmd_volver=self.menu_principal
            )
        # Aquí agregarías los elif para Camiones y Camionetas más adelante

    # ------------------------------------------------------------------
    # 1.3 INSERTAR AUTOS
    # ------------------------------------------------------------------
    def insertar_autos(self):
        # 1. Definimos la función que se ejecutará al dar click en "Guardar"
        def realizar_insercion():
            # Obtenemos los datos de las variables de la vista
            datos = [v.get() for v in vars_entry]
            # Llamamos al MODELO
            if Autos.Autos.insertar(*datos):
                messagebox.showinfo("Éxito", "Auto guardado correctamente")
                self.menu_acciones("Autos")
            else:
                messagebox.showerror("Error", "No se pudo guardar el auto")

        # 2. Le pedimos a la vista que dibuje el formulario y nos devuelva las variables
        #    Pasamos 'realizar_insercion' como el comando del botón Guardar
        vars_entry = self.vista.pantalla_insertar_autos(
            cmd_guardar=realizar_insercion,
            cmd_volver=lambda: self.menu_acciones("Autos")
        )

    # ------------------------------------------------------------------
    # 1.4 CONSULTAR AUTOS
    # ------------------------------------------------------------------
    def consultar_autos(self):
        # 1. Pedimos los datos al MODELO
        datos = Autos.Autos.consultar()
        
        # 2. Le mandamos los datos a la VISTA para que los pinte
        self.vista.pantalla_consultar_autos(
            datos=datos,
            cmd_volver=lambda: self.menu_acciones("Autos")
        )

    # ------------------------------------------------------------------
    # 1.5 CAMBIAR AUTOS
    # ------------------------------------------------------------------
    def cambiar_autos(self):
        def realizar_cambio():
            id_val = var_id.get()
            datos = [v.get() for v in vars_entry]
            # Validación simple
            if not id_val:
                messagebox.showwarning("Atención", "Debes ingresar un ID")
                return

            # Llamada al MODELO
            if Autos.Autos.actualizar(id_val, *datos):
                messagebox.showinfo("Éxito", "Auto actualizado")
                self.menu_acciones("Autos")
            else:
                messagebox.showerror("Error", "Error al actualizar (Verifique ID)")

        # La vista dibuja y nos devuelve las variables para leerlas aquí
        var_id, vars_entry = self.vista.pantalla_cambiar_autos(
            cmd_actualizar=realizar_cambio,
            cmd_volver=lambda: self.menu_acciones("Autos")
        )

    # ------------------------------------------------------------------
    # 1.6 BORRAR AUTOS
    # ------------------------------------------------------------------
    def borrar_autos(self):
        def realizar_borrado():
            id_val = var_id.get()
            if not id_val: return
            
            if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar?"):
                # Llamada al MODELO
                if Autos.Autos.eliminar(id_val):
                    messagebox.showinfo("Éxito", "Auto eliminado")
                    self.menu_acciones("Autos")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar")

        var_id = self.vista.pantalla_borrar_autos(
            cmd_eliminar=realizar_borrado,
            cmd_volver=lambda: self.menu_acciones("Autos")
        )