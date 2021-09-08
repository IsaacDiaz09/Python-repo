class Coche:
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

"""
Vehiculo_1 = Moto()
print()
Vehiculo_1.desplazamiento()

Vehiculo_2 = Coche()
print()
Vehiculo_2.desplazamiento()

Vehiculo_3 = Camion()
print()
Vehiculo_3.desplazamiento()
print()
"""

def desplaza_vehiculo(vehiculo):
    vehiculo.desplazamiento()

print("A tráves de polimorfismo")
mi_camion = Camion()
print("Tipo:",type(mi_camion))
desplaza_vehiculo(mi_camion)

print()
print("Método común")
mi_camion = Camion()
mi_camion.desplazamiento()

"""
Ambos entregan el mismo resultado pero con polimorfismo es 
mas flexible y dinamico.
"""
