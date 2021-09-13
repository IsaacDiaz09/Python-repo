import re

cont = 0
# Obtener todos los enlaces que tenga la pagina web con el html ya extraiso
with open("Networking/html.txt","r",encoding="utf-8") as file:
    data = file.readlines()
    
    for line in data:
        # RegEx para filtrar los links
        links = re.findall(r'href="(http[s]?://.*?)"',line)
        for link in links:
            # Se escriben las coincidencias en otro texto
            with open("Networking/links.txt","a",encoding="utf-8") as f:
                f.write(link+"\n")
            cont += 1
            print(link)
    print("{} enlaces encontrados en el html".format(cont))

"""
· Salida:

https://static.tsugi.org/bootstrap-3.4.1/css/bootstrap.min.css
https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.css
https://static.tsugi.org/fontawesome-free-5.8.2-web/css/all.css
https://static.tsugi.org/fontawesome-free-5.8.2-web/css/v4-shims.css
https://static.tsugi.org/css/tsugi2.css
https://www.py4e.com
https://www.py4e.com/lessons
https://www.py4e.com/discussions
https://www.py4e.com/materials
http://www.dr-chuck.com
http://www.dr-chuck.com/office/
https://www.py4e.com/book
https://www.py4e.com/login
https://www.w3.org/Protocols/rfc2616/rfc2616.txt
https://www.py4e.com
http://” or “href=
https://pypi.python.org/pypi/beautifulsoup4
https://packaging.python.org/tutorials/installing-packages/
http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
https://www.py4e.com/code3
http://www.crummy.com
https://github.com/csev/py4e/tree/master/book3
22 enlaces encontrados en el html
"""