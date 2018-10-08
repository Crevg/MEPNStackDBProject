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

def eliminarPeliWindow(root):
    #ventana principal
    frameEliminarPeli = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameEliminarNombre = Frame(frameEliminarPeli, bg = backgroundColor[0])
    frameEliminarPeliBotones = Frame(frameEliminarPeli, bg = backgroundColor[0])
    #labels
    labelEliminarPeli = Label(frameEliminarPeli, text = "Eliminar Película", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelEliminarNombre = Label(frameEliminarNombre, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys


    peliculas = cargarPeliculas()
    if peliculas == []:
        messagebox.showerror("Error", "No existen películas, por favor agregue una antes de continuar.")
        return cancelar()
    elif peliculas[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
        return cancelar()

    listaNombres = colors.getListaNombres(peliculas)

    print (listaNombres)
    comboboxEliminarNombre = ttk.Combobox(frameEliminarNombre, width = 40, font= ("Arial Bold", 15), state= "readonly")
    comboboxEliminarNombre["values"] = listaNombres 
    comboboxEliminarNombre.current(0)

    #funciones

    def cancelar():
        frameEliminarPeli.pack_forget()
        return    

    def eliminar():
        nombre =  comboboxEliminarNombre.get()
        id = colors.getIdByName(peliculas, nombre)
        res = colors.borrarPelicula(id)
        if res.status_code == requests.codes.ok:
            messagebox.showinfo("Listo!", "Se eliminó la película con éxito")
            frameEliminarPeli.pack_forget()
            return
        else:
            messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")  

    #botones

    botonAceptarEliminarPeli = Button(frameEliminarPeliBotones, text="Eliminar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= eliminar)
    botonCancelarEliminarPeli = Button(frameEliminarPeliBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= cancelar)

    #packs
    frameEliminarPeli.pack(fill = BOTH)
    labelEliminarPeli.pack()
    frameEliminarNombre.pack(fill = X, pady = 100)
    frameEliminarPeliBotones.pack(fill=X)

    labelEliminarNombre.pack()

    comboboxEliminarNombre.pack()

    botonCancelarEliminarPeli.pack(side= RIGHT, padx = 100, pady = 50)
    botonAceptarEliminarPeli.pack(side = RIGHT, padx = 100, pady = 50)


