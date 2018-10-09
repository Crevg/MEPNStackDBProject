from tkinter import ttk
from tkinter import *
import colors
import requests
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor


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



def leerPeliWindow(root):
    #ventana principal
    frameLeerPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameLeerNombre = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerGenero = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerDirector = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerFranquicia = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerPais = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerAnno = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerDuracion = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerActores = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerProductoras = Frame(frameLeerPeli, bg = backgroundColor[0])
    frameLeerPeliBotones = Frame(frameLeerPeli, bg = backgroundColor[0])
    #labels
    labelLeerPeli = Label(frameLeerPeli, text = "Consultar Información de Películas", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerNombre = Label(frameLeerNombre, text= "Nombre", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerGenero = Label(frameLeerGenero, text= "Género", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerDirector = Label(frameLeerDirector, text= "Director", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerFranquicia = Label(frameLeerFranquicia, text= "Franquicia", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerPais = Label(frameLeerPais, text= "País", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerAnno = Label(frameLeerAnno, text= "Año", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerDuracion = Label(frameLeerDuracion, text= "Duración (en minutos)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerActores = Label(frameLeerActores, text= "Actores (separados por coma)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerProductoras = Label(frameLeerProductoras, text= "Compañia Productora", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])

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
    

    listaPelis = colors.getListaNombres(peliculas)
    comboboxLeerNombre = ttk.Combobox(frameLeerNombre, width = 40, font= ("Arial Bold", 11), state = "readonly")
    comboboxLeerNombre["values"] = listaPelis
    entryLeerGenero = Entry(frameLeerGenero, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerDirector = Entry(frameLeerDirector, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerFranquicia = Entry(frameLeerFranquicia, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerPais= Entry(frameLeerPais, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerAnno = Entry(frameLeerAnno, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerDuracion = Entry(frameLeerDuracion, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerActores = Entry(frameLeerActores, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryLeerProductoras = Entry(frameLeerProductoras, width = 40, font= ("Arial Bold", 11),  state= "readonly")

    def cargarInfo(event):
        indice = 0
        for i in range (0, len(listaPelis)):
            if listaPelis[i] == comboboxLeerNombre.get():
                indice = i
                break
        nombreProd = "Productora no encontrada"
        for i in range(0, len (productoras)):
            if productoras[i]["_id"] == peliculas[indice]["productora"]:
                nombreProd = productoras[i]["nombre"]
                break
        actores = ""
        cantActores = len(peliculas[indice]["actores"])
        for i in range (0, cantActores):
            actores = actores + peliculas[indice]["actores"][i]
            if i + 1 < cantActores:
                actores = actores + ", "
            

        entryLeerGenero.config(state="normal")
        entryLeerDirector.config(state="normal")
        entryLeerFranquicia.config(state="normal")
        entryLeerPais.config(state="normal")
        entryLeerAnno.config(state="normal")
        entryLeerDuracion.config(state="normal")
        entryLeerActores.config(state="normal")
        entryLeerProductoras.config(state="normal")
    
        entryLeerGenero.delete(0, END)
        entryLeerDirector.delete(0, END)
        entryLeerFranquicia.delete(0, END)
        entryLeerPais.delete(0, END)
        entryLeerAnno.delete(0, END)
        entryLeerDuracion.delete(0, END)
        entryLeerActores.delete(0, END)
        entryLeerProductoras.delete(0, END)

        entryLeerGenero.insert(0,peliculas[indice]["genero"])
        entryLeerDirector.insert(0,peliculas[indice]["nombreDirector"])
        entryLeerFranquicia.insert(0,peliculas[indice]["franquicia"])
        entryLeerPais.insert(0,peliculas[indice]["pais"])
        entryLeerAnno.insert(0,peliculas[indice]["anno"])
        entryLeerDuracion.insert(0,peliculas[indice]["duracion"])
        entryLeerActores.insert(0, actores)
        entryLeerProductoras.insert(0,nombreProd)

        entryLeerGenero.config(state="readonly")
        entryLeerDirector.config(state="readonly")
        entryLeerFranquicia.config(state="readonly")
        entryLeerPais.config(state="readonly")
        entryLeerAnno.config(state="readonly")
        entryLeerDuracion.config(state="readonly")
        entryLeerActores.config(state="readonly")
        entryLeerProductoras.config(state="readonly")
    
    
    comboboxLeerNombre.bind("<<ComboboxSelected>>", cargarInfo)

    #funciones

    def volver():
        frameLeerPeli.pack_forget()
        return    
    #botones

    botonVolverLeerPeli = Button(frameLeerPeliBotones, text="Volver" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= volver)

    #packs
    frameLeerPeli.pack(fill = BOTH)
    labelLeerPeli.pack()
    frameLeerNombre.pack(fill = X)
    frameLeerGenero.pack(fill = X)
    frameLeerDirector.pack(fill = X)
    frameLeerFranquicia.pack(fill = X)
    frameLeerPais.pack(fill = X)
    frameLeerAnno.pack(fill = X)
    frameLeerDuracion.pack(fill = X)
    frameLeerActores.pack(fill = X)
    frameLeerProductoras.pack(fill = X, pady = 10)
    frameLeerPeliBotones.pack(fill=X)

    labelLeerNombre.pack()
    labelLeerGenero.pack()
    labelLeerDirector.pack()
    labelLeerFranquicia.pack()
    labelLeerPais.pack()
    labelLeerAnno.pack()
    labelLeerDuracion.pack()
    labelLeerActores.pack()
    labelLeerProductoras.pack()

    comboboxLeerNombre.pack()
    entryLeerGenero.pack()
    entryLeerDirector.pack()
    entryLeerFranquicia.pack()
    entryLeerPais.pack()
    entryLeerAnno.pack()
    entryLeerDuracion.pack()
    entryLeerActores.pack()
    entryLeerProductoras.pack()

    botonVolverLeerPeli.pack(side = TOP)


