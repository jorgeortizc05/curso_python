#La tupla es mas rapida, pero no permite introducir mas elementos una vez creadas

mitupla = ('Harry', 'Ron', 'Hermione',24,56) #tambien sin parentesis mitupla = 'Harry', 'Ron', etc

print(mitupla[0])

print(mitupla)

#convertir tupla a lista
milista = list(mitupla)  #tuple(milista) si deseas lista a tupla
print("Lista: ", milista)

print("Harry" in mitupla) #true o false si existe en la tupla o lista

#count: cuantas veces se repite un elemento
print(mitupla.count('Harry')) #Solo hay un harry en la tupla
#longitud de una tupla
print(len(mitupla)) #hay 5 elementos en este caso
#Tuplas unitarias: importante ponerle una coma al final
unico = ("juan",)

#Puedes separar en variables
mitupla = ("Juan", 12, 1 , 1995)
nombre, dia, mes, agno = mitupla
print(nombre, dia, mes, agno)