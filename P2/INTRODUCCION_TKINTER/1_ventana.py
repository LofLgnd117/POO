"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear
aplicaciones en python para escritorio
"""
from tkinter import *

ventana = Tk() # Crear una ventana
ventana.title("Mi primer App con Tkinter") #Titulo de la ventana
ventana.geometry("800x600") #Tamaño de la ventana

ventana.mainloop() #Metodo que mantiene la ventana abierta todo el tiempo que dure la aplicacion activa