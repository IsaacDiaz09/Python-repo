import re
string = "From: Using the : blablabla"
r = re.findall(r"^F.+:",string)
print(r)

"""
Salida:
['From: Using the :']
· Muestra el string mas largo ya que como tal hay dos coincidencias en la linea
"""

r = re.findall(r"^F.+?:",string)
print(r)
"""
Salida:
['From:']
"""