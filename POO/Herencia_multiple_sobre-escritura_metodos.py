# POO VII
# Herencia múltiple y sobre escritura de métodos.

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
        print(f"Marca: {self.marca}\nModelo : {self.modelo} \nEn marcha: \
{self.en_marcha}\nAcelera: {self.acelera} \nFrena: {self.frena}")


# Clase 'autobus'
class autobus(Vehiculos):
    def carga(self, personas):
        self.carga_personas = personas
        if (self.carga_personas):
            self.carga_personas = "El autobus lleva pasajeros"
        else:
            self.carga_personas = "El autobus no lleva pasajeros"
        
    def estado(self):
        print(f"Marca: {self.marca}\nModelo : {self.modelo} \nEn marcha: \
{self.en_marcha}\nAcelera: {self.acelera} \nFrena: {self.frena}\n\
{self.carga_personas}")

print()
print("--- Mi autobus ---")
miAutobus = autobus("Cars", "FX700")
print()
miAutobus.arrancar()
miAutobus.carga(True)
miAutobus.estado()


# Clase 'motocicleta'
class motocicleta(Vehiculos):
    hace_caballito = ""
    
    def caballito(self):
        self.hace_caballito = "Voy haciendo el caballito"
    def estado(self):
        print(f"Marca: {self.marca}\nModelo : {self.modelo} \nEn marcha: \
{self.en_marcha}\nAcelera: {self.acelera} \nFrena: {self.frena}\n\
{self.hace_caballito}")
# Se sobreescribe el método estado de la clase motocicleta por el heredado
# con el fin de agregarle el aviso de 'caballito'
miMoto = motocicleta("Suzuki","XF1")
"""
Esos dos parametros se acomodararan en las posiciones de 'marca' y 'modelo' de
la clase padre 'Vehiculos' y serán heredados a la instancia 'miMoto' creada con 
la clase 'motocicleta' 
"""
print()
# Mi moto tiene 6 comportamientos, 5 heredados y 1 propio 
print("--- Mi motocicleta ---")

miMoto.caballito() # Se llama al método 'caballito'
miMoto.estado() 
# Se le pregunta el estado, se muestra el declarado en la clase 'motocicleta'.
print()

""" Clase 'vehiculos electricos', esta clase a diferencia de las demás, no 
hereda nada de 'Vehiculos' """

class vehiculos_electricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    
    def cargar_Energia(self):
        self.cargado = True
        self.autonomia -=  20

class Bici_electrica(vehiculos_electricos):
    def estado(self):
        super().estado()
        print(f"Autonomia: {self.autonomia}")

print("-- Mi bici electrica --")
mi_bici = Bici_electrica("Tesla", "Ts125")
mi_bici.arrancar()
mi_bici.acelerar()
mi_bici.estado()
print()
