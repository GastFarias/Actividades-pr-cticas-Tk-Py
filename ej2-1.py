from tkinter import *


#region elementos
ventana = Tk()
ventana.geometry("250x200")
ventana.resizable(False,False)

labelNro1 = Label(ventana,text="Primer numero")
labelNro1.grid(column=0,row= 0)

labelNro2 = Label(ventana, text="Segundo numero")
labelNro2.grid(column=0 , row= 1)

labelResultado = Label(ventana, text="Resultado")
labelResultado.grid(column=0,row=2)

nro1 = StringVar(ventana, "")
entryNro1 = Entry(ventana, textvariable= nro1)
entryNro1.grid(column=1,row= 0)

nro2 = StringVar(ventana,"")
entryNro2 = Entry(ventana, textvariable=nro2)
entryNro2.grid(column=1,row=1)

resultado = StringVar(ventana,"")
entryResultado = Entry(ventana, textvariable = resultado, state="readonly")
entryResultado.grid(column = 1, row = 2)

botonMas = Button(ventana, text= "+", command= lambda: Sumar(), width=10)
botonMas.grid(column=0,row=3)

botonMenos = Button(ventana,text="-", command= lambda: Restar(), width=10)
botonMenos.grid(column=1, row=3)

botonMultiplicar = Button(ventana, text="x", command=lambda: Multiplicar(), width=10)
botonMultiplicar.grid(column=0, row=4)

botonDividir = Button(ventana, text= "/", command= lambda: Dividir(), width=10)
botonDividir.grid(column=1, row= 4)

botonPorcentaje = Button(ventana, text="%", command= lambda: Porcentaje(), width=10)
botonPorcentaje.grid(column=0, row=5)

botonNuevo = Button(ventana,text= "Nuevo", command= lambda: Nuevo(), width=10)
botonNuevo.grid(column=1, row=5)

#endregion

#region funciones
def checkCampos():
    val = 0
    try:
        float(nro1.get())
        val += 1
    except:
        nro1.set(" # # ERROR # # ")

    try:
        float(nro2.get())
        val += 1
    except:
        nro2.set(" # # ERROR # # ")
    
    return val == 2


def Sumar():
    if checkCampos() == True:
        resultado.set(str(float(nro1.get()) + float(nro2.get())))
    else:
        pass

def Restar():
    if checkCampos() == True:
        resultado.set(str(float(nro1.get()) - float(nro2.get())))
    else: 
        pass

def Multiplicar():
    if checkCampos() == True:
        resultado.set(str(float(nro1.get()) * float(nro2.get())))
    else: 
        pass    

def Dividir():
    if checkCampos() == True:
        if float(nro2.get()) != 0:
            resultado.set(str(float(nro1.get()) / float(nro2.get())))
        else:
            nro2.set("# Error Division por 0 #")
    else: 
        pass

def Porcentaje():
    if checkCampos() == True:
        resultado.set(str(float(nro1.get()) * float(nro2.get()) / 100 ))
    else:
        pass

def Nuevo():
    nro1.set("")
    nro2.set("")
    resultado.set("")
#endregion

####################################
ventana.mainloop()