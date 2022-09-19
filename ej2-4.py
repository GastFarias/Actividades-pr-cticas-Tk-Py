from ctypes import alignment
import tkinter as Tk

ventana = Tk.Tk()
ventana.geometry("280x160")
ventana.resizable(False,False)

labelValor1 = Tk.Label(ventana,text="Valor 1")
labelValor1.grid(column=0, row=0)

labelValor2 = Tk.Label(ventana, text= "Valor 2")
labelValor2.grid(column=0, row=1)

labelResultado = Tk.Label(ventana,text="Resultado")
labelResultado.grid(column=0, row = 2)

nro1 = Tk.StringVar(ventana,"")
entryNro1 = Tk.Entry(ventana, textvariable= nro1)
entryNro1.grid(column=1, row=0)

nro2 = Tk.StringVar(ventana,"")
entryNro2 = Tk.Entry(ventana, textvariable= nro2)
entryNro2.grid(column=1, row=1)

resultado = Tk.StringVar(ventana, "")
entryResultado = Tk.Entry(ventana,textvariable= resultado)
entryResultado.grid(column=1, row=2)

seleccion = Tk.IntVar()
radioSumar = Tk.Radiobutton(ventana, text="Sumar", variable= seleccion, value=0)
radioSumar.grid(column=2,row=0)

radioRestar = Tk.Radiobutton(ventana, text="Restar", variable= seleccion, value=1)
radioRestar.grid(column=2,row=1)

radioMultiplicar = Tk.Radiobutton(ventana, text="Multiplicar", variable= seleccion, value=2)
radioMultiplicar.grid(column=2,row=2)

radioDividir = Tk.Radiobutton(ventana, text="Dividir", variable= seleccion, value=3)
radioDividir.grid(column=2,row=3)

boton = Tk.Button(ventana, text="Calcular", command=lambda: Calcular())
boton.grid(column=1, row=4)

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

def Calcular():
    if checkCampos() == True:
        if seleccion.get() == 0:
            resultado.set(str(float(nro1.get()) + float(nro2.get())))
        elif seleccion.get() == 1:
            resultado.set(str(float(nro1.get()) - float(nro2.get())))
        elif seleccion.get() == 2:
            resultado.set(str(float(nro1.get()) * float(nro2.get())))
        elif seleccion.get() == 3:
            if float(nro2.get()) != 0:
                resultado.set(str(float(nro1.get()) / float(nro2.get())))
            else:
                nro2.set("# Error Division por 0 #")
                resultado.set("")





ventana.mainloop()