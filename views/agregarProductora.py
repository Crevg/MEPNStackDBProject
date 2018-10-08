from tkinter import ttk
from tkinter import *
import colors
import datetime
import requests
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor



def agregarProduWindow(root):
    #ventana principal
    frameAgregarProdu = Frame(root, width = 700, height = 500, bg = backgroundColor[0]) 

    #frames

    frameAgregarNombreProdu = Frame(frameAgregarProdu, bg = backgroundColor[0])
    frameAgregarAnnoProdu = Frame(frameAgregarProdu, bg = backgroundColor[0])
    frameAgregarDireccionProdu = Frame(frameAgregarProdu, bg = backgroundColor[0])
    frameAgregarProduBotones = Frame(frameAgregarProdu, bg = backgroundColor[0])
    #labels
    labelAgregarProdu = Label(frameAgregarProdu, text = "Agregar Nueva Compañía Productora", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarNombreProdu = Label(frameAgregarNombreProdu, text= "Nombre", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarAnnoProdu = Label(frameAgregarAnnoProdu, text= "Año de creación", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])
    labelAgregarDireccionProdu = Label(frameAgregarDireccionProdu, text= "Dirección", font= ("Arial Bold", 15), fg= foregroundColor[0], bg=backgroundColor[0])

    #entrys

    listaProductoras = ["ab" , "bb", "cb"] 
    entryAgregarNombreProdu = Entry(frameAgregarNombreProdu, width = 40, font= ("Arial Bold", 15))
    entryAgregarAnnoProdu = Entry(frameAgregarAnnoProdu, width = 40, font= ("Arial Bold", 15))
    entryAgregarDireccionProdu = Entry(frameAgregarDireccionProdu, width = 40, font= ("Arial Bold", 15))


    #funciones

    def cancelar():
        frameAgregarProdu.pack_forget()
        return    

    def agregar():
        year = datetime.date.today().year
        anno = entryAgregarAnnoProdu.get()
        nombre = entryAgregarNombreProdu.get()
        direccion = entryAgregarDireccionProdu.get()
        if not nombre or not direccion:
            messagebox.showerror("Error","Debe llenar todos los campos")
        elif not anno:
            messagebox.showerror("Error", "Por favor inserte un año válido")
        else:
            valido = False
            try:
                anno = int (anno)
                valido = True
            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número")
                valido = False
            if valido:
                if anno > year or anno < 1900:
                    messagebox.showerror("Error", "Por favor inserte un año válido")

                else:
                    body = {"nombre":nombre, "anno":anno, "direccion":direccion}
                    try:
                        res = colors.agregarProductora(body)
                        messagebox.showinfo("Listo!", "Se agregó la productora con éxito.")
                        frameAgregarProdu.pack_forget()
                    except requests.exceptions.ConnectionError:
                        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
                    return  

    #botones

    botonAceptarAgregarProdu = Button(frameAgregarProduBotones, text="Agregar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= agregar)
    botonCancelarAgregarProdu = Button(frameAgregarProduBotones, text="Cancelar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= cancelar)

    #packs
    frameAgregarProdu.pack(fill = BOTH)
    labelAgregarProdu.pack()
    frameAgregarNombreProdu.pack(fill = X, pady = 25)
    frameAgregarAnnoProdu.pack(fill = X , pady = 25)
    frameAgregarDireccionProdu.pack(fill = X, pady = 25)
    frameAgregarProduBotones.pack(fill=X , pady = 20)

    labelAgregarNombreProdu.pack()
    labelAgregarAnnoProdu.pack()
    labelAgregarDireccionProdu.pack()

    entryAgregarNombreProdu.pack()
    entryAgregarAnnoProdu.pack()
    entryAgregarDireccionProdu.pack()

    botonCancelarAgregarProdu.pack(side= RIGHT, padx = 100)
    botonAceptarAgregarProdu.pack(side = RIGHT, padx = 100)


