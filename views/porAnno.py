from tkinter import ttk
from tkinter import *
import colors
import requests
import datetime
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor

def cargarProductoras():
    try:
        res = colors.leerProductoras()

        if res.status_code == requests.codes.ok:
            return res.json()
        else:
            return [[]]
    except requests.exceptions.ConnectionError:
        return [[]]


def annoPeliWindow(root):
    #ventana principal
    frameAnnoPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameAnnoNombre = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoGenero = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoDirector = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoFranquicia = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoPais = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameLabelsAnno = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoAnno = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoDuracion = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoActores = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoProductoras = Frame(frameAnnoPeli, bg = backgroundColor[0])
    frameAnnoPeliBotones = Frame(frameAnnoPeli, bg = backgroundColor[0])
    #labels
    labelAnnoPeli = Label(frameAnnoPeli, text = "Consultar película por año", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoNombre = Label(frameAnnoNombre, text= "Título", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoGenero = Label(frameAnnoGenero, text= "Género", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoDirector = Label(frameAnnoDirector, text= "Director", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoFranquicia = Label(frameAnnoFranquicia, text= "Franquicia", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoPais = Label(frameAnnoPais, text= "País", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoAnnoInicial = Label(frameLabelsAnno, text= "Año inicial", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoAnnoFinal = Label(frameLabelsAnno, text= "Año final", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoDuracion = Label(frameAnnoDuracion, text= "Duración (en minutos)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoActores = Label(frameAnnoActores, text= "Actores (separados por coma)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAnnoProductoras = Label(frameAnnoProductoras, text= "Compañia Productora", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys
    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return cancelar()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servir, por favor intentelo más tarde.")
        return cancelar()
    peliculas = []
    listaPelis = []
    comboBoxAnnoNombre = ttk.Combobox(frameAnnoNombre,  width = 40, font= ("Arial Bold", 11),  state= "disabled")
    entryAnnoGenero = Entry(frameAnnoGenero, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryAnnoDirector = Entry(frameAnnoDirector, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryAnnoFranquicia = Entry(frameAnnoFranquicia, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryAnnoPais= Entry(frameAnnoPais, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryAnnoAnnoInicial = Entry(frameAnnoAnno, width = 20, font= ("Arial Bold", 11))
    entryAnnoAnnoFinal = Entry(frameAnnoAnno, width = 20, font= ("Arial Bold", 11))
    entryAnnoDuracion = Entry(frameAnnoDuracion, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryAnnoActores = Entry(frameAnnoActores, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryAnnoProductoras = Entry(frameAnnoProductoras, width = 40, font= ("Arial Bold", 11),  state= "readonly")

    def cargarInfo(event):
        nombre = comboBoxAnnoNombre.get()
        indice = 0
        for i in range (0, len(listaPelis)):
            if listaPelis[i] == nombre:
                indice = i
                break

        entryAnnoGenero.config(state="normal")
        entryAnnoDirector.config(state="normal")
        comboBoxAnnoNombre.config(state="normal")
        entryAnnoPais.config(state="normal")
        entryAnnoFranquicia.config(state="normal")
        entryAnnoDuracion.config(state="normal")
        entryAnnoActores.config(state="normal")
        entryAnnoProductoras.config(state="normal")

        entryAnnoGenero.delete(0, END)
        entryAnnoDirector.delete(0, END)
        entryAnnoPais.delete(0, END)
        entryAnnoFranquicia.delete(0, END)
        entryAnnoDuracion.delete(0, END)
        entryAnnoActores.delete(0, END)
        entryAnnoProductoras.delete(0, END)
        actores = ""
        cantActores = len(peliculas[indice]["actores"])
        for i in range (0, cantActores):
            actores = actores + peliculas[indice]["actores"][i]
            if i + 1 < cantActores:
                actores = actores + ","
            
        nombreProd = "Productora no encontrada"
        for i in range(0, len (productoras)):
            if productoras[i]["_id"] == peliculas[indice]["productora"]:
                nombreProd = productoras[i]["nombre"]
                break

        entryAnnoGenero.insert(0,peliculas[indice]["genero"])
        entryAnnoDirector.insert(0,peliculas[indice]["nombreDirector"])
        entryAnnoPais.insert(0,peliculas[indice]["pais"])
        entryAnnoFranquicia.insert(0,peliculas[indice]["anno"])
        entryAnnoDuracion.insert(0,peliculas[indice]["duracion"])
        entryAnnoActores.insert(0, actores)
        entryAnnoProductoras.insert(0,nombreProd)   

        entryAnnoGenero.config(state="readonly")
        entryAnnoDirector.config(state="readonly")
        comboBoxAnnoNombre.config(state="readonly")
        entryAnnoPais.config(state="readonly")
        entryAnnoFranquicia.config(state="readonly")
        entryAnnoDuracion.config(state="readonly")
        entryAnnoActores.config(state="readonly")
        entryAnnoProductoras.config(state="readonly")

    comboBoxAnnoNombre.bind("<<ComboboxSelected>>", cargarInfo)

    def buscar():
        for i in range (0, len(peliculas)):
            peliculas.pop()
        for i in range (0, len(listaPelis)):
            listaPelis.pop()
        annoInicial = entryAnnoAnnoInicial.get()
        annoFinal = entryAnnoAnnoFinal.get()
        year = datetime.date.today().year

        if not annoInicial or not annoFinal:
            comboBoxAnnoNombre.config(state="disabled")
            messagebox.showerror("Error", "Por favor ingrese años válidos.")
        else:
            try:
                annoInicial = int (annoInicial)
                annoFinal = int (annoFinal)
                valido = True
            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número")
                valido = False
            if valido:
                if annoFinal > year or annoInicial < 1900:
                    messagebox.showerror("Error", "Por favor ingrese años válidos.")
                else:
                    res = colors.buscarPorAnno(annoInicial, annoFinal)
                    if res.status_code == requests.codes.ok:

                        if len(res.json()) == 0:
                            comboBoxAnnoNombre.config(state="disabled")
                            messagebox.showinfo("Disculpe", "No se encontraron películas en esos años.")             

                        else:
                            for i in range (0, len (res.json())):
                                peliculas.append(res.json()[i])
                            nombres = colors.getListaNombres(peliculas)
                            for i in range (0, len(nombres)):
                                listaPelis.append(nombres[i])
                            comboBoxAnnoNombre.config(state="readonly")
                            comboBoxAnnoNombre["values"] = listaPelis
                            comboBoxAnnoNombre.current(0)
                            return cargarInfo("event")
                    else:
                        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
                        comboBoxAnnoNombre.config(state="disabled")
            else:
                comboBoxAnnoNombre.config(state="disabled")
        entryAnnoGenero.config(state="normal")
        entryAnnoDirector.config(state="normal")
        entryAnnoPais.config(state="normal")
        entryAnnoFranquicia.config(state="normal")
        entryAnnoDuracion.config(state="normal")
        entryAnnoActores.config(state="normal")
        entryAnnoProductoras.config(state="normal")

        entryAnnoGenero.delete(0, END)
        entryAnnoDirector.delete(0, END)
        entryAnnoPais.delete(0, END)
        entryAnnoFranquicia.delete(0, END)
        entryAnnoDuracion.delete(0, END)
        entryAnnoActores.delete(0, END)
        entryAnnoProductoras.delete(0, END)

        entryAnnoGenero.config(state="readonly")
        entryAnnoDirector.config(state="readonly")
        entryAnnoPais.config(state="readonly")
        entryAnnoFranquicia.config(state="readonly")
        entryAnnoDuracion.config(state="readonly")
        entryAnnoActores.config(state="readonly")
        entryAnnoProductoras.config(state="readonly")
    #funciones

    def cancelar():
        frameAnnoPeli.pack_forget()
        return    
    #botones

    botonBuscarAnnoPeli = Button(frameAnnoPeliBotones, text="Buscar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4],  command= buscar)
    botonCancelarAnnoPeli = Button(frameAnnoPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= cancelar)

    #packs
    frameAnnoPeli.pack(fill = BOTH)
    labelAnnoPeli.pack()
    frameLabelsAnno.pack(fill = X)
    frameAnnoAnno.pack(fill = X)
    frameAnnoNombre.pack(fill = X)
    frameAnnoGenero.pack(fill = X)
    frameAnnoDirector.pack(fill = X)
    frameAnnoFranquicia.pack(fill = X)
    frameAnnoPais.pack(fill = X)
    frameAnnoDuracion.pack(fill = X)
    frameAnnoActores.pack(fill = X)
    frameAnnoProductoras.pack(fill = X, pady = 10)
    frameAnnoPeliBotones.pack(fill=X)

    labelAnnoNombre.pack()
    labelAnnoGenero.pack()
    labelAnnoDirector.pack()
    labelAnnoFranquicia.pack()
    labelAnnoPais.pack()
    labelAnnoAnnoFinal.pack(side = RIGHT, padx = 140)
    labelAnnoAnnoInicial.pack(side = RIGHT , padx = 90)
    labelAnnoDuracion.pack()
    labelAnnoActores.pack()
    labelAnnoProductoras.pack()

    comboBoxAnnoNombre.pack()
    entryAnnoGenero.pack()
    entryAnnoDirector.pack()
    entryAnnoFranquicia.pack()
    entryAnnoPais.pack()
    entryAnnoAnnoFinal.pack(side = RIGHT, padx = 100)
    entryAnnoAnnoInicial.pack(side = RIGHT)
    entryAnnoDuracion.pack()
    entryAnnoActores.pack()
    entryAnnoProductoras.pack()

    botonCancelarAnnoPeli.pack(side= RIGHT, padx = 100)
    botonBuscarAnnoPeli.pack(side = RIGHT, padx = 100)

