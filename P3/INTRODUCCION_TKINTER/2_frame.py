from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Marcos o Frame en Tkinter")



marco1=Frame(ventana, width=400, height=200, bg="blue", relief=SOLID, border=2)
marco1.pack_propagate(False)
marco1.pack(pady=200) 


marco2=Frame(marco1, width=300, height=150, bg="silver", relief=GROOVE, border=10)
marco2.pack(pady=50)

ventana.mainloop()