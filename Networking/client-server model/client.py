import socket
import threading
import sys

PORT = 55505
SERVER = socket.gethostbyname(socket.gethostname())

# Protocolo IPv4 que maneja streams de datos
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Asociar servidor con la direccion de la conexion
client.connect((SERVER,PORT))

username = input("Write your username: ")

def recieve_message():
    while True:
        try:
            # Recibe el mensaje y lo decodifica
            msg = client.recv(1024).decode()
            
            # Si le pide el username se lo envia
            if msg == "@Username":
                client.send(username.encode())
            else:
                print(msg)

        except:
            print("An error ocurred :c")
            client.close()
            break

def write_message():
    while True:
        try:
            msg_to_send = input().strip()
            if msg_to_send != "":
                message = "{}: {}".format(username,msg_to_send).encode()
                client.send(message)
        except EOFError:
            print("Finalizando la sesión...")
            sys.exit()


# un hilo para cada usuario 
recieve_thread = threading.Thread(target=recieve_message)
recieve_thread.start()

write_msg_thread = threading.Thread(target=write_message)
write_msg_thread.start()
