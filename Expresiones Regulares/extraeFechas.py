import re

# Extraer las fechas del archivo que tengan el siguiente formato (dd,nn mm aa) hh:mm:ss
# y se almacenan en un archivo de texto
with open("Expresiones regulares/mbox-short.txt","r") as file:
    data = file.readlines()
    result = []
    for line in data:
        result += re.findall(r"Date: .*(\(?[a-zA-Z]{3}\, [\d]{1,2} [a-zA-Z]{3} [\d]{4}\)?) ([\d]{2}:[\d]{2}:[\d]{2})?",line)
    result = set(result)

    print("Se hallaron {} coincidencias".format(len(result)))
    
    with open("Expresiones regulares/fechasTxt.txt","w") as datesFile:
        datesFile.write("Fecha:\t\tHora:\n\n")
        for i in result:
            datesFile.write(f"{i[0]}\t{i[1]}\n")
        print("Se han escrito los datos en el archivo")
