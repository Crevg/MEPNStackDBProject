from tkinter import ttk
from tkinter import *
import colors
import requests

#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor

#requests

def cargarProductoras():
    res = requests.get("http://localhost:3000/productoras/readAll")
    if res.status_code == requests.codes.ok:
        return res.json()
    else:
        return [[]]


def actualizarPeliWindow(root):
    #ventana principal
    frameActualizarPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameActualizarNombre = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarGenero = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarFranquicia = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarPais = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarAnno = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarActores = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarProductoras = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarPeliBotones = Frame(frameActualizarPeli, bg = backgroundColor[0])
    #labels
    labelActualizarPeli = Label(frameActualizarPeli, text = "Actualizar Película", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarNombre = Label(frameActualizarNombre, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarGenero = Label(frameActualizarGenero, text= "Género", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarFranquicia = Label(frameActualizarFranquicia, text= "Franquicia", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarPais = Label(frameActualizarPais, text= "País", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarAnno = Label(frameActualizarAnno, text= "Año", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarActores = Label(frameActualizarActores, text= "Actores (separados por coma)", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarProductoras = Label(frameActualizarProductoras, text= "Compañia Productora", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])

    #funciones

    def cancelar():
        frameActualizarPeli.pack_forget()
        return    

    def actualizar():
        #FALTA LÓGICA DE Actualizar
        frameActualizarPeli.pack_forget()
        return  


    #entrys

    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return cancelar()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servir, por favor intentelo más tarde.")
        return cancelar()

    listaProductoras = colors.getListaNombres(productoras)
    comboboxActualizarNombre = ttk.Combobox(frameActualizarNombre, width = 40, font= ("Arial Bold", 15),  state= "readonly")
    comboboxActualizarNombre["values"] = listaNombres
    entryActualizarGenero = Entry(frameActualizarGenero, width = 40, font= ("Arial Bold", 15))
    entryActualizarFranquicia = Entry(frameActualizarFranquicia, width = 40, font= ("Arial Bold", 15))
    entryActualizarPais= Entry(frameActualizarPais, width = 40, font= ("Arial Bold", 15))
    entryActualizarAnno = Entry(frameActualizarAnno, width = 40, font= ("Arial Bold", 15))
    entryActualizarActores = Entry(frameActualizarActores, width = 40, font= ("Arial Bold", 15))
    comboboxActualizarProductoras = ttk.Combobox(frameActualizarProductoras, width = 40, font= ("Arial Bold", 15),  state= "readonly")
    comboboxActualizarProductoras["values"] = listaProductoras

  
    botonAceptarActualizarPeli = Button(frameActualizarPeliBotones, text="Actualizar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= actualizar)
    botonCancelarActualizarPeli = Button(frameActualizarPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= cancelar)

    #packs
    frameActualizarPeli.pack(fill = BOTH)
    labelActualizarPeli.pack()
    frameActualizarNombre.pack(fill = X)
    frameActualizarGenero.pack(fill = X)
    frameActualizarFranquicia.pack(fill = X)
    frameActualizarPais.pack(fill = X)
    frameActualizarAnno.pack(fill = X)
    frameActualizarActores.pack(fill = X)
    frameActualizarProductoras.pack(fill = X, pady = 10)
    frameActualizarPeliBotones.pack(fill=X)

    labelActualizarNombre.pack()
    labelActualizarGenero.pack()
    labelActualizarFranquicia.pack()
    labelActualizarPais.pack()
    labelActualizarAnno.pack()
    labelActualizarActores.pack()
    labelActualizarProductoras.pack()

    comboboxActualizarNombre.pack()
    entryActualizarGenero.pack()
    entryActualizarFranquicia.pack()
    entryActualizarPais.pack()
    entryActualizarAnno.pack()
    entryActualizarActores.pack()
    comboboxActualizarProductoras.pack()

    botonCancelarActualizarPeli.pack(side= RIGHT, padx = 100)
    botonAceptarActualizarPeli.pack(side = RIGHT, padx = 100)


