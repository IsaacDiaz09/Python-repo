class Fraccion:
    def __init__(self, n, d):
        # Inicializacion atributos
        self.__num = n
        self.__den = d
    
    def imprime(self):
        print(f"{self.__num}/{self.__den}")

print("Objeto a")
a = Fraccion(4,5)
a.imprime()
print("\nObjeto b")
b = Fraccion(8,9)
b.imprime()
