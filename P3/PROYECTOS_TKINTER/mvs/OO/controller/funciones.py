from tkinter import messagebox
from model import operaciones

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
                operaciones.Operaciones.insertar(numero1, numero2, signo, resultado)
            #messagebox.showinfo(icon="info", title=titulo, message=f"{numero1} {signo} {numero2} = {resultado}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió el siguiente error: {e}")