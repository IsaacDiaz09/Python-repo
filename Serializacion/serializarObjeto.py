import pickle
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
        return f"Marca: {self.marca}\nModelo : {self.modelo} \nEn marcha:\
{self.en_marcha}\nAcelera: {self.acelera} \nFrena: {self.frena}"

# Se añaden las instancias a una lista, y es esta la que se serializa
Coche1 = Vehiculos("Mazda","Mzd105")
Coche2 = Vehiculos("Renault","Rt110")
Coche3 = Vehiculos("Porshe","Psh009")

cochesSerializar = [Coche1,Coche2,Coche3]

with open("Serializacion/cochesSerializados","wb") as archivo:
    pickle.dump(cochesSerializar,archivo)

del archivo