with open("txt/lorem_ipsum.txt","r") as archivo:
    for linea in archivo:
        # print(linea)
        if linea[-1] == '\n':
            linea = linea[:-1]
        print(linea)
