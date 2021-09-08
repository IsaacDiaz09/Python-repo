# https://www.py4e.com/html3/12-network
import socket
import re
# configurado para streams de datos funcionando en IPv4
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
# Conexion con el socket con el puerto que maneja, se pasa como una tupla
# Un socket es la combinacion de una direccion IP + el puerto del servicio que usa

"""Hacer un solicitud HTTP teniendo ya el Socket"""

request = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(request)
"""
· Encabezado:

HTTP/1.1 200 OK
Date: Wed, 08 Sep 2021 00:31:50 GMT
Server: Apache/2.4.18 (Ubuntu)     
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

· Cuerpo:

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""
response = ""
# Se recibe o no la respuesta
while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    response += data.decode()
print(response)

# Cierre de la conexion
mysock.close()

# Descartando la cabecera HTTP para ver solo el contenido
for line in response.split("\n"):
    r = re.findall(r"^[^\r].*[^\r]$",line)
    if r != []:
        print(r[0])

"""
· Se obtiene solo el cuerpo del mensaje:

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""
