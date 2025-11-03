from tkinter import *

ventana = Tk()
ventana.title("Etiquetas")
ventana.geometry("600x400")


marco1 = Frame(ventana, width=600, height=100, bg="#FB3908", relief=RAISED, border=2)
marco1.pack()
marco1.pack_propagate(False)

marco2 = Frame(ventana, width=600, height=100, bg="#08FBEF", relief=RAISED, border=2)
marco2.pack()
marco2.pack_propagate(False)

marco3 = Frame(ventana, width=600, height=100, bg="#08FB10", relief=RAISED, border=2)
marco3.pack()
marco3.pack_propagate(False)

marco4 = Frame(ventana, width=600, height=100, bg="#BA08FB", relief=RAISED, border=2)
marco4.pack()
marco4.pack_propagate(False)

#Etiquetas o Labels
etiqueta1 = Label(marco1, text="David Israel García Páez",bg="#FB3908").pack(pady=30)
etiqueta2 = Label(marco2, text="Universidad Tecnologica de Durango",bg="#08FBEF").pack(pady=30)
etiqueta3 = Label(marco3, text="Tecnologias de la Informacion",bg="#08FB10").pack(pady=30)
etiqueta4 = Label(marco4, text="Desarrollo de SW Multiplataforma",bg="#BA08FB").pack(pady=30)


ventana.mainloop()