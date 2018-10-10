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


def productoraPeliWindow(root):
    #ventana principal
    frameProductoraPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameProductoraNombre = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraGenero = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraAnno = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraProductoras = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraPeliBotonesDatos = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraCantidad = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraDuracionMaxima = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraDuracionMinima = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraDuracionPromedio = Frame(frameProductoraPeli, bg = backgroundColor[0])
    frameProductoraPeliBotonesDuracion = Frame(frameProductoraPeli, bg = backgroundColor[0])

    #labels
    labelProductoraPeli = Label(frameProductoraPeli, text = "Consultar película por Productora", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraNombre = Label(frameProductoraNombre, text= "Título", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraGenero = Label(frameProductoraGenero, text= "Género", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraAnno = Label(frameProductoraAnno, text= "Año", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraProductoras = Label(frameProductoraProductoras, text= "Compañia Productora", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraCantidad = Label(frameProductoraCantidad, text= "Cantidad", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraDuracionMaxima = Label(frameProductoraDuracionMaxima, text= "Duración Máxima", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraDuracionMinima = Label(frameProductoraDuracionMinima, text= "Duración Mínima", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])
    labelProductoraDuracionPromedio = Label(frameProductoraDuracionPromedio, text= "Duración Promedio", font= ("Arial Bold", 10), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys
    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return cancelar()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servir, por favor intentelo más tarde.")
        return cancelar()
    listaProduc = colors.getListaNombres(productoras)
    peliculas = []
    listaPelis = []

    comboBoxProductoraNombre = ttk.Combobox(frameProductoraNombre,  width = 40, font= ("Arial Bold", 10),  state= "disabled")
    entryProductoraGenero = Entry(frameProductoraGenero, width = 40, font= ("Arial Bold", 10), state = "readonly")
    entryProductoraAnno = Entry(frameProductoraAnno, width = 40, font= ("Arial Bold", 10), state = "readonly")
    entryProductoraCantidad = Entry(frameProductoraCantidad, width = 40, font= ("Arial Bold", 10), state = "readonly")
    entryProductoraDuracionMaxima = Entry(frameProductoraDuracionMaxima, width = 40, font= ("Arial Bold", 10), state = "readonly")
    entryProductoraDuracionMinima = Entry(frameProductoraDuracionMinima, width = 40, font= ("Arial Bold", 10), state = "readonly")
    entryProductoraDuracionPromedio = Entry(frameProductoraDuracionPromedio, width = 40, font= ("Arial Bold", 10), state = "readonly")

    comboBoxProductoraProductoras = ttk.Combobox(frameProductoraProductoras,  width = 40, font= ("Arial Bold", 10),  state= "readonly")
    comboBoxProductoraProductoras["values"] = listaProduc

    def cargarInfo(event):
        nombre = comboBoxProductoraNombre.get()
        indice = 0
        for i in range (0, len(listaPelis)):
            if listaPelis[i] == nombre:
                indice = i
                break

        entryProductoraGenero.config(state="normal")
        comboBoxProductoraNombre.config(state="normal")
        entryProductoraAnno.config(state="normal")

        entryProductoraGenero.delete(0, END)
        entryProductoraAnno.delete(0, END)
        
        nombreProd = "Productora no encontrada"
        entryProductoraGenero.insert(0,peliculas[indice]["genero"])
        entryProductoraAnno.insert(0,peliculas[indice]["anno"])
        comboBoxProductoraNombre.config(state = "readonly")
        entryProductoraGenero.config(state="readonly")
        entryProductoraAnno.config(state="readonly")

    comboBoxProductoraNombre.bind("<<ComboboxSelected>>", cargarInfo)

    def buscardatos():
        for i in range (0, len(peliculas)):
            peliculas.pop()
        for i in range (0, len(listaPelis)):
            listaPelis.pop()
        Productora = comboBoxProductoraProductoras.get()
        if not Productora:
            comboBoxProductoraNombre.config(state="disabled")
            messagebox.showerror("Error", "Por favor ingrese una Productora válida.")
        else:
            idprod = colors.getIdByName(productoras, Productora)
            res = colors.buscarPorProductoraDatos(idprod)
            if res.status_code == requests.codes.ok:
                if len(res.json()) == 0:
                    comboBoxProductoraNombre.config(state="disabled")
                    messagebox.showinfo("Disculpe", "No se encontró una película de esa Productora.")             
                else:
                    for i in range (0, len (res.json())):
                        peliculas.append(res.json()[i])
                    nombres = colors.getListaNombres(peliculas)
                    for i in range (0, len(nombres)):
                        listaPelis.append(nombres[i])
                    comboBoxProductoraNombre.config(state="readonly")
                    comboBoxProductoraNombre["values"] = listaPelis
                    comboBoxProductoraNombre.current(0)
                    return cargarInfo("event")
            else:
                comboBoxProductoraNombre.config(state="disabled")
                messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor por favor intente más tarde") 
        entryProductoraGenero.config(state="normal")
        entryProductoraAnno.config(state="normal")

        entryProductoraGenero.delete(0, END)
        entryProductoraAnno.delete(0, END)

        entryProductoraGenero.config(state="readonly")
        entryProductoraAnno.config(state="readonly")
    #funciones

    def buscarduracion():
        Productora = comboBoxProductoraProductoras.get()
        if not Productora:
            comboBoxProductoraNombre.config(state="disabled")
            messagebox.showerror("Error", "Por favor ingrese una Productora válida.")
        else:
            idprod = colors.getIdByName(productoras, Productora)
            res = colors.buscarPorProductoraDuracion(idprod)
            if res.status_code == requests.codes.ok:
                if len(res.json()) == 0:
                    messagebox.showinfo("Disculpe", "No se encontró una película de esa Productora.")             
                else:
                    valores = res.json()[0]["value"]
                    print (res.json()[0])
                    entryProductoraCantidad.config(state = "normal")
                    entryProductoraDuracionMaxima.config(state = "normal")
                    entryProductoraDuracionMinima.config(state = "normal")
                    entryProductoraDuracionPromedio.config(state = "normal")

                    entryProductoraCantidad.delete(0, END)
                    entryProductoraDuracionMaxima.delete(0, END)
                    entryProductoraDuracionMinima.delete(0, END)
                    entryProductoraDuracionPromedio.delete(0, END)

                    entryProductoraCantidad.insert(0, valores["cantidad"])
                    entryProductoraDuracionMaxima.insert(0, valores["duracionMaxima"])
                    entryProductoraDuracionMinima.insert(0, valores["duracionMinima"])
                    entryProductoraDuracionPromedio.insert(0, valores["duracionPromedio"])

                    entryProductoraCantidad.config(state = "readonly")
                    entryProductoraDuracionMaxima.config(state = "readonly")
                    entryProductoraDuracionMinima.config(state = "readonly")
                    entryProductoraDuracionPromedio.config(state = "readonly")
                    

    def cancelar():
        frameProductoraPeli.pack_forget()
        return    
    #botones

    botonBuscarProductoraPeli = Button(frameProductoraPeliBotonesDatos, text="Buscar datos de películas" , font= ("Arial Bold", 10), bg = backgroundColor[4],  command= buscardatos)
    botonCancelarProductoraPeli = Button(frameProductoraDuracionPromedio, text="Cancelar", font= ("Arial Bold", 10), bg = backgroundColor[4], command= cancelar)
    botonBuscarDuracionProductoraPeli = Button(frameProductoraPeliBotonesDuracion, text="Buscar información de duración" , font= ("Arial Bold", 10), bg = backgroundColor[4],  command= buscarduracion)


    #packs

    frameProductoraPeli.pack(fill = BOTH)
    labelProductoraPeli.pack()
    frameProductoraProductoras.pack(fill = X, pady = 5)
    frameProductoraPeliBotonesDatos.pack(fill=X)
    frameProductoraNombre.pack(fill = X)
    frameProductoraGenero.pack(fill = X)
    frameProductoraAnno.pack(fill = X, pady = 5)
    frameProductoraPeliBotonesDuracion.pack(fill = X)
    frameProductoraCantidad.pack(fill = X)
    frameProductoraDuracionMaxima.pack(fill = X)
    frameProductoraDuracionMinima.pack(fill = X)
    frameProductoraDuracionPromedio.pack(fill = X, pady = 5)

    labelProductoraNombre.pack()
    labelProductoraGenero.pack()
    labelProductoraAnno.pack()
    labelProductoraCantidad.pack()
    labelProductoraDuracionMaxima.pack()
    labelProductoraDuracionMinima.pack()
    labelProductoraDuracionPromedio.pack()

    comboBoxProductoraNombre.pack()
    entryProductoraGenero.pack()
    entryProductoraAnno.pack()
    comboBoxProductoraProductoras.pack()
    entryProductoraCantidad.pack()
    entryProductoraDuracionMaxima.pack()
    entryProductoraDuracionMinima.pack()
    entryProductoraDuracionPromedio.pack()

    botonBuscarProductoraPeli.pack(side = TOP)
    botonBuscarDuracionProductoraPeli.pack(side = TOP)
    botonCancelarProductoraPeli.pack(side  = TOP, pady= 10)
