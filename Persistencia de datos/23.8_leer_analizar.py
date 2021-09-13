frases = []

with open("txt/reporte.txt","r") as file:
    for linea in file.readlines():
        #print(linea,end="")
        frases.append(linea.split())

for linea in frases:
    for palabra in linea:
        for letra in palabra:
            print(letra)