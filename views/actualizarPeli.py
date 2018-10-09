from tkinter import ttk
from tkinter import *
import colors
import requests

#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor

#requests

def cargarPeliculas():
    res = colors.leerPelicula()
    if res.status_code == requests.codes.ok:
        return res.json()
    else:
        return [[]]


def cargarProductoras():
    try:
        res = colors.leerProductoras()

        if res.status_code == requests.codes.ok:
            return res.json()
        else:
            return [[]]
    except requests.exceptions.ConnectionError:
        return [[]]



def actualizarPeliWindow(root):
    #ventana principal
    frameActualizarPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameActualizarNombre = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarGenero = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarDirector = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarFranquicia = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarPais = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarAnno = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarDuracion = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarActores = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarProductoras = Frame(frameActualizarPeli, bg = backgroundColor[0])
    frameActualizarPeliBotones = Frame(frameActualizarPeli, bg = backgroundColor[0])
    #labels
    labelActualizarPeli = Label(frameActualizarPeli, text = "Actualizar Película", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarNombre = Label(frameActualizarNombre, text= "Nombre", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarGenero = Label(frameActualizarGenero, text= "Director", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarDirector = Label(frameActualizarDirector, text= "Género", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarFranquicia = Label(frameActualizarFranquicia, text= "Franquicia", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarPais = Label(frameActualizarPais, text= "País", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarDuracion = Label(frameActualizarDuracion, text= "Duración (en minutos)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarAnno = Label(frameActualizarAnno, text= "Año", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarActores = Label(frameActualizarActores, text= "Actores (separados por coma)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarProductoras = Label(frameActualizarProductoras, text= "Compañia Productora", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])

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

    peliculas = cargarPeliculas()
    if peliculas == []:
        messagebox.showerror("Error", "No existen películas, por favor agregue una antes de continuar.")
        return cancelar()
    elif peliculas[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
        return cancelar()
    


    listaProductoras = colors.getListaNombres(productoras)
    listaPelis = colors.getListaNombres(peliculas)
    comboboxActualizarNombre = ttk.Combobox(frameActualizarNombre, width = 40, font= ("Arial Bold", 11),  state= "readonly")
    comboboxActualizarNombre["values"] = listaPelis
    entryActualizarGenero = Entry(frameActualizarGenero, width = 40, font= ("Arial Bold", 11))
    entryActualizarDirector = Entry(frameActualizarDirector, width = 40, font= ("Arial Bold", 11))
    entryActualizarFranquicia = Entry(frameActualizarFranquicia, width = 40, font= ("Arial Bold", 11))
    entryActualizarPais= Entry(frameActualizarPais, width = 40, font= ("Arial Bold", 11))
    entryActualizarAnno = Entry(frameActualizarAnno, width = 40, font= ("Arial Bold", 11))
    entryActualizarDuracion= Entry(frameActualizarDuracion, width = 40, font= ("Arial Bold", 11))
    entryActualizarActores = Entry(frameActualizarActores, width = 40, font= ("Arial Bold", 11))
    comboboxActualizarProductoras = ttk.Combobox(frameActualizarProductoras, width = 40, font= ("Arial Bold", 11),  state= "readonly")
    comboboxActualizarProductoras["values"] = listaProductoras
    comboboxActualizarProductoras.current(0)


    def cargarInfo(event):
        indice = 0
        for i in range (0, len(listaPelis)):
            if listaPelis[i] == comboboxActualizarNombre.get():
                indice = i
                break
        nombreProd = "Productora no encontrada"
        for i in range(0, len (productoras)):
            if productoras[i]["_id"] == peliculas[indice]["productora"]:
                comboboxActualizarProductoras.current(i)
                break
        
        actores = ""
        cantActores = len(peliculas[indice]["actores"])
        for i in range (0, cantActores):
            actores = actores + peliculas[indice]["actores"][i]
            if i + 1 < cantActores:
                actores = actores + ", "
            

        entryActualizarGenero.delete(0, END)
        entryActualizarDirector.delete(0, END)
        entryActualizarFranquicia.delete(0, END)
        entryActualizarPais.delete(0, END)
        entryActualizarAnno.delete(0, END)
        entryActualizarDuracion.delete(0, END)
        entryActualizarActores.delete(0, END)
        
        entryActualizarGenero.insert(0,peliculas[indice]["genero"])
        entryActualizarDirector.insert(0,peliculas[indice]["nombreDirector"])
        entryActualizarFranquicia.insert(0,peliculas[indice]["franquicia"])
        entryActualizarPais.insert(0,peliculas[indice]["pais"])
        entryActualizarAnno.insert(0,peliculas[indice]["anno"])
        entryActualizarDuracion.insert(0,peliculas[indice]["duracion"])
        entryActualizarActores.insert(0, actores)

       
    
    
    comboboxActualizarNombre.bind("<<ComboboxSelected>>", cargarInfo)



    botonAceptarActualizarPeli = Button(frameActualizarPeliBotones, text="Actualizar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= actualizar)
    botonCancelarActualizarPeli = Button(frameActualizarPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= cancelar)

    #packs
    frameActualizarPeli.pack(fill = BOTH)
    labelActualizarPeli.pack()
    frameActualizarNombre.pack(fill = X)
    frameActualizarGenero.pack(fill = X)
    frameActualizarDirector.pack(fill = X)
    frameActualizarFranquicia.pack(fill = X)
    frameActualizarPais.pack(fill = X)
    frameActualizarAnno.pack(fill = X)
    frameActualizarDuracion.pack(fill = X)
    frameActualizarActores.pack(fill = X)
    frameActualizarProductoras.pack(fill = X, pady = 10)
    frameActualizarPeliBotones.pack(fill=X)

    labelActualizarNombre.pack()
    labelActualizarGenero.pack()
    labelActualizarDirector.pack()
    labelActualizarFranquicia.pack()
    labelActualizarPais.pack()
    labelActualizarAnno.pack()
    labelActualizarDuracion.pack()
    labelActualizarActores.pack()
    labelActualizarProductoras.pack()

    comboboxActualizarNombre.pack()
    entryActualizarGenero.pack()
    entryActualizarDirector.pack()
    entryActualizarFranquicia.pack()
    entryActualizarPais.pack()
    entryActualizarAnno.pack()
    entryActualizarDuracion.pack()
    entryActualizarActores.pack()
    comboboxActualizarProductoras.pack()

    botonCancelarActualizarPeli.pack(side= RIGHT, padx = 100)
    botonAceptarActualizarPeli.pack(side = RIGHT, padx = 100)


