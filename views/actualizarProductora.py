from tkinter import ttk
from tkinter import *
import colors
import requests
import datetime

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


    #funciones

    def cancelar():
        frameActualizarProdu.pack_forget()
        return    

 


    #entrys
    productoras = cargarProductoras()
    if productoras == []:
        messagebox.showerror("Error", "No existen compañías productoras, por favor agregue una antes de continuar.")
        return cancelar()
    elif productoras[0] == []:
        messagebox.showerror("Error", "No se pudo establecer comunicación con el servir, por favor intentelo más tarde.")
        return cancelar()

    listaProductoras = colors.getListaNombres(productoras)
    comboboxActualizarNombreProdu = ttk.Combobox(frameActualizarNombreProdu, width = 40, font= ("Arial Bold", 15), state = "readonly")
    comboboxActualizarNombreProdu["values"] = listaProductoras
    entryActualizarAnnoProdu = Entry(frameActualizarAnnoProdu, width = 40, font= ("Arial Bold", 15))
    entryActualizarDireccionProdu = Entry(frameActualizarDireccionProdu, width = 40, font= ("Arial Bold", 15))

    def actualizar():
        idProd = colors.getIdByName(productoras, comboboxActualizarNombreProdu.get())
        year = datetime.date.today().year
        anno = entryActualizarAnnoProdu.get()
        nombre = comboboxActualizarNombreProdu.get()
        direccion = entryActualizarDireccionProdu.get()
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
                        res = colors.actualizarProductora(body, idProd)
                        messagebox.showinfo("Listo!", "Se actualizó la productora con éxito.")
                        frameActualizarProdu.pack_forget()
                    except requests.exceptions.ConnectionError:
                        messagebox.showerror("Error", "No se pudo establecer comunicación con el servidor, por favor intentelo más tarde.")
                    return  
 


    def cargarInfo(event):
        indice = 0
        for i in range (0, len(listaProductoras)):
            if listaProductoras[i] == comboboxActualizarNombreProdu.get():
                indice = i
                break
         
        entryActualizarAnnoProdu.config(state = "normal")
        entryActualizarDireccionProdu.config(state = "normal")

        entryActualizarAnnoProdu.delete(0, END)
        entryActualizarDireccionProdu.delete(0, END)

        entryActualizarAnnoProdu.insert(0, productoras[indice]["anno"])
        entryActualizarDireccionProdu.insert(0,productoras[indice]["direccion"])

    comboboxActualizarNombreProdu.bind("<<ComboboxSelected>>", cargarInfo)

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


