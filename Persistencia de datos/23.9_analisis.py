frase_moficada = []

with open("txt/reporte.txt","r") as archivo:
    data = archivo.readlines()

for frase in data:
    frase_moficada.append(frase[:-1]+ " : " + str(len(frase)))

with open("txt/reporte_edit.txt","w") as archivo:
    for frase in frase_moficada:
        archivo.write(frase + "\n") 
