from tkinter import *
from tkinter import messagebox
from controller import controlador

class Vistas():
    def __init__(self,ventana):
        ventana.title("Gestión de Notas")
        ventana.geometry("500x400")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
   
    @staticmethod
    def menu_principal(ventana):
        Vistas.borrarPantalla(ventana)
        label_titulo=Label(ventana, text=".::Menu principal::.", justify="center") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        boton_registro=Button(ventana, text="1.-Registro", justify="center", command=lambda: Vistas.registro(ventana))
        boton_registro.pack(pady=5)
        boton_registro.config()

        boton_login=Button(ventana, text="2.-Login", justify="center", command=lambda: Vistas.login(ventana))
        boton_login.pack(pady=5)
        boton_login.config()

        boton_salir=Button(ventana, text="3.-Salir", justify="center")
        boton_salir.pack(pady=5)
        boton_salir.config()
   
    @staticmethod
    def registro(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Registro en el Sistema::.", justify="center")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_nombre=Label(ventana, text="¿Cual es tu nombre?:", justify="center")
        lbl_nombre.pack(pady=5)
        lbl_nombre.config()
        entry_nombre=Entry(ventana, width=30, justify="center")
        entry_nombre.pack(pady=5)

        lbl_apellidos=Label(ventana, text="¿Cuales son tus apellidos?:", justify="center")
        lbl_apellidos.pack(pady=5)
        lbl_apellidos.config()
        entry_apellidos=Entry(ventana, width=30, justify="center")
        entry_apellidos.pack(pady=5)

        lbl_email=Label(ventana, text="Ingresa tu email:", justify="center")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30, justify="center")
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:", justify="center")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30, show="*", justify="center")
        entry_contrasena.pack(pady=5)

        boton_registrar=Button(
            ventana,
            text="Registrar",
            justify="center",
            command=lambda: controlador.Controlador.registrar(
                entry_nombre.get(),
                entry_apellidos.get(),
                entry_email.get(),
                entry_contrasena.get()
            )
        )
        boton_registrar.pack(pady=5)
        boton_registrar.config()

        boton_volver=Button(ventana, text="Volver", justify="center", command=lambda: Vistas.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

    @staticmethod
    def login(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Inicio de Sesión::.", justify="center")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_email=Label(ventana, text="Ingresa tu E-mail:", justify="center")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30, justify="center")
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:", justify="center")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30, show="*", justify="center")
        entry_contrasena.pack(pady=5)

        boton_entrar=Button(ventana, text="Entrar", justify="center", command=lambda: (controlador.Controlador.login(
            entry_email.get(),
            entry_contrasena.get(),
            ventana
            )
        ))
        boton_entrar.pack(pady=5)
        boton_entrar.config()

        boton_volver=Button(ventana, text="Volver", justify="center", command=lambda: Vistas.menu_principal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        Vistas.borrarPantalla(ventana)

        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        label_titulo=Label(ventana, text=f".::Bienvenido {nom_user} {ape_user}, has iniciado sesión::.", justify="center") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        boton_crear=Button(ventana, text="1.-Crear", justify="center", command=lambda: Vistas.crear_nota(ventana))
        boton_crear.pack(pady=5)
        boton_crear.config()

        boton_mostrar=Button(ventana, text="2.-Mostrar", justify="center", command=lambda: Vistas.mostrar_nota(ventana))
        boton_mostrar.pack(pady=5)
        boton_mostrar.config()

        boton_cambiar=Button(ventana, text="3.-Cambiar", justify="center", command=lambda: Vistas.cambiar_nota(ventana))
        boton_cambiar.pack(pady=5)
        boton_cambiar.config()

        boton_eliminar=Button(ventana, text="4.-Eliminar", justify="center", command=lambda: Vistas.borrar_nota(ventana))
        boton_eliminar.pack(pady=5)
        boton_eliminar.config()

        boton_regresar=Button(ventana, text="5.-Regresar", justify="center", command=lambda: Vistas.login(ventana))
        boton_regresar.pack(pady=5)
        boton_regresar.config()

    @staticmethod
    def crear_nota(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_titulo1=Label(ventana, text=".::Crear Nota::.", justify="center")
        lbl_titulo1.pack(pady=5)
        lbl_titulo1.config()
        
        lbl_titulo2=Label(ventana, text="Titulo:", justify="center")
        lbl_titulo2.pack(pady=5)
        lbl_titulo2.config()
        entry_titulo2=Entry(ventana, width=30, justify="center")
        entry_titulo2.pack(pady=5)

        lbl_descripcion=Label(ventana, text="Descripción:", justify="center")
        lbl_descripcion.pack(pady=5)
        lbl_descripcion.config()
        entry_descripcion=Entry(ventana, width=30, justify="center")
        entry_descripcion.pack(pady=5)

        boton_guardar=Button(ventana, text="Guardar", justify="center", command=lambda: controlador.Controlador.crear_nota(
            id_user,
            entry_titulo2.get(),
            entry_descripcion.get()
        ))
        boton_guardar.pack(pady=5)
        boton_guardar.config()

        boton_volver=Button(ventana, text="Volver", justify="center", command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        boton_volver.pack(pady=5)
        boton_volver.config()

    @staticmethod
    def mostrar_nota(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"{nom_user} {ape_user}, tus notas son:", justify="center")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()

        filas=""
        registros=controlador.Controlador.mostrar_nota(id_user)
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas = filas + f"Nota: {num_notas}\nID: {fila[0]} Titulo: {fila[2]} Fecha de creación: {fila[4]}\nDescripción: {fila[3]}\n\n"
                num_notas+=1
            label_result = Label(ventana, text=filas.strip(), justify="center", wraplength=450)
            label_result.pack(pady=5)
        else:
            messagebox.showinfo(icon="info",message="...:: No existen notas para este usuario ::.")
            return


        boton_volver=Button(ventana, text="Volver", justify="center", command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        boton_volver.pack(pady=5)
        boton_volver.config()
    
    @staticmethod
    def cambiar_nota(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_titulo1=Label(ventana, text=f".::{nom_user} {ape_user} Vamos a modificar una nota::.", justify="center")
        lbl_titulo1.pack(pady=5)
        lbl_titulo1.config()
        
        lbl_id=Label(ventana, text="ID de la Nota a cambiar:", justify="center")
        lbl_id.pack(pady=5)
        lbl_id.config()
        entry_id=Entry(ventana, width=30, justify="center")
        entry_id.pack(pady=5)

        lbl_titulo2=Label(ventana, text="Nuevo Titulo:", justify="center")
        lbl_titulo2.pack(pady=5)
        lbl_titulo2.config()
        entry_titulo2=Entry(ventana, width=30, justify="center")
        entry_titulo2.pack(pady=5)

        lbl_descripcion=Label(ventana, text="Nueva Descripción:", justify="center")
        lbl_descripcion.pack(pady=5)
        lbl_descripcion.config()
        entry_descripcion=Entry(ventana, width=30, justify="center")
        entry_descripcion.pack(pady=5)

        boton_guardar=Button(ventana, text="Guardar", justify="center", command=lambda: controlador.Controlador.cambiar_nota(
            entry_id.get(),
            entry_titulo2.get(),
            entry_descripcion.get()))
        boton_guardar.pack(pady=5)
        boton_guardar.config()

        boton_volver=Button(ventana, text="Volver", justify="center", command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        boton_volver.pack(pady=5)
        boton_volver.config()

    @staticmethod
    def borrar_nota(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_titulo1=Label(ventana, text=f".::{nom_user} {ape_user} Vamos a eliminar una nota::.", justify="center")
        lbl_titulo1.pack(pady=5)
        lbl_titulo1.config()
        
        lbl_id=Label(ventana, text="ID de la Nota a eliminar:", justify="center")
        lbl_id.pack(pady=5)
        lbl_id.config()
        entry_id=Entry(ventana, width=30, justify="center")
        entry_id.pack(pady=5)

        boton_eliminar=Button(ventana, text="Eliminar", justify="center", command=lambda: controlador.Controlador.eliminar_nota(entry_id.get()))
        boton_eliminar.pack(pady=5)
        boton_eliminar.config()

        boton_volver=Button(ventana, text="Volver", justify="center", command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        boton_volver.pack(pady=5)
        boton_volver.config()