class Coche:
    def __init__(self, gasolina): 
        self.gasolina = gasolina
        print("Tenemos", gasolina , "litros")
    
    def arrancar(self): 
        if self.gasolina > 0: 
            print("Arranca")
        else: 
            print("No arranca")
    def conducir(self):
        # while self.gasolina > 0: 
        if self.gasolina > 0: 
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else: 
            print("No se mueve")

Coche_isaac = Coche(15)
Coche_isaac.arrancar()
Coche_isaac.conducir()

""" 
Se crea una clase llamda 'coche', se crea una instancia de ella llamada
'Coche_isaac' y se le asignan 15 litros de gasolina. Una vez se enciende y 
empieza a conducir gastará de a 1 litro hasta que se agote (si usamos 'while'),
por otro lado, con if, solo gastará 1 litro cuando se llame el método.
Ambos solo funcionan si litros >= 0.
"""