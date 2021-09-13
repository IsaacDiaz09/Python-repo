with open("txt/personas.txt","r",encoding="utf-8") as archivo:
    diccionario_personas = {}
    personas = []
    lineas = archivo.readlines()
    for linea in lineas:
        if linea[-1] == '\n':
            linea = linea[:-1]
            personas.append(linea.split(";"))
        else:
            personas.append(linea.split(";"))
    print()
    for i in personas:
        diccionario_personas[i[0]] = i[1:4]
    print(diccionario_personas)
    print()
    