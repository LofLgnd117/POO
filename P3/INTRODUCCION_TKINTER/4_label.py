from tkinter import *

ventana = Tk()
ventana.title("Etiquetas")
ventana.geometry("600x400")


marco1 = Frame(ventana, width=600, height=100, bg="#FFA51D", relief=RAISED, border=2)
marco1.pack()
marco1.pack_propagate(False)

marco2 = Frame(ventana, width=600, height=100, bg="#D6622C", relief=RAISED, border=2)
marco2.pack()
marco2.pack_propagate(False)

marco3 = Frame(ventana, width=600, height=100, bg="#97451F", relief=RAISED, border=2)
marco3.pack()
marco3.pack_propagate(False)

marco4 = Frame(ventana, width=600, height=100, bg="#FF704C", relief=RAISED, border=2)
marco4.pack()
marco4.pack_propagate(False)

#Etiquetas o Labels
etiqueta1 = Label(marco1, text="Leonardo Javier Flores Verdin",bg="#FF704C").pack(pady=30)
etiqueta2 = Label(marco2, text="Universidad Tecnologica de Durango",bg="#97451F").pack(pady=30)
etiqueta3 = Label(marco3, text="Tecnologias de la Informacion",bg="#D6622C").pack(pady=30)
etiqueta4 = Label(marco4, text="Desarrollo de SW Multiplataforma",bg="#FFA51D").pack(pady=30)


ventana.mainloop()