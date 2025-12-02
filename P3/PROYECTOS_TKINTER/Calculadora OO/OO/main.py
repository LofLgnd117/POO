"""
Crear una calculadora:
1.- Dos campos de texto
2.- Cuatro botones para las Operaciones
3.- Mostrar el resultado en una alerta
4.- Programacion Estructurada
5.- Implementar el MVC
"""
from view import interfaz
from tkinter import Tk

def main():
    root = Tk()
    app = interfaz.Vistas(root) # Instanciamos la clase Vistas pasando la ventana raíz
    root.mainloop()

if __name__ == "__main__":
    main() 