people = [
    {"name": "Harry", "hose": "Gryffndor"},
    {"name": "Cho", "hose": "Ravenclaw"},
    {"name": "Draco", "hose": "Slytherin"}

]

#Se ordena por nombre. se crear una funcion person y retorna el diccionario name
people.sort(key=lambda person: person["name"])

print(people)