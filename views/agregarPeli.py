from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import colors
import requests
import datetime

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
    frameAgregarDirector = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarFranquicia = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarPais = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarAnno = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarDuracion = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarActores = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarProductoras = Frame(frameAgregarPeli, bg = backgroundColor[0])
    frameAgregarPeliBotones = Frame(frameAgregarPeli, bg = backgroundColor[0])
    #labels
    labelAgregarPeli = Label(frameAgregarPeli, text = "Agregar Nueva Película", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarNombre = Label(frameAgregarNombre, text= "Nombre", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarGenero = Label(frameAgregarGenero, text= "Género", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarDirector = Label(frameAgregarDirector, text= "Director", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarFranquicia = Label(frameAgregarFranquicia, text= "Franquicia (si corresponde)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarPais = Label(frameAgregarPais, text= "País", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarDuracion = Label(frameAgregarDuracion, text= "Duración (en minutos)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarAnno = Label(frameAgregarAnno, text= "Año", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarActores = Label(frameAgregarActores, text= "Actores (separados por coma)", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarProductoras = Label(frameAgregarProductoras, text= "Compañia Productora", font= ("Arial Bold", 11), fg= foregroundColor[0], bg=backgroundColor[0])

   #funciones

    def cancelar():
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


    entryAgregarNombre = Entry(frameAgregarNombre, width = 40, font= ("Arial Bold", 11))
    entryAgregarGenero = Entry(frameAgregarGenero, width = 40, font= ("Arial Bold", 11))
    entryAgregarDirector = Entry(frameAgregarDirector, width = 40, font= ("Arial Bold", 11))
    entryAgregarFranquicia = Entry(frameAgregarFranquicia, width = 40, font= ("Arial Bold", 11))
    entryAgregarPais= Entry(frameAgregarPais, width = 40, font= ("Arial Bold", 11))
    entryAgregarAnno = Entry(frameAgregarAnno, width = 40, font= ("Arial Bold", 11))
    entryAgregarDuracion = Entry(frameAgregarDuracion, width = 40, font= ("Arial Bold", 11))
    entryAgregarActores = Entry(frameAgregarActores, width = 40, font= ("Arial Bold", 11))
    comboboxAgregarProductoras = ttk.Combobox(frameAgregarProductoras, width = 40, font= ("Arial Bold", 11),  state= "readonly")
    comboboxAgregarProductoras["values"] = listaProductoras
    comboboxAgregarProductoras.current(0)


    def agregar():
        year = datetime.date.today().year

        nombre = entryAgregarNombre.get()
        genero = entryAgregarGenero.get()
        director = entryAgregarDirector.get()
        franquicia = entryAgregarFranquicia.get()
        pais = entryAgregarPais.get()
        anno = entryAgregarAnno.get()
        duracion = entryAgregarDuracion.get()
        actores = entryAgregarActores.get()
        productora = comboboxAgregarProductoras.get()
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
                        res = colors.agregarPelicula(body)
                        messagebox.showinfo("Listo!", "Se agregó la película nueva con éxito.")
                        frameAgregarPeli.pack_forget()
                    except requests.exceptions.ConnectionError:
                        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
                    return 
                   
 
    #botones

    botonAceptarAgregarPeli = Button(frameAgregarPeliBotones, text="Agregar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= agregar)
    botonCancelarAgregarPeli = Button(frameAgregarPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 11), bg = backgroundColor[4], command= cancelar)

    #packs
    frameAgregarPeli.pack(fill = BOTH)
    labelAgregarPeli.pack()
    frameAgregarNombre.pack(fill = X)
    frameAgregarGenero.pack(fill = X)
    frameAgregarDirector.pack(fill = X)
    frameAgregarFranquicia.pack(fill = X)
    frameAgregarPais.pack(fill = X)
    frameAgregarAnno.pack(fill = X)
    frameAgregarDuracion.pack(fill = X)
    frameAgregarActores.pack(fill = X)
    frameAgregarProductoras.pack(fill = X, pady = 10)
    frameAgregarPeliBotones.pack(fill=X)

    labelAgregarNombre.pack()
    labelAgregarGenero.pack()
    labelAgregarDirector.pack()
    labelAgregarFranquicia.pack()
    labelAgregarPais.pack()
    labelAgregarAnno.pack()
    labelAgregarDuracion.pack()
    labelAgregarActores.pack()
    labelAgregarProductoras.pack()

    entryAgregarNombre.pack()
    entryAgregarGenero.pack()
    entryAgregarDirector.pack()
    entryAgregarFranquicia.pack()
    entryAgregarPais.pack()
    entryAgregarAnno.pack()
    entryAgregarDuracion.pack()
    entryAgregarActores.pack()
    comboboxAgregarProductoras.pack()

    botonCancelarAgregarPeli.pack(side= RIGHT, padx = 150)
    botonAceptarAgregarPeli.pack(side = RIGHT, padx = 50)


