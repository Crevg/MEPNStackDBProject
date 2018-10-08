import requests

#global var
backgroundColor = ["cyan2", "red", "green", "blue", "white"]
foregroundColor = ["red3", "white"]

def getListaNombres(json):
    nombres = []
    for i in range (0, len(json)):
        nombres.append(json[i]["nombre"])
    return nombres

def getIdByIndex(json, index):
    return json[index]["_id"]    

def getIdByName(json, name):
    for i in range (0, len(json)):
        if json[i]["nombre"] == name:
            return json[i]["_id"]
    

def leerPelicula():
    return requests.get("http://localhost:3000/peliculas/readAll")

def borrarPelicula(id):
    return requests.delete("http://localhost:3000/peliculas/"+id+"/del")

def agregarProductora(body):
    return requests.post("http://localhost:3000/productoras/create", json = body)

def leerProductoras():
    return requests.get("http://localhost:3000/productoras/readAll")

def borrarProductora(id):
    return requests.delete("http://localhost:3000/productoras/"+id+"/del")
