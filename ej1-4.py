from cProfile import label
from cgitb import reset
from tkinter import *
from tokenize import String

ventana = Tk()
ventana.geometry("500x80")
ventana.resizable(False,False)

label = Label(ventana,text="")
label.grid(column=0 , row=0)

labelContador = Label(ventana, text="Coontador")
labelContador.grid(column=0, row=1, padx=5)

Nro = StringVar(ventana,"0")
entryNro = Entry(ventana, textvariable= Nro, state="readonly")
entryNro.grid(column=1,row=1,padx=5)

botonSiguiente = Button(ventana,text="Siguiente",command= lambda: Siguiente(), width=10)
botonSiguiente.grid(column=2,row=1,padx=5)

botonAnterior = Button(ventana,text="Anterior", command= lambda: Anterior(), width=10)
botonAnterior.grid(column=3, row=1,padx=5)

botonReset = Button(ventana, text="Reset", command= lambda: Reset(), width=10)
botonReset.grid(column=4, row=1,padx=5)

def Siguiente():
    Nro.set(str(int(Nro.get()) + 1))

def Anterior():
    Nro.set(str(int(Nro.get()) - 1))

def Reset():
    Nro.set("0")

    
################################################
ventana.mainloop()
