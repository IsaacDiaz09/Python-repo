import re
"""
Exercise 2: 

Write a program to look for lines of the form:
New Revision: 39772
"""

with open("Expresiones regulares/mbox.txt","r") as file:
    with open("Expresiones regulares/revisions.txt","w") as fileToWrite:    
        data = file.readlines()
        for line in data:
            if re.search(r"^New Revision: [\d]+",line):
                fileToWrite.write(line)
        print("Se han escrito las coincidencias en el archivo de texto")
