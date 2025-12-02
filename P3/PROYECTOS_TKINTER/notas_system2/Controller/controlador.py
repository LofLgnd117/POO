from tkinter import *

class Controlador:
    @staticmethod
    def registrar(nombre, apellidos, email, password):
            registro=usuario.Usuario.iniciar_sesion(nombre, apellidos,email,password)
            if registro:
                self.menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()