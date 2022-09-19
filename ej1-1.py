from tkinter import * 


ventana = Tk()
ventana.title("ContCreciente")
ventana.geometry("250x125")
ventana.grid()
ventana.wm_resizable(False,False)


label = Label(ventana, text="Contador", justify= CENTER)
label.grid(column=0 ,row= 0, pady= "30px")

var = StringVar(ventana,"0")
entry = Entry(ventana,state="readonly", textvariable= var)
entry.grid(column=1, row = 0,pady="30px")

boton = Button(ventana, text= "+", command=lambda: sumar())
boton.grid(column=2,row=0, pady="30px")


def sumar():
    cont = int(var.get())
    cont += 1
    var.set(int(cont))
    
ventana.mainloop()