#Llaman a funciones de orden superior

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
        f()
    return wrapper

@announce #Llamo a mi funcion announce(hello)
def hello():
    print("Hello, world!")

hello()