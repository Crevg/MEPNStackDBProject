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


def leerProduWindow(root):
    #ventana principal
    frameLeerProdu = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameLeerNombreProdu = Frame(frameLeerProdu, bg = backgroundColor[0])
    frameLeerAnnoProdu = Frame(frameLeerProdu, bg = backgroundColor[0])
    frameLeerDireccionProdu = Frame(frameLeerProdu, bg = backgroundColor[0])
    frameLeerProduBotones = Frame(frameLeerProdu, bg = backgroundColor[0])
    #labels
    labelLeerProdu = Label(frameLeerProdu, text = "Leer Nueva Compañía Productora", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerNombreProdu = Label(frameLeerNombreProdu, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerAnnoProdu = Label(frameLeerAnnoProdu, text= "Año de creación", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelLeerDireccionProdu = Label(frameLeerDireccionProdu, text= "Dirección", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])



    #funciones

    def volver():
        frameLeerProdu.pack_forget()
        return   


    #entrys
    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return volver()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servir, por favor intentelo más tarde.")
        return volver()

    listaProductoras = colors.getListaNombres(productoras)
    comboboxLeerNombreProdu = ttk.Combobox(frameLeerNombreProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")
    comboboxLeerNombreProdu["values"] = listaProductoras
    entryLeerAnnoProdu = Entry(frameLeerAnnoProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")
    entryLeerDireccionProdu = Entry(frameLeerDireccionProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")

    def cargarInfo(event):

        indice = 0
        for i in range (0, len(listaProductoras)):
            if listaProductoras[i] == comboboxLeerNombreProdu.get():
                indice = i
                break

                
        entryLeerAnnoProdu.config(state = "normal")
        entryLeerDireccionProdu.config(state = "normal")

        entryLeerAnnoProdu.delete(0, END)
        entryLeerDireccionProdu.delete(0, END)

        entryLeerAnnoProdu.insert(0, productoras[indice]["anno"])
        entryLeerDireccionProdu.insert(0,productoras[indice]["direccion"])

    comboboxLeerNombreProdu.bind("<<ComboboxSelected>>", cargarInfo)
    #botones

    botonVolverLeerProdu = Button(frameLeerProduBotones, text="Volver" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= volver)

    #packs
    frameLeerProdu.pack(fill = BOTH)
    labelLeerProdu.pack()
    frameLeerNombreProdu.pack(fill = X, pady = 25)
    frameLeerAnnoProdu.pack(fill = X , pady = 25)
    frameLeerDireccionProdu.pack(fill = X, pady = 25)
    frameLeerProduBotones.pack(fill=X , pady = 20)

    labelLeerNombreProdu.pack()
    labelLeerAnnoProdu.pack()
    labelLeerDireccionProdu.pack()

    comboboxLeerNombreProdu.pack()
    entryLeerAnnoProdu.pack()
    entryLeerDireccionProdu.pack()

    botonVolverLeerProdu.pack(side= TOP)


