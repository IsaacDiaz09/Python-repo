# https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping
# https://stackoverflow.com/questions/45086383/python-requests-403-forbidden-despite-setting-user-agent-headers
# https://docs.python.org/es/3/library/urllib.html

import urllib.request
import urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

"""https://docs.python.org/3.0/library/urllib.request.html#urllib.request._urlopener"""
# Clase que sobre-escribe el agente de usuario evitando un error '403:Prohibido'
class AppUrlOpener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppUrlOpener()
data = opener.open("https://www.py4e.com/html3/12-network")


with open("Networking/html.txt","w",encoding="utf-8") as file:
    for line in data:
        file.write(line.decode())
