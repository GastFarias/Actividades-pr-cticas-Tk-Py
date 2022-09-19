
import random
from tkinter import *

ventana = Tk()
ventana.geometry("250x250")

labelNro1 = Label(ventana, text= "Numero 1")
labelNro1.grid(column=0, row=0)

labelNro2 = Label(ventana, text= "Numero 2")
labelNro2.grid(column=0, row=1)

labelGenerado = Label(ventana, text= "Numero Generado")
labelGenerado.grid(column=0, row= 2)

nro1 = Spinbox(ventana, from_= 0, to= 100,state="readonly")
nro1.grid(column=1, row = 0)

nro2 = Spinbox(ventana, from_= 0, to= 100, state="readonly")
nro2.grid(column= 1, row=1)

gen = StringVar(ventana, "")
nroGenerado = Entry(ventana, textvariable= gen, state= "readonly")
nroGenerado.grid(column=1, row=2)

botonGenerar = Button(ventana, text= "Generar", command= lambda: Generar())
botonGenerar.grid(column=1, row= 3)

#######################

def Generar():
    var1 = int(nro1.get())
    var2 = int(nro2.get())
    if var1 >= var2:
        gen.set(str(random.randint(var2,var1 )))
    else:
        gen.set(str(random.randint(var1, var2 )))



#######################
ventana.mainloop()