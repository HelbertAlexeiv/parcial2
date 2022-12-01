from tkinter import *
from random import randint
root = Tk()
filaExterior = 0
columnaExterior= 0
root.config(width=400, height=400)
root.resizable(False, False)

#Frames
datosFrame = Frame(root)
matrizFrame = Frame(root)

def generarFila(fila, columna):
    columna = columna
    fila = fila
    color = "green"
    numeroAleatorio = randint(1, 5)
    for i in range(int(ordenEntry.get())):
        if int(buscarEntry.get()) == randint(1, 5):
            Canvas(matrizFrame, width=100, height=100, bg="red").grid(row=fila, column=columna)
        else:
            Canvas(matrizFrame, width=100, height=100, bg=color).grid(row=fila, column=columna)
        Label(matrizFrame, text=numeroAleatorio).grid(row=fila, column=columna)
        columna += 1

#funcion
def generarMatriz(fila = filaExterior, columna = columnaExterior):
    for i in range(int(ordenEntry.get())):
        generarFila(fila, 0)
        fila +=1
    
#Frame entrada de datos
orden = Label(datosFrame, text="Orden de la matriz:")
ordenEntry = Entry(datosFrame, width=10)

buscar = Label(datosFrame, text="Buscar")
buscarEntry = Entry(datosFrame, width=10)

botonEmpezar = Button(datosFrame, text="empezar", command=generarMatriz)

orden.grid(row=0, column=0)
ordenEntry.grid(row=0, column=1)

buscar.grid(row=0, column=2)
buscarEntry.grid(row=0, column=3)

botonEmpezar.grid(row=1, column=1)

#Empaquetado de frames
matrizFrame.pack()
datosFrame.pack()
root.mainloop()
