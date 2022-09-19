from tkinter import *

ventana = Tk()
ventana.title("ContDecreciente")
ventana.wm_resizable(False,False)

label = Label(ventana, text = "Contador", justify= CENTER)
label.grid(column= 0, row= 0, padx=25, pady=25)

var = StringVar(ventana, str(88))
entry = Entry(ventana, state= "readonly", textvariable= var )
entry.grid(column=1, row= 0, pady=25)

boton = Button(ventana, text= "     -     ", command= lambda: restar())
boton.grid(column=2, row= 0,padx=25, pady=25)

def restar():
    nro = int(var.get())
    nro -= 1 
    var.set(str(nro))

ventana.mainloop()