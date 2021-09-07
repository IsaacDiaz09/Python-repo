import re
import urllib.request
from datetime import datetime
import urllib.error

try:
    # Practica del curso de FCC de python para todos, regEx
    # Se obtiene un archivo de texto en la internet y se le saca la informacion que pasa el patron
    data = urllib.request.urlopen("http://data.pr4e.org/mbox-short.txt")
    result = []
    # Debe iniciar con 1 caracter alfanumerico, le siguen n cantidad de caracteres alfanbeticos, una @
    # le siguen n caracteres alfabeticos y todos estos deben estar seguidos de un punto
    for line in data:
        line = line.decode("utf-8").strip()
        result += re.findall(r"\w+@[a-zA-Z\.]{2,}[a-zA-Z]{1}",line)

    # Se pone dentro de un set para descartar las posibles repeticiones
    result = set(result)
    print(result)
    print("Se encontraron {} direcciones de correo electronico en el archivo".format(len(result)))

    """Ejemplo salida: [stephen.marquard@uct.ac.za]"""

    # los guardamos en un fichero txt
    with open("Expresiones regulares/emails.txt","w") as file:
        contador = 0
        file.write("Archivo escrito el: {}\n".format(datetime.now()))
        for email in result:
            contador += 1
            file.write("{}: {}\n".format(contador,email))

except urllib.error.URLError:
    print(":(... No fue posible extraer la información del fichero, revisa tu conexión y/o la disponibilidad de la web")
