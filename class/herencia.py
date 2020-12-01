class Empleado:
    #Siempre en una clase un metodo contiene un self
    #El constructor se define con __init__
    def __init__(self, nombre, edad, legajo, salario):
        self.nombre = nombre
        self.edad = edad
        self.legajo = legajo
        self.salario = salario

    def calcularSalario(self, descuentos, bonos): #contiene un self, siempre si esta dentro de una clase
        return self.salario - descuentos + bonos

class AgenteVentas(Empleado): #Entre parentesis llamas a la clase padre.
    def __init__(self, nombre, edad, legajo, salario, mostrador): #sobreescribo el metodo __init__ de la clase padre
        self.numeroMostrador = mostrador
        super().__init__(nombre,edad,legajo,salario) #a pesar de sobreescribir, puedo llamar al __init__ de la clase padre

class Tripulante(Empleado): #Llamo a mi clase padre, esta es otra herencia
    def mostrarRenovacionLicencia(self):
        if self.edad < 50:
            print("Renueva su licencia cada 1 anio")
        else:
            print("Renueva su licencia cada 6 meses")


jorge = AgenteVentas("Jorge Ortiz",28,"ACJ89",2500,4)
print(jorge.calcularSalario(50, 500))

pepe = Tripulante("Jose Ortiz", 55, "PO34",700)
print(pepe.mostrarRenovacionLicencia())