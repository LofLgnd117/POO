from tkinter import *

class Vistas():
    def __init__(self,ventana):
        ventana.title("Gestión de Notas")
        ventana.geometry("500x400")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        label_titulo=Label(ventana, text=".::Menu principal::.") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        boton_registro=Button(ventana, text="1.-Registro",command=lambda: self.registro(ventana))
        boton_registro.pack(pady=5)
        boton_registro.config()

        boton_login=Button(ventana, text="2.-Login", command=lambda: self.login(ventana))
        boton_login.pack(pady=5)
        boton_login.config()

        boton_salir=Button(ventana, text="3.-Salir")
        boton_salir.pack(pady=5)
        boton_salir.config()

    def registro(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Registro en el Sistema::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_nombre=Label(ventana, text="¿Cual es tu nombre?:")
        lbl_nombre.pack(pady=5)
        lbl_nombre.config()
        entry_nombre=Entry(ventana, width=30)
        entry_nombre.pack(pady=5)

        lbl_apellidos=Label(ventana, text="¿Cuales son tus apellidos?:")
        lbl_apellidos.pack(pady=5)
        lbl_apellidos.config()
        entry_apellidos=Entry(ventana, width=30)
        entry_apellidos.pack(pady=5)

        lbl_email=Label(ventana, text="Ingresa tu email:")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30)
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30, show="*")
        entry_contrasena.pack(pady=5)

        boton_registrar=Button(ventana, text="Registrar")
        boton_registrar.pack(pady=5)
        boton_registrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

    def login(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Inicio de Sesión::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_email=Label(ventana, text="Ingresa tu E-mail:")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30)
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30, show="*")
        entry_contrasena.pack(pady=5)

        boton_entrar=Button(ventana, text="Entrar", command=lambda: self.menu_notas(ventana, "Leonardo", "Verdin"))
        boton_entrar.pack(pady=5)
        boton_entrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

    def menu_notas(self,ventana,nombre,apellidos):
        self.borrarPantalla(ventana)
        label_titulo=Label(ventana, text=f".::Bienvenido {nombre} {apellidos}, has iniciado sesión::.") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        boton_crear=Button(ventana, text="1.-Crear",command=lambda: self.crear())
        boton_crear.pack(pady=5)
        boton_crear.config()

        boton_mostrar=Button(ventana, text="2.-Mostrar", command=lambda: "")
        boton_mostrar.pack(pady=5)
        boton_mostrar.config()

        boton_cambiar=Button(ventana, text="3.-Cambiar", command=lambda: "")
        boton_cambiar.pack(pady=5)
        boton_cambiar.config()

        boton_eliminar=Button(ventana, text="4.-Eliminar", command=lambda: "")
        boton_eliminar.pack(pady=5)
        boton_eliminar.config()

        boton_regresar=Button(ventana, text="5.-Regresar", command=lambda: self.login(ventana))
        boton_regresar.pack(pady=5)
        boton_regresar.config()

    def crear(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Crear Nota::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_email=Label(ventana, text="Titulo:")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30)
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30)
        entry_contrasena.pack(pady=5)

        boton_entrar=Button(ventana, text="Entrar", command=lambda: self.menu_notas)
        boton_entrar.pack(pady=5)
        boton_entrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

    def cambiar_nota(self,ventana):

        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::, has iniciado sesión, vamos a modificar una nota::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_id_nota=Label(ventana, text="ID de la nota a cambiar:")
        lbl_id_nota.pack(pady=5)
        lbl_id_nota.config()
        entry_id_nota=Entry(ventana, width=30)
        entry_id_nota.pack(pady=5)

        lbl_nuevo_titulo=Label(ventana, text="Nuevo titulo:")
        lbl_nuevo_titulo.pack(pady=5)
        lbl_nuevo_titulo.config()
        entry_nuevo_titulo=Entry(ventana, width=30)
        entry_nuevo_titulo.pack(pady=5)

        lbl_descripcion=Label(ventana, text="Nueva Descripcion:")
        lbl_descripcion.pack(pady=5)
        lbl_descripcion.config()
        entry_descripcion=Entry(ventana, width=30)
        entry_descripcion.pack(pady=5)


        boton_entrar=Button(ventana, text="guardar", command=lambda: self.menu_notas)
        boton_entrar.pack(pady=5)
        boton_entrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

def cambiar_nota(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::, has iniciado sesión, vamos a eliminar una nota::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_id_nota=Label(ventana, text="ID de la nota a eliminar:")
        lbl_id_nota.pack(pady=5)
        lbl_id_nota.config()
        txt_id = Entry(ventana)
        txt_id.focus
        txt_id.pach(pady=15)

        lbl_nuevo_titulo=Label(ventana, text="Nuevo titulo:")
        lbl_nuevo_titulo.pack(pady=5)
        lbl_nuevo_titulo.config()
        entry_nuevo_titulo=Entry(ventana, width=30)
        entry_nuevo_titulo.pack(pady=5)

        lbl_descripcion=Label(ventana, text="Nueva Descripcion:")
        lbl_descripcion.pack(pady=5)
        lbl_descripcion.config()
        entry_descripcion=Entry(ventana, width=30)
        entry_descripcion.pack(pady=5)


        boton_entrar=Button(ventana, text="guardar", command=lambda: self.menu_notas)
        boton_entrar.pack(pady=5)
        boton_entrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()