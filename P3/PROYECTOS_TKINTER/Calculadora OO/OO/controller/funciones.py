from tkinter import messagebox
from model import operaciones
from view import interfaz
#Controlador

class Controladores:

    @staticmethod
    def operaciones(titulo, numero1, numero2, signo):
        try:
            if signo == "+":
                resultado = numero1 + numero2
            elif signo == "-":
                resultado = numero1 - numero2
            elif signo == "x":
                resultado = numero1 * numero2
            elif signo == "/":
                if numero2 == 0:
                    messagebox.showerror("Error", "No se puede dividir por cero")
                    return
                resultado = numero1 / numero2
            else:
                messagebox.showerror("Error", f"Operación desconocida: {signo}")
                return
            result=messagebox.askquestion( message=f"{numero1} {signo} {numero2} = {resultado}\n ¿Quires guardar la operación en la BD?",icon="question")
            if result =="yes":
                respuesta=operaciones.Operaciones.insertar(numero1, numero2, signo, resultado)
                Controladores.respuesta_sql("Agregar registro",respuesta)
        #messagebox.showinfo(icon="info", title=titulo, message=f"{numero1} {signo} {numero2} = {resultado}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió el siguiente error: {e}")

    @staticmethod
    def consultar():
        registros = operaciones.Operaciones.mostrar()
        return registros

    @staticmethod
    def cambiar(num1, num2, signo, resultado, id):
        respuesta = operaciones.Operaciones.actualizar(num1, num2, signo, resultado, id)
        Controladores.respuesta_sql("Cambiar registro", respuesta)

    @staticmethod
    def buscar(ventana,id):
        respuesta = operaciones.Operaciones.buscar(id)
    
    @staticmethod
    def eliminar(id):
        respuesta = operaciones.Operaciones.eliminar(id)
        Controladores.respuesta_sql("Borrar registro", respuesta)

    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo, message="¡Acción realizada con éxito!")
        else:
            messagebox.showinfo(title=titulo, message="No fue posible realizar la acción, vuelva a intentar")