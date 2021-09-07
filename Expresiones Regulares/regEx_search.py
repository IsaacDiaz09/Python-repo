import re
import urllib.request

# Practica FCC curso Python para todos expresiones regulares
try:
    data = urllib.request.urlopen("http://data.pr4e.org/authors.txt")
    for line in data:
        line = line.decode("utf-8").rstrip()
        if re.search(r"^(English|Spanish)",line):
            print(line)
except urllib.error.URLError:
    print("Tiempo de espera agotado, compruebe su conexión a Internet o la disponibilidad de la web.")

"""
Salida: 
English,Charles Severance
English,Sue Blumenberg
English,Elloitt Hauser
Spanish,Fernando Tardío Muñiz
"""