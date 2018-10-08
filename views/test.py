import requests


r = requests.get('http://localhost:3000/productoras/readAll')
pelis=  r.json()

print (pelis)





