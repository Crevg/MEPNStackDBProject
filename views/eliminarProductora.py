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


def eliminarProduWindow(root):
    #ventana principal
    frameEliminarProdu = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameEliminarNombreProdu = Frame(frameEliminarProdu, bg = backgroundColor[0])
    frameEliminarProduBotones = Frame(frameEliminarProdu, bg = backgroundColor[0])
    #labels
    labelEliminarProdu = Label(frameEliminarProdu, text = "Eliminar Productora", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelEliminarNombreProdu = Label(frameEliminarNombreProdu, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])


    #funciones

    def cancelar():
        frameEliminarProdu.pack_forget()
        return    

    def eliminar():      
        nombre =  comboboxEliminarNombreProdu.get()
        print (nombre)
        id = colors.getIdByName(productoras, nombre)
        #verifica que no tenga pelis ligadas

        peliculas = cargarPeliculas()
        if peliculas == [[]]:
            messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")  
        else:
            for i in range(0, len(peliculas)):
                if peliculas[i]["productora"] == id:
                    messagebox.showerror("Error", "Debe eliminar las películas de esta compañía antes de eliminarla.")
                    return
        
        res = colors.borrarProductora(id)
        if res.status_code == requests.codes.ok:
            messagebox.showinfo("Listo!", "Se eliminó la película con éxito")
            frameEliminarPeli.pack_forget()
            return
        else:
            messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")  
  
        frameEliminarProdu.pack_forget()
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


    comboboxEliminarNombreProdu = ttk.Combobox(frameEliminarNombreProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")
    comboboxEliminarNombreProdu["values"] = listaProductoras 
    comboboxEliminarNombreProdu.current(0)

    #botones

    botonAceptarEliminarProdu = Button(frameEliminarProduBotones, text="Eliminar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= eliminar)
    botonCancelarEliminarProdu = Button(frameEliminarProduBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= cancelar)

    #packs
    frameEliminarProdu.pack(fill = BOTH)
    labelEliminarProdu.pack()
    frameEliminarNombreProdu.pack(fill = X, pady = 100)
    frameEliminarProduBotones.pack(fill=X)

    labelEliminarNombreProdu.pack()

    comboboxEliminarNombreProdu.pack()

    botonCancelarEliminarProdu.pack(side= RIGHT, padx = 100, pady = 50)
    botonAceptarEliminarProdu.pack(side = RIGHT, padx = 100, pady = 50)


