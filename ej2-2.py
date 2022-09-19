from argparse import _VersionAction
from msilib.schema import ListBox
from tkinter import *
import tkinter

ventana = Tk()
ventana.geometry("300x250")

labelTitulo = Label(ventana, text="Escribe el titula de la pelicula")
labelTitulo.grid(column=0, row=0)

labelLista = Label(ventana,text="Peliculas")
labelLista.grid(column= 1, row=0)

varTitulo = StringVar(ventana, "")
entryTitulo = Entry(ventana, textvariable= varTitulo)
entryTitulo.grid(column=0, row=1)

lista = Listbox(ventana)
lista.grid(column=1, row= 1)

boton = Button(ventana, text="Añadir", command= lambda: añadir())
boton.grid(column=0, row=2)

def añadir():
    if str(varTitulo.get()).strip() != "":
        lista.insert(END, varTitulo.get())
        varTitulo.set("")
    else: 
        varTitulo.set("")

ventana.mainloop()