from tkinter import ttk
from tkinter import *
import colors
import requests
import datetime

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

    def actualizar():
        idPeli = colors.getIdByName(peliculas, comboboxActualizarNombre.get())
        year = datetime.date.today().year
        nombre = comboboxActualizarNombre.get()
        genero = entryActualizarGenero.get()
        director = entryActualizarDirector.get()
        franquicia = entryActualizarFranquicia.get()
        pais = entryActualizarPais.get()
        anno = entryActualizarAnno.get()
        duracion = entryActualizarDuracion.get()
        actores = entryActualizarActores.get()
        productora = comboboxActualizarProductoras.get()
        id_productora = colors.getIdByName(productoras, productora)

        if not nombre or not genero or not director or not pais or not anno or not duracion or not actores or not productora:
            messagebox.showerror("Error", "Todos los campos menos franquicia son obligatorios")
        else:
            valido = False
            try:
                anno = int (anno)
                duracion = int (duracion)
                valido = True
            except ValueError:
                messagebox.showerror("Error", "El año y la duración deben ser números")
                valido = False
            if valido:
                if anno > year or anno < 1900 or duracion < 0:
                    messagebox.showerror("Error", "Por favor inserte un año y una duración válidas")
                else:
                    actores = actores.split(",")
                    body = {"nombre": nombre, "genero": genero, "nombreDirector": director, "franquicia": franquicia, "pais": pais, "anno": anno, "duracion": duracion, "actores": actores, "productora": id_productora}
                    try:
                        res = colors.actualizarPelicula(body, idPeli)
                        messagebox.showinfo("Listo!", "Se actualizó la película nueva con éxito.")
                        frameActualizarPeli.pack_forget()
                    except requests.exceptions.ConnectionError:
                        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
                    return   



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
                actores = actores + ","
            

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


