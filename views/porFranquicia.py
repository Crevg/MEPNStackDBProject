from tkinter import ttk
from tkinter import *
import colors
import requests
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


def franquiciaPeliWindow(root):
    #ventana principal
    frameFranquiciaPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameFranquiciaNombre = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaGenero = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaDirector = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaFranquicia = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaPais = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaAnno = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaDuracion = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaActores = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaProductoras = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    frameFranquiciaPeliBotones = Frame(frameFranquiciaPeli, bg = backgroundColor[0])
    #labels
    labelFranquiciaPeli = Label(frameFranquiciaPeli, text = "Consultar película por franquicia", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaNombre = Label(frameFranquiciaNombre, text= "Título", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaGenero = Label(frameFranquiciaGenero, text= "Género", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaDirector = Label(frameFranquiciaDirector, text= "Director", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaFranquicia = Label(frameFranquiciaFranquicia, text= "Franquicia", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaPais = Label(frameFranquiciaPais, text= "País", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaAnno = Label(frameFranquiciaAnno, text= "Año", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaDuracion = Label(frameFranquiciaDuracion, text= "Duración (en minutos)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaActores = Label(frameFranquiciaActores, text= "Actores (separados por coma)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelFranquiciaProductoras = Label(frameFranquiciaProductoras, text= "Compañia Productora", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])

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
    comboBoxFranquiciaNombre = ttk.Combobox(frameFranquiciaNombre,  width = 40, font= ("Arial Bold", 11),  state= "disabled")
    entryFranquiciaGenero = Entry(frameFranquiciaGenero, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryFranquiciaDirector = Entry(frameFranquiciaDirector, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryFranquiciaFranquicia = Entry(frameFranquiciaFranquicia, width = 40, font= ("Arial Bold", 11))
    entryFranquiciaPais= Entry(frameFranquiciaPais, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryFranquiciaAnno = Entry(frameFranquiciaAnno, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryFranquiciaDuracion = Entry(frameFranquiciaDuracion, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryFranquiciaActores = Entry(frameFranquiciaActores, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryFranquiciaProductoras = Entry(frameFranquiciaProductoras, width = 40, font= ("Arial Bold", 11),  state= "readonly")

    def cargarInfo(event):
        nombre = comboBoxFranquiciaNombre.get()
        indice = 0
        for i in range (0, len(listaPelis)):
            if listaPelis[i] == nombre:
                indice = i
                break

        entryFranquiciaGenero.config(state="normal")
        entryFranquiciaDirector.config(state="normal")
        comboBoxFranquiciaNombre.config(state="normal")
        entryFranquiciaPais.config(state="normal")
        entryFranquiciaAnno.config(state="normal")
        entryFranquiciaDuracion.config(state="normal")
        entryFranquiciaActores.config(state="normal")
        entryFranquiciaProductoras.config(state="normal")

        entryFranquiciaGenero.delete(0, END)
        entryFranquiciaDirector.delete(0, END)
        entryFranquiciaPais.delete(0, END)
        entryFranquiciaAnno.delete(0, END)
        entryFranquiciaDuracion.delete(0, END)
        entryFranquiciaActores.delete(0, END)
        entryFranquiciaProductoras.delete(0, END)
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

        entryFranquiciaGenero.insert(0,peliculas[indice]["genero"])
        entryFranquiciaDirector.insert(0,peliculas[indice]["nombreDirector"])
        entryFranquiciaPais.insert(0,peliculas[indice]["pais"])
        entryFranquiciaAnno.insert(0,peliculas[indice]["anno"])
        entryFranquiciaDuracion.insert(0,peliculas[indice]["duracion"])
        entryFranquiciaActores.insert(0, actores)
        entryFranquiciaProductoras.insert(0,nombreProd)   

        entryFranquiciaGenero.config(state="readonly")
        entryFranquiciaDirector.config(state="readonly")
        comboBoxFranquiciaNombre.config(state="readonly")
        entryFranquiciaPais.config(state="readonly")
        entryFranquiciaAnno.config(state="readonly")
        entryFranquiciaDuracion.config(state="readonly")
        entryFranquiciaActores.config(state="readonly")
        entryFranquiciaProductoras.config(state="readonly")

    comboBoxFranquiciaNombre.bind("<<ComboboxSelected>>", cargarInfo)

    def buscar():
        for i in range (0, len(peliculas)):
            peliculas.pop()
        for i in range (0, len(listaPelis)):
            listaPelis.pop()
        franquicia = entryFranquiciaFranquicia.get()
        if not franquicia:
            comboBoxFranquiciaNombre.config(state="disabled")

            messagebox.showerror("Error", "Por favor ingrese una franquicia válida.")
        else:
            res = colors.buscarPorFranquicia(franquicia)
            if res.status_code == requests.codes.ok:
                if len(res.json()) == 0:
                    comboBoxFranquiciaNombre.config(state="disabled")
                    messagebox.showinfo("Disculpe", "No se encontró una película en esa franquicia.")             

                else:


                    for i in range (0, len (res.json())):
                        peliculas.append(res.json()[i])
                    nombres = colors.getListaNombres(peliculas)
                    for i in range (0, len(nombres)):
                        listaPelis.append(nombres[i])
                    

                    comboBoxFranquiciaNombre.config(state="readonly")
                    comboBoxFranquiciaNombre["values"] = listaPelis
                    comboBoxFranquiciaNombre.current(0)
                    return cargarInfo("event")
            else:
                comboBoxFranquiciaNombre.config(state="disabled")
                messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor por favor intente más tarde")
        entryFranquiciaGenero.config(state="normal")
        entryFranquiciaDirector.config(state="normal")
        entryFranquiciaPais.config(state="normal")
        entryFranquiciaAnno.config(state="normal")
        entryFranquiciaDuracion.config(state="normal")
        entryFranquiciaActores.config(state="normal")
        entryFranquiciaProductoras.config(state="normal")

        entryFranquiciaGenero.delete(0, END)
        entryFranquiciaDirector.delete(0, END)
        entryFranquiciaPais.delete(0, END)
        entryFranquiciaAnno.delete(0, END)
        entryFranquiciaDuracion.delete(0, END)
        entryFranquiciaActores.delete(0, END)
        entryFranquiciaProductoras.delete(0, END)

        entryFranquiciaGenero.config(state="readonly")
        entryFranquiciaDirector.config(state="readonly")
        entryFranquiciaPais.config(state="readonly")
        entryFranquiciaAnno.config(state="readonly")
        entryFranquiciaDuracion.config(state="readonly")
        entryFranquiciaActores.config(state="readonly")
        entryFranquiciaProductoras.config(state="readonly")
    #funciones

    def cancelar():
        frameFranquiciaPeli.pack_forget()
        return    
    #botones

    botonBuscarFranquiciaPeli = Button(frameFranquiciaPeliBotones, text="Buscar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4],  command= buscar)
    botonCancelarFranquiciaPeli = Button(frameFranquiciaPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= cancelar)

    #packs
    frameFranquiciaPeli.pack(fill = BOTH)
    labelFranquiciaPeli.pack()
    frameFranquiciaFranquicia.pack(fill = X)
    frameFranquiciaNombre.pack(fill = X)
    frameFranquiciaGenero.pack(fill = X)
    frameFranquiciaDirector.pack(fill = X)
    frameFranquiciaPais.pack(fill = X)
    frameFranquiciaAnno.pack(fill = X)
    frameFranquiciaDuracion.pack(fill = X)
    frameFranquiciaActores.pack(fill = X)
    frameFranquiciaProductoras.pack(fill = X, pady = 10)
    frameFranquiciaPeliBotones.pack(fill=X)

    labelFranquiciaNombre.pack()
    labelFranquiciaGenero.pack()
    labelFranquiciaDirector.pack()
    labelFranquiciaFranquicia.pack()
    labelFranquiciaPais.pack()
    labelFranquiciaAnno.pack()
    labelFranquiciaDuracion.pack()
    labelFranquiciaActores.pack()
    labelFranquiciaProductoras.pack()

    comboBoxFranquiciaNombre.pack()
    entryFranquiciaGenero.pack()
    entryFranquiciaDirector.pack()
    entryFranquiciaFranquicia.pack()
    entryFranquiciaPais.pack()
    entryFranquiciaAnno.pack()
    entryFranquiciaDuracion.pack()
    entryFranquiciaActores.pack()
    entryFranquiciaProductoras.pack()

    botonCancelarFranquiciaPeli.pack(side= RIGHT, padx = 100)
    botonBuscarFranquiciaPeli.pack(side = RIGHT, padx = 100)

