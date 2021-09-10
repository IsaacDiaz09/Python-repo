import pickle

lista_prueba = ["Pedro","Isaac","Roberto","Isabela"]

# Write binary -> Escritura binaria
with open("Serializacion/lista_prueba","wb") as archivo:
    pickle.dump(lista_prueba,archivo)
del archivo
