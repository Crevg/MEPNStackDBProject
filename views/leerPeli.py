from tkinter import ttk
from tkinter import *
import colors
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor



def leerPeliWindow(root):
    #ventana principal
    frameLeerPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameLeerNombre = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerGenero = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerFranquicia = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerPais = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerAnno = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerActores = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerProductoras = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerPeliBotones = Frame(frameLeerPeli, bg = backgroundColor[0])
    #labels
    labelLeerPeli = Label(frameLeerPeli, text = "Consultar Información de Películas", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerNombre = Label(frameLeerNombre, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerGenero = Label(frameLeerGenero, text= "Género", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerFranquicia = Label(frameLeerFranquicia, text= "Franquicia", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerPais = Label(frameLeerPais, text= "País", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerAnno = Label(frameLeerAnno, text= "Año", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerActores = Label(frameLeerActores, text= "Actores (separados por coma)", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerProductoras = Label(frameLeerProductoras, text= "Compañia Productora", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys

 
    listaProductoras = ["ab" , "bb", "cb"] 
    comboboxLeerNombre = ttk.Combobox(frameLeerNombre, width = 40, font= ("Arial Bold", 15), state = "readonly")
    entryLeerGenero = Entry(frameLeerGenero, width = 40, font= ("Arial Bold", 15), state = "readonly")
    entryLeerFranquicia = Entry(frameLeerFranquicia, width = 40, font= ("Arial Bold", 15), state = "readonly")
    entryLeerPais= Entry(frameLeerPais, width = 40, font= ("Arial Bold", 15), state = "readonly")
    entryLeerAnno = Entry(frameLeerAnno, width = 40, font= ("Arial Bold", 15), state = "readonly")
    entryLeerActores = Entry(frameLeerActores, width = 40, font= ("Arial Bold", 15), state = "readonly")
    entryLeerProductoras = Entry(frameLeerProductoras, width = 40, font= ("Arial Bold", 15),  state= "readonly")


    #funciones

    def volver():
        frameLeerPeli.pack_forget()
        return    
    #botones

    botonVolverLeerPeli = Button(frameLeerPeliBotones, text="Volver" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= volver)

    #packs
    frameLeerPeli.pack(fill = BOTH)
    labelLeerPeli.pack()
    frameLeerNombre.pack(fill = X)
    frameLeerGenero.pack(fill = X)
    frameLeerFranquicia.pack(fill = X)
    frameLeerPais.pack(fill = X)
    frameLeerAnno.pack(fill = X)
    frameLeerActores.pack(fill = X)
    frameLeerProductoras.pack(fill = X, pady = 10)
    frameLeerPeliBotones.pack(fill=X)

    labelLeerNombre.pack()
    labelLeerGenero.pack()
    labelLeerFranquicia.pack()
    labelLeerPais.pack()
    labelLeerAnno.pack()
    labelLeerActores.pack()
    labelLeerProductoras.pack()

    comboboxLeerNombre.pack()
    entryLeerGenero.pack()
    entryLeerFranquicia.pack()
    entryLeerPais.pack()
    entryLeerAnno.pack()
    entryLeerActores.pack()
    entryLeerProductoras.pack()

    botonVolverLeerPeli.pack(side = TOP)


