from serializarObjeto import Vehiculos
import pickle

with open("Serializacion/cochesSerializados","rb") as fichero:
    misCoches = pickle.load(fichero)
"""
Si no se importa la clase -Vehiculos-
<serializarObjeto.Vehiculos object at 0x000001529A7C2FD0>
<serializarObjeto.Vehiculos object at 0x000001529A7C2F70>
<serializarObjeto.Vehiculos object at 0x000001529A7C2F40>
"""
for c in misCoches:
    print(c.estado())
    print("------")
# Serializar directamente la clase junto a sus instancias...