# POO VI
# Herencia:

class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Tomaran el valor que les sea pasado como argumento en su llamada
        self.en_marcha = False
        self.acelera = False
        self.frena = False
        # Por defecto estan desactivados esos comportamientos, en 'False' hasta
        # que se indique lo contrario
    
    def arrancar(self):
        self.en_marcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print(f"Marca: {self.marca}\nModelo : {self.modelo} \nEn marcha:\
{self.en_marcha}\nAcelera: {self.acelera} \nFrena: {self.frena}")

class motocicleta(Vehiculos):
    pass
    # Para que no de error, como tal ya hereda todo de Vehiculos

"""
Esos dos parametros se acomodararan en las posiciones de 'marca' y 'modelo' de
la clase padre 'Vehiculos' y serán heredados a la instancia 'miMoto' creada con 
la clase 'motocicleta' 
"""

print("Mi motocicleta")
miMoto = motocicleta("Suzuki","XF1")
print()
miMoto.estado()
print()
