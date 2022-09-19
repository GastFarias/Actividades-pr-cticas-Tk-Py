from tkinter import * 
import math
ventana = Tk()
ventana.geometry("250x125")

labelNRo = Label(ventana, text="Nro: ")
labelNRo.grid(column=0,row=0)

varNro = StringVar(ventana, "1")
entryNro = Entry(ventana, textvariable= varNro)
entryNro.grid(column=1, row=0)

labelFactorial = Label(ventana, text= "Factorial: ")
labelFactorial.grid(column= 0, row= 1)

varFact = StringVar(ventana, "1")
entryFact = Entry(ventana, textvariable= varFact)
entryFact.grid(column= 1, row = 1)

boton = Button(ventana, text= "Aumentar", command= lambda: Aumentar())
boton.grid(column=1, row= 2)

def Aumentar():
    varNro.set(str(int(varNro.get())+1))
    varFact.set(str(math.factorial(int(varNro.get()))))


##################
ventana.mainloop()