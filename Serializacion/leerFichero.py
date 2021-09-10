import pickle

# Read binary -> Lectura binaria
with open("Serializacion/lista_prueba","rb") as archivo:
    lista_recuperada = pickle.load(archivo)

print(lista_recuperada)
# -> ['Pedro', 'Isaac', 'Roberto', 'Isabela']