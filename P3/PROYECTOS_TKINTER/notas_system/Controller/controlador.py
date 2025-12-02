from tkinter import messagebox
from model import nota
from model import usuario
from view import interfaz

class Controlador:

    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo, message="¡Acción realizada con éxito!")
        else:
            messagebox.showinfo(icon="info",title=titulo, message="No fue posible realizar la acción, vuelva a intentar")

    @staticmethod
    def registrar(nombre, apellidos, email, password):
        if not all([str(nombre).strip(), str(apellidos).strip(), str(email).strip(), password]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Correo electrónico inválido.")
            return False

        if len(password) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres.")
            return False

        try:
            registrado = usuario.Usuario.registrar(nombre, apellidos, email, password)
            if registrado:
                messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
                return True
            else:
                messagebox.showerror("Error", "No se pudo registrar el usuario. Verifique los datos o la conexión.")
                return False
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar: {e}")
            return False

    @staticmethod
    def login(email, password, ventana):
        if not all([str(email).strip(), password]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return None

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Correo electrónico inválido.")
            return None

        if len(password) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres.")
            return None

        try:
            registro = usuario.Usuario.iniciar_sesion(email, password)
            if registro:
                messagebox.showinfo("Éxito", f"Bienvenido {registro[1]} {registro[2]}, haz iniciado seción correctamente")
                interfaz.Vistas.menu_notas(ventana, registro[0], registro[1], registro[2])
                return registro
            else:
                messagebox.showerror("Error", "Email o contraseña incorrectos.")
                return None
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al iniciar sesión: {e}")
            return None

    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear Notas", respuesta)

    @staticmethod
    def mostrar_nota(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros
    
    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        respuesta=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.respuesta_sql("Cambiar Notas", respuesta)

    @staticmethod
    def eliminar_nota(id):
        respuesta = nota.Nota.eliminar(id)
        Controlador.respuesta_sql("Borrar Nota", respuesta)