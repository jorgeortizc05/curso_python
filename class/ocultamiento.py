class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = {}

    def anadirMateria(self, id,  nombre):
        self.materias[id] = nombre

class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre = nombre
        self.profesor = profesor
        #no puede ser anterior a 2006
        self.fechaInicioDictado = fecha

    #getter and setter
    @property #getter
    def fechaInicioDictado(self):
        print("getter fechaInicioDictado")
        return self._fechaInicioDictado #este metodo esta protegido

    @fechaInicioDictado.setter #setter
    def fechaInicioDictado(self, fecha):
        if fecha > 2006:
            self._fechaInicioDictado = fecha
        else:
            self._fechaInicioDictado = 2006



ing = Carrera("Ingenieria")
algebra = Materia("Algebra", "Ricardo Quinteros", 2010)
fisica = Materia("Fisica", "Margarita Gomez", 2006)
quimica = Materia("Quimica", "Lorena Rios", 2001)


ing.anadirMateria(100, algebra)

print(ing.materias)
print(algebra.fechaInicioDictado)
print(fisica.fechaInicioDictado)
print(quimica.fechaInicioDictado)