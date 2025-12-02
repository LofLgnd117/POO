from tkinter import messagebox

#Controlador
def operaciones(operacion, numero1, numero2):
    try:
        if operacion == "suma":
            resultado = numero1 + numero2
            simbolo = "+"
            titulo = "Suma"
        elif operacion == "resta":
            resultado = numero1 - numero2
            simbolo = "-"
            titulo = "Resta"
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
            simbolo = "x"
            titulo = "Multiplicación"
        elif operacion == "division":
            if numero2 == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return
            resultado = numero1 / numero2
            simbolo = "/"
            titulo = "División"
        else:
            messagebox.showerror("Error", f"Operación desconocida: {operacion}")
            return

        messagebox.showinfo(icon="info", title=titulo, message=f"{numero1} {simbolo} {numero2} = {resultado}")
    except Exception as e:
        messagebox.showerror(f"Ocurrió el siguiente error: {e}")