#Me permite que una clase cambie segun la necesidad, en este caso calcularSuelod

class Empleado:
    def __init__(self, nombre, legado, sueldo):
        self.nombre = nombre
        self.legado = legado
        self.sueldoBruto = sueldo

    def calcularSueldo(self, descuentos):
        return self.sueldoBruto-descuentos

class Gerente(Empleado):
    #Nota: En python no me permite llamar mas de una vez el metodo con el mismo nombre
    #sobreescribo el metodo calcularSueldo() => recordemos que ya lo tenems en el padre
    def calcularSueldo(self, bonificaciones, descuentos = 0):#si solo quisiera un metodo con descuentos, lo que puedo hacer
        #es crear otro metodo llamado calcularSueldo(self, bonificaciones), pero en python no me permite
        #una solucion es poner un parametro inicializado en 0, pero tienes que ponerlo al final, caso contrario
        #tendras un error de tipo non-default
        return self.sueldoBruto-descuentos+bonificaciones


marco = Empleado("Marcos Rios", 221, 3000)
julia = Gerente("Julia Campos", 109, 60000)

marco.calcularSueldo(1000)
julia.calcularSueldo(1600, 100)