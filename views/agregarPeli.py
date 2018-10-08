from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import colors
import requests

#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor

#requests

def cargarProductoras():
    try:
        res = colors.leerProductoras()

        if res.status_code == requests.codes.ok:
            return res.json()
        else:
            return [[]]
    except requests.exceptions.ConnectionError:
        return [[]]

def agregarPeliWindow(root):
    #ventana principal
    frameAgregarPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameAgregarNombre = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarGenero = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarFranquicia = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarPais = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarAnno = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarActores = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarProductoras = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarPeliBotones = Frame(frameAgregarPeli, bg = backgroundColor[0])
    #labels
    labelAgregarPeli = Label(frameAgregarPeli, text = "Agregar Nueva Película", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarNombre = Label(frameAgregarNombre, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarGenero = Label(frameAgregarGenero, text= "Género", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarFranquicia = Label(frameAgregarFranquicia, text= "Franquicia", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarPais = Label(frameAgregarPais, text= "País", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarAnno = Label(frameAgregarAnno, text= "Año", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarActores = Label(frameAgregarActores, text= "Actores (separados por coma)", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarProductoras = Label(frameAgregarProductoras, text= "Compañia Productora", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])

   #funciones

    def cancelar():
        frameAgregarPeli.pack_forget()
        return    

    def agregar():
        #FALTA LÓGICA DE AGREGAR
        frameAgregarPeli.pack_forget()
        return  


    #entrys

 
    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return cancelar()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
        return cancelar()
    listaProductoras = colors.getListaNombres(productoras)


    entryAgregarNombre = Entry(frameAgregarNombre, width = 40, font= ("Arial Bold", 15))
    entryAgregarGenero = Entry(frameAgregarGenero, width = 40, font= ("Arial Bold", 15))
    entryAgregarFranquicia = Entry(frameAgregarFranquicia, width = 40, font= ("Arial Bold", 15))
    entryAgregarPais= Entry(frameAgregarPais, width = 40, font= ("Arial Bold", 15))
    entryAgregarAnno = Entry(frameAgregarAnno, width = 40, font= ("Arial Bold", 15))
    entryAgregarActores = Entry(frameAgregarActores, width = 40, font= ("Arial Bold", 15))
    comboboxAgregarProductoras = ttk.Combobox(frameAgregarProductoras, width = 40, font= ("Arial Bold", 15),  state= "readonly")
    comboboxAgregarProductoras["values"] = listaProductoras


 
    #botones

    botonAceptarAgregarPeli = Button(frameAgregarPeliBotones, text="Agregar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= agregar)
    botonCancelarAgregarPeli = Button(frameAgregarPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= cancelar)

    #packs
    frameAgregarPeli.pack(fill = BOTH)
    labelAgregarPeli.pack()
    frameAgregarNombre.pack(fill = X)
    frameAgregarGenero.pack(fill = X)
    frameAgregarFranquicia.pack(fill = X)
    frameAgregarPais.pack(fill = X)
    frameAgregarAnno.pack(fill = X)
    frameAgregarActores.pack(fill = X)
    frameAgregarProductoras.pack(fill = X, pady = 10)
    frameAgregarPeliBotones.pack(fill=X)

    labelAgregarNombre.pack()
    labelAgregarGenero.pack()
    labelAgregarFranquicia.pack()
    labelAgregarPais.pack()
    labelAgregarAnno.pack()
    labelAgregarActores.pack()
    labelAgregarProductoras.pack()

    entryAgregarNombre.pack()
    entryAgregarGenero.pack()
    entryAgregarFranquicia.pack()
    entryAgregarPais.pack()
    entryAgregarAnno.pack()
    entryAgregarActores.pack()
    comboboxAgregarProductoras.pack()

    botonCancelarAgregarPeli.pack(side= RIGHT, padx = 100)
    botonAceptarAgregarPeli.pack(side = RIGHT, padx = 100)


