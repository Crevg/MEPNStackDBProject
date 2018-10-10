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
    
def agregarPelicula(body):
    return requests.post("http://localhost:3000/peliculas/create", json = body)

def leerPelicula():
    return requests.get("http://localhost:3000/peliculas/readAll")

def actualizarPelicula(body, id):
    return requests.put("http://localhost:3000/peliculas/"+id+"/update", json = body)

def borrarPelicula(id):
    return requests.delete("http://localhost:3000/peliculas/"+id+"/del")

def agregarProductora(body):
    return requests.post("http://localhost:3000/productoras/create", json = body)

def leerProductoras():
    return requests.get("http://localhost:3000/productoras/readAll")

def actualizarProductora(body, id):
    return requests.put("http://localhost:3000/productoras/"+id+"/update", json = body)

def borrarProductora(id):
    return requests.delete("http://localhost:3000/productoras/"+id+"/del")

def buscarPorTitulo(titulo):
    res = requests.get("http://localhost:3000/peliculas/"+titulo+"/porTitulo")
    return res

def buscarPorFranquicia(franquicia):
    res = requests.get("http://localhost:3000/peliculas/"+franquicia+"/porFranquicia")
    return res

def buscarPorAnno(inicial, final):
    res = requests.get("http://localhost:3000/peliculas/"+str (inicial)+"/" + str(final)+"/porAnno")
    return res

def buscarPorProductoraDatos(idProd):    
    res = requests.get("http://localhost:3000/peliculas/"+idProd+"/porProductora/datos")
    return res

def buscarPorProductoraDuracion(idProd):
    res = requests.get("http://localhost:3000/peliculas/"+idProd+"/porProductora/duraciones")
    return res
