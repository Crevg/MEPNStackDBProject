from tkinter import ttk
from tkinter import *
import colors
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor



def actualizarProduWindow(root):
    #ventana principal
    frameActualizarProdu = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameActualizarNombreProdu = Frame(frameActualizarProdu, bg = backgroundColor[0])
    frameActualizarAnnoProdu = Frame(frameActualizarProdu, bg = backgroundColor[0])
    frameActualizarDireccionProdu = Frame(frameActualizarProdu, bg = backgroundColor[0])
    frameActualizarProduBotones = Frame(frameActualizarProdu, bg = backgroundColor[0])
    #labels
    labelActualizarProdu = Label(frameActualizarProdu, text = "Actualizar Compañía Productora", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarNombreProdu = Label(frameActualizarNombreProdu, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarAnnoProdu = Label(frameActualizarAnnoProdu, text= "Año de creación", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelActualizarDireccionProdu = Label(frameActualizarDireccionProdu, text= "Direccion", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys
    listaProductoras = ["ab" , "bb", "cb"] 
    comboboxActualizarNombreProdu = ttk.Combobox(frameActualizarNombreProdu, width = 40, font= ("Arial Bold", 15), state = "readonly")
    comboboxActualizarNombreProdu["values"] = listaProductoras
    entryActualizarAnnoProdu = Entry(frameActualizarAnnoProdu, width = 40, font= ("Arial Bold", 15))
    entryActualizarDireccionProdu = Entry(frameActualizarDireccionProdu, width = 40, font= ("Arial Bold", 15))


    #funciones

    def cancelar():
        frameActualizarProdu.pack_forget()
        return    

    def actualizar():
        #FALTA LÓGICA DE Actualizar
        frameActualizarProdu.pack_forget()
        return  

    #botones

    botonAceptarActualizarProdu = Button(frameActualizarProduBotones, text="Actualizar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= actualizar)
    botonCancelarActualizarProdu = Button(frameActualizarProduBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= cancelar)

    #packs
    frameActualizarProdu.pack(fill = BOTH)
    labelActualizarProdu.pack()
    frameActualizarNombreProdu.pack(fill = X, pady = 25)
    frameActualizarAnnoProdu.pack(fill = X , pady = 25)
    frameActualizarDireccionProdu.pack(fill = X, pady = 25)
    frameActualizarProduBotones.pack(fill=X , pady = 20)

    labelActualizarNombreProdu.pack()
    labelActualizarAnnoProdu.pack()
    labelActualizarDireccionProdu.pack()

    comboboxActualizarNombreProdu.pack()
    entryActualizarAnnoProdu.pack()
    entryActualizarDireccionProdu.pack()

    botonCancelarActualizarProdu.pack(side= RIGHT, padx = 100)
    botonAceptarActualizarProdu.pack(side = RIGHT, padx = 100)


