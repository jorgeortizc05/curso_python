#Para llamar una funcion necesitas importar
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

"""# si importas de esta manera
from functions
#tendras que concatenar para llamar a la funcion
for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")"""