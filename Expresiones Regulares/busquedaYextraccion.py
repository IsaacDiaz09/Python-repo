import re

# Se lee un archivo y se le aplica el patron para obtener todos los mensajes de id en el 
with open("Expresiones regulares\mbox.txt","r") as file:
    cont = 0
    data = file.readlines()
    result = []
    with open("Expresiones regulares\IDmsgs.txt","w") as ids:
        for line in data:
            result += re.findall(r"Message-ID: \S*",line)
        # para eliminar duplicados
        result = set(result)
        for id in sorted(result):
            cont += 1
            ids.write("{}: {}\n".format(cont,id))
        print("Se ha finalizado la escritura de los Ids de msg.")
        print("Se han escrito {} registros.".format(len(result)))
