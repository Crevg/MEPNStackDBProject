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



def tituloPeliWindow(root):
    #ventana principal
    frameTituloPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameTituloNombre = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloGenero = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloDirector = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloFranquicia = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloPais = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloAnno = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloDuracion = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloActores = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloProductoras = Frame(frameTituloPeli, bg = backgroundColor[0])
    frameTituloPeliBotones = Frame(frameTituloPeli, bg = backgroundColor[0])
    #labels
    labelTituloPeli = Label(frameTituloPeli, text = "Consultar película por título", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloNombre = Label(frameTituloNombre, text= "Título", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloGenero = Label(frameTituloGenero, text= "Género", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloDirector = Label(frameTituloDirector, text= "Director", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloFranquicia = Label(frameTituloFranquicia, text= "Franquicia", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloPais = Label(frameTituloPais, text= "País", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloAnno = Label(frameTituloAnno, text= "Año", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloDuracion = Label(frameTituloDuracion, text= "Duración (en minutos)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloActores = Label(frameTituloActores, text= "Actores (separados por coma)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelTituloProductoras = Label(frameTituloProductoras, text= "Compañia Productora", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys
    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return cancelar()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servir, por favor intentelo más tarde.")
        return cancelar()

    entryTituloNombre = Entry(frameTituloNombre,  width = 40, font= ("Arial Bold", 11))
    entryTituloGenero = Entry(frameTituloGenero, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloDirector = Entry(frameTituloDirector, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloFranquicia = Entry(frameTituloFranquicia, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloPais= Entry(frameTituloPais, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloAnno = Entry(frameTituloAnno, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloDuracion = Entry(frameTituloDuracion, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloActores = Entry(frameTituloActores, width = 40, font= ("Arial Bold", 11), state = "readonly")
    entryTituloProductoras = Entry(frameTituloProductoras, width = 40, font= ("Arial Bold", 11),  state= "readonly")

    def buscar():
        entryTituloGenero.config(state="normal")
        entryTituloDirector.config(state="normal")
        entryTituloFranquicia.config(state="normal")
        entryTituloPais.config(state="normal")
        entryTituloAnno.config(state="normal")
        entryTituloDuracion.config(state="normal")
        entryTituloActores.config(state="normal")
        entryTituloProductoras.config(state="normal")
    
        entryTituloGenero.delete(0, END)
        entryTituloDirector.delete(0, END)
        entryTituloFranquicia.delete(0, END)
        entryTituloPais.delete(0, END)
        entryTituloAnno.delete(0, END)
        entryTituloDuracion.delete(0, END)
        entryTituloActores.delete(0, END)
        entryTituloProductoras.delete(0, END)


        nombre = entryTituloNombre.get()
        if not nombre:
            messagebox.showerror("Error", "Por favor ingrese un nombre válido.")
        else:
            res = colors.buscarPorTitulo(nombre)
            if res.status_code == requests.codes.ok:
                if len(res.text) == 0:
                    messagebox.showinfo("Disculpe", "No se encontró una película con ese título.")             

                else:
                    pelicula = res.json() 
                    actores = ""
                    cantActores = len(pelicula["actores"])
                    for i in range (0, cantActores):
                        actores = actores + pelicula["actores"][i]
                        if i + 1 < cantActores:
                            actores = actores + ","
                        
                    nombreProd = "Productora no encontrada"
                    for i in range(0, len (productoras)):
                        if productoras[i]["_id"] == pelicula["productora"]:
                            nombreProd = productoras[i]["nombre"]
                            break
                    

                    entryTituloGenero.insert(0,pelicula["genero"])
                    entryTituloDirector.insert(0,pelicula["nombreDirector"])
                    entryTituloFranquicia.insert(0,pelicula["franquicia"])
                    entryTituloPais.insert(0,pelicula["pais"])
                    entryTituloAnno.insert(0,pelicula["anno"])
                    entryTituloDuracion.insert(0,pelicula["duracion"])
                    entryTituloActores.insert(0, actores)
                    entryTituloProductoras.insert(0,nombreProd)                
            else:
                messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor por favor intente más tarde")
        entryTituloGenero.config(state="readonly")
        entryTituloDirector.config(state="readonly")
        entryTituloFranquicia.config(state="readonly")
        entryTituloPais.config(state="readonly")
        entryTituloAnno.config(state="readonly")
        entryTituloDuracion.config(state="readonly")
        entryTituloActores.config(state="readonly")
        entryTituloProductoras.config(state="readonly")
    #funciones

    def cancelar():
        frameTituloPeli.pack_forget()
        return    
    #botones

    botonBuscarTituloPeli = Button(frameTituloPeliBotones, text="Buscar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= buscar)
    botonCancelarTituloPeli = Button(frameTituloPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= cancelar)

    #packs
    frameTituloPeli.pack(fill = BOTH)
    labelTituloPeli.pack()
    frameTituloNombre.pack(fill = X)
    frameTituloGenero.pack(fill = X)
    frameTituloDirector.pack(fill = X)
    frameTituloFranquicia.pack(fill = X)
    frameTituloPais.pack(fill = X)
    frameTituloAnno.pack(fill = X)
    frameTituloDuracion.pack(fill = X)
    frameTituloActores.pack(fill = X)
    frameTituloProductoras.pack(fill = X, pady = 10)
    frameTituloPeliBotones.pack(fill=X)

    labelTituloNombre.pack()
    labelTituloGenero.pack()
    labelTituloDirector.pack()
    labelTituloFranquicia.pack()
    labelTituloPais.pack()
    labelTituloAnno.pack()
    labelTituloDuracion.pack()
    labelTituloActores.pack()
    labelTituloProductoras.pack()

    entryTituloNombre.pack()
    entryTituloGenero.pack()
    entryTituloDirector.pack()
    entryTituloFranquicia.pack()
    entryTituloPais.pack()
    entryTituloAnno.pack()
    entryTituloDuracion.pack()
    entryTituloActores.pack()
    entryTituloProductoras.pack()

    botonCancelarTituloPeli.pack(side= RIGHT, padx = 100)
    botonBuscarTituloPeli.pack(side = RIGHT, padx = 100)

