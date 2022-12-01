from tkinter import *
alto = 400
ancho = 400
columna = 0
fila = 0
root = Tk()

for i in range(5):
    Canvas(width=100, height=100, bg="green").grid(row=fila, column=columna)
    Label(text="2").grid(row=fila, column=columna)
    fila += 1
    columna += 1
    
root.mainloop()
