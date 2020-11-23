#Tiene un key y un valor. Se mete en llaves
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

#Agrego valores al diccionario
houses["Hermione"] = "Gryffindor"

print("La casa de Harry es ", houses["Harry"])
print(houses)

#Eliminar un valor del diccionario
del houses["Draco"]
print(houses)

mi_diccionario = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(mi_diccionario)

mi_diccionario = {23:"Jordan","Nombre":"Michael","anillos":[1991,1992,1993,1996,1997,1998]}
print("Obtengo datos de la clave anillos: ", mi_diccionario["anillos"])
print("Keys: ", mi_diccionario.keys())
print("Values: ", mi_diccionario.values())
print("Longitud del diccionario: ", len(mi_diccionario))