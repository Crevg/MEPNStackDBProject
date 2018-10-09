import requests
from tkinter import *
import colors
from agregarPeli import agregarPeliWindow
from leerPeli import leerPeliWindow
from actualizarPeli import actualizarPeliWindow
from eliminarPeli import eliminarPeliWindow
from agregarProductora import agregarProduWindow
from leerProductora import leerProduWindow
from actualizarProductora import actualizarProduWindow
from eliminarProductora import eliminarProduWindow


#main window
#colores
backgroundColor = colors.backgroundColor
foregroundColor = colors.foregroundColor

root = Tk()
root.title("Películas")
root.config(bg= backgroundColor[0])
root.geometry('700x500')


def nextWindow(action):
    if action == "selección":
        homeFrame.pack(fill = BOTH)
    elif action == "agregarpeli":
        homeFrame.pack_forget()
        agregarPeliWindow(root)  
    elif action == "leerpeli":
        homeFrame.pack_forget() 
        leerPeliWindow(root)
    elif action == "actualizarpeli":
        homeFrame.pack_forget()
        actualizarPeliWindow(root)
    elif action == "eliminarpeli":
        homeFrame.pack_forget()
        eliminarPeliWindow(root)
    elif action == "agregarprodu":
        homeFrame.pack_forget()
        agregarProduWindow(root)
    elif action == "leerprodu":
        homeFrame.pack_forget()
        leerProduWindow(root)
    elif action == "actualizarprodu":
        homeFrame.pack_forget()
        actualizarProduWindow(root)
    elif action == "eliminarprodu":
        homeFrame.pack_forget()
        eliminarProduWindow(root)
    elif action == "portitulo":
        homeFrame.pack_forget()
    elif action == "porfranquicia":
        homeFrame.pack_forget()
    elif action == "poraño":
        homeFrame.pack_forget()
    elif action == "porprodu":
        homeFrame.pack_forget()
    homeFrame.pack(fill = BOTH)


#################################################################VENTANA DE SELECCION#################################################################
homeFrame = Frame(root, width = 700, height = 500, bg = backgroundColor[0])

#elementos de la ventana
labelBienvenido = Label(homeFrame, text= "Bienvenido\nSeleccione una opción para continuar", font= ("Arial Bold", 20), fg= foregroundColor[0], bg=backgroundColor[0])
#peliculas

labelPeliculas = Label(homeFrame, text= "Películas", font= ("Arial Bold", 20), fg= foregroundColor[1], bg=backgroundColor[1])
frameBotonesPelicula = Frame(homeFrame)
botonCPeli = Button(frameBotonesPelicula, text="Agregar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= lambda:nextWindow("agregarpeli"))
botonRPeli = Button(frameBotonesPelicula, text="Leer" , width= 10 ,font= ("Arial Bold", 15), bg = backgroundColor[4], command= lambda:nextWindow("leerpeli"))
botonUPeli = Button(frameBotonesPelicula, text="Actualizar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= lambda:nextWindow("actualizarpeli"))
botonDPeli = Button(frameBotonesPelicula, text="Eliminar" , width= 10 , font= ("Arial Bold", 15) , bg = backgroundColor[4], command= lambda:nextWindow("eliminarpeli"))

#productoras
labelProductoras = Label(homeFrame, text= "Compañías productoras", font= ("Arial Bold", 20), fg= foregroundColor[1], bg=backgroundColor[2])
frameBotonesProductoras = Frame(homeFrame)
botonCProdu = Button(frameBotonesProductoras, text="Agregar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= lambda:nextWindow("agregarprodu"))
botonRProdu = Button(frameBotonesProductoras, text="Leer" , width= 10 ,font= ("Arial Bold", 15), bg = backgroundColor[4], command= lambda:nextWindow("leerprodu"))
botonUProdu = Button(frameBotonesProductoras, text="Actualizar" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4],command= lambda:nextWindow("actualizarprodu"))
botonDProdu = Button(frameBotonesProductoras, text="Eliminar" , width= 10 , font= ("Arial Bold", 15) , bg = backgroundColor[4],command= lambda:nextWindow("eliminarprodu"))

#consultas básicas
labelConsultas = Label(homeFrame, text= "Consultas básicas", font= ("Arial Bold", 20), fg= foregroundColor[1], bg=backgroundColor[3])
frameBotonesConsultas = Frame(homeFrame)
botonCConsultas = Button(frameBotonesConsultas, text="Por título" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4],command= lambda:nextWindow("portitulo"))
botonRConsultas = Button(frameBotonesConsultas, text="Por franquicia" , width= 10 ,font= ("Arial Bold", 15), bg = backgroundColor[4],command= lambda:nextWindow("porfranquicia"))
botonUConsultas = Button(frameBotonesConsultas, text="Por año" , width= 10, font= ("Arial Bold", 15), bg = backgroundColor[4], command= lambda:nextWindow("poraño"))
botonDConsultas = Button(frameBotonesConsultas, text="Por productora" , width= 10 , font= ("Arial Bold", 15) , bg = backgroundColor[4], command= lambda:nextWindow("porprodu"))

labelBienvenido.pack(side=TOP, pady = 30)
labelPeliculas.pack(side=TOP,fill = X, pady = 10)
frameBotonesPelicula.pack(side=TOP, pady = 10)
botonCPeli.pack(side=LEFT)
botonRPeli.pack(side=LEFT)
botonUPeli.pack(side=LEFT)
botonDPeli.pack(side=LEFT)
labelProductoras.pack(side=TOP, fill = X, pady = 10)
frameBotonesProductoras.pack(side=TOP, pady = 10)
botonCProdu.pack(side=LEFT)
botonRProdu.pack(side=LEFT)
botonUProdu.pack(side=LEFT)
botonDProdu.pack(side=LEFT)
labelConsultas.pack(side=TOP, fill = X, pady = 10)
frameBotonesConsultas.pack(side=TOP, pady = 10)
botonCConsultas.pack(side=LEFT)
botonRConsultas.pack(side=LEFT)
botonUConsultas.pack(side=LEFT)
botonDConsultas.pack(side=LEFT)

###########################################################################VENTANA DE AGREGAR PELICULAS##############################################################


#llama a la ventana principal
nextWindow("selección")
#ciclo del programa
root.mainloop()

