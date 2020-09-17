#Set: es una coleccion que no esta ordenada ni indexada y se mete en llaves.

#Create an empty set
s = set()

#Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) #Los sets no admite valores repetidos. No se agrega a la cadena
print(s)

s.remove(2)
print(s)

#f me permite introducir parametros en println enter {}
#len devuelve el tamaño de la cadena
print(f"The set has {len(s)} elements.")
