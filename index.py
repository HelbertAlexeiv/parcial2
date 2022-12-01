from tkinter import *

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
    for i in range(int(ordenEntry.get())):
        Canvas(matrizFrame, width=100, height=100, bg=color).grid(row=fila, column=columna)
        Label(matrizFrame, text="2").grid(row=fila, column=columna)
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
