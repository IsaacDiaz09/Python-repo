import pickle
class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.en_marcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        return f"Marca: {self.marca}\nModelo : {self.modelo} \nEn marcha:\
{self.en_marcha}\nAcelera: {self.acelera} \nFrena: {self.frena}"

# Se añade la clase y dos instancias a la lista
Coche1 = Vehiculos("Mazda","Mzd105")
Coche2 = Vehiculos("Renault","Rt110")

cochesSerializar = [Vehiculos,Coche1,Coche2]

with open("Serializacion/cochesSerializados2","wb") as archivo:
    pickle.dump(cochesSerializar,archivo)

del archivo