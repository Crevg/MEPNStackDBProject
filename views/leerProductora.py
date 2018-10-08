from tkinter import ttk
from tkinter import *
import colors
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor



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

    #entrys

    listaProductoras = ["ab" , "bb", "cb"] 
    comboboxLeerNombreProdu = ttk.Combobox(frameLeerNombreProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")
    comboboxLeerNombreProdu["values"] = listaProductoras
    entryLeerAnnoProdu = Entry(frameLeerAnnoProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")
    entryLeerDireccionProdu = Entry(frameLeerDireccionProdu, width = 40, font= ("Arial Bold", 15), state= "readonly")


    #funciones

    def volver():
        frameLeerProdu.pack_forget()
        return    

  

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


