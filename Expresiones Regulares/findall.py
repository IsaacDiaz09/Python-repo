import re

# Usando el metodo findall() para extraer todos los substrings que coinciden con el patron de busqueda
str = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Return-Path: <postmaster@collab.sakaiproject.org> \
for <source@collab.sakaiproject.org>; Received: (from apache@localhost) Author: stephen.marquard@uct.ac.za"

result =  re.findall(r"\w{1}\S+@\S+\w{1}",str)
# Debe iniciar con 1 caracter alfanumerico, le siguen n cantidad de caracteres de no espacio despues tiene una @
# le siguen n caracteres no espacio y 1 caracter alfanumerico, se corta cuando encuentra un espacio en blanco

print(result)
print("Se encontraron {} coincidencias".format(len(result)))

# Salida:
"""
[
    'stephen.marquard@uct.ac.za', 
    'postmaster@collab.sakaiproject.org', 
    'source@collab.sakaiproject.org', 
    'apache@localhost', 
    'stephen.marquard@uct.ac.za'
]
Se encontraron 5 coincidencias
"""
