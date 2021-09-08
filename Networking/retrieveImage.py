import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysock.connect(("data.pr4e.org",80))

request = b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n"

img = b""


# sendall() se asegura de enviar toda la informacion que se le pase
mysock.sendall(request)

# Se recibe o no la respuesta
while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    img += data

# Se cierra la conexion porque ya recibio toda la informacion
mysock.close()

# Tamaño de la imagen (con la cabecera HTTP)
print("Img lenght:",len(img))

# Longitud de la cabecera
header = img.find(b"\r\n\r\n")
print("Header lenght:",header)
print("Header content:")
# Prints out from index 0 up to where header ends
print(img[:header].decode())


print("Bytes of Image")
print(len(img))

# Saves the cleaned data in hard drive
with open("Networking/savedImage.jpg","wb") as image:
    img = img[header+4:]
    image.write(img)
    print("Image saved successfully")
    