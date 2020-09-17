class Point():
    #self: representa la instancia de una clase. Accedemos a los atributos y metodos de la clase
    #__init__ representa el constructor. Este meotdo se llama cuando se crea un objeto a partir
    # de una clase y permite que la clase inicialice los atributos de la clase
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2,8)
print(p.x)
print(p.y)