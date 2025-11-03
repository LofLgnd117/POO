from tkinter import *

ventana = Tk()
ventana.title("Uso del mainloop")
ventana.geometry("600x400")

marco1 = Frame(ventana, width=600, height=50, bg="#FB2C08", relief=RAISED, border=2)
marco1.pack()

marco2 = Frame(ventana, width=600, height=50, bg="#FF8800", relief=RAISED, border=2)
marco2.pack()

marco3 = Frame(ventana, width=600, height=50, bg="#FBF308", relief=RAISED, border=2)
marco3.pack()

marco4 = Frame(ventana, width=600, height=50, bg="#4DFB08", relief=RAISED, border=2)
marco4.pack()

marco5 = Frame(ventana, width=600, height=50, bg="#08A2FB", relief=RAISED, border=2)
marco5.pack()

marco6 = Frame(ventana, width=600, height=50, bg="#EB08FB", relief=RAISED, border=2)
marco6.pack()

ventana.mainloop()