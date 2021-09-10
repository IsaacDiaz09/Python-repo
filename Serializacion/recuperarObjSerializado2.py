import pickle

with open("Serializacion/cochesSerializados2","rb") as fichero:
    misCoches = pickle.load(fichero)

print(misCoches[1].estado())
# No no anda
"""
AttributeError: Can't get attribute 'Vehiculos' on <module '__main__' from 'd:\\ESTUDIO\\Repositorios\\Python\\Serializacion\\recuperarObjSerializado2.py'>
"""
# Se debe siempre traer la o las clases bajo la que se instanciaron los objetos
