import urllib.request
import urllib.error

def sortDict(dict):
    tmp = []
    for k,v in dict.items():
        tmp.append((v,k))
    return sorted(tmp)


# Contar ocurrencias de forma mas eficiente con el metodo .get()
dictionary = {}
try:
    data = urllib.request.urlopen("http://data.pr4e.org/mbox-short.txt")
    for line in data:
        line = line.decode("utf-8").strip()
        if line != "":
            dictionary[line] = dictionary.get(line,0) + 1

    # print(dictionary)

    # Ordenado por numero de apariciones
    print(sortDict(dictionary))
    
except urllib.error.URLError:
    print("Tiempo de espera agotado, compruebe su conexión a Internet o la disponibilidad de la web.")
