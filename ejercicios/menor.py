"""
Hallar el menor de dos numeros enteros positivos sin utilizar condicionales ni
operadores ternarios. Suponer que los numeros no son iguales
"""

#Opcion 1: Decrementos sucesivos
#los numeros tambien se comportan como boleanos
#0 = false ; cualquier_numero = true
def menor(a, b):
    m = 0

    while a and b:
        a = a -1
        b = b - 1
        m = m + 1

    return m

print("Decremento sucesivos: ", menor(54,9))

#Opcion 2: Mediante un arreglo
#Los booleanos se combierte en numeros
#false = 0 ; True = 1
def menor2(a,b):
    arreglo = [a,b]
    return arreglo [a > b] #retorna el numero segun la posicion True = 1 o False = 0

print("Mediante arreglo: ", menor2(10,3))

#Opcion 3: Valor numerico de bool
def menor3(a, b):
    return (a>b)*b + (b>a)*a

print("Valor numerico de bool: ", menor3(10,23))


