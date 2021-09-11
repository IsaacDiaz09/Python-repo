# https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim
import socket
import threading

# Puerto que no este en uso
PORT = 55505

# Obtiene la IP local del dispositivo dinamicamente
SERVER = socket.gethostbyname(socket.gethostname())

# Protocolo IPv4 que maneja streams de datos
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Asociar servidor con la direccion de la conexion
server.bind((SERVER,PORT))

# Se pone a la escucha
server.listen()

input("Press Enter to start the server")
print("Server running on {}:{}".format(SERVER,PORT))
print("Server listening...")

# Almacenar conexiones y usuarios
clients = []
usernames = []

# Enviar el msg a los demas clientes
def broadcast(message,__client):
    for client in clients:
        if client != __client:
            client.send(message)


# Manejar los msg de cada usuario
def handle_msg(client):
    while True:
        try:
            # Se obtiene el msg y se envia a los demas
            msg = client.recv(1024)
            broadcast(msg,client)
        except ConnectionResetError:
            # Se localiza el cliente que se desconecto y se elimina y se le cierra la conexion
            # Tambien se envia un broadcast a los demas usuarios de que se desconectó, rompe el ciclo
            pos = clients.index(client)
            username = usernames[pos]
            broadcast("ChatBot: {} disconnected".format(username).encode(),client)
            print("User {} disconnected from server".format(username))
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break

def recieve_connection():
    # Bucle infinito porque siempre estara a la escucha

    while True:

        # Se acepta al cliente y se guardan los datos de conexion
        client, address = server.accept()

        # Msg a la aplicacion del cliente pidiendole su usuario
        client.send("@Username".encode())

        """Para que cuando reciba este msg sepa que se le esta pidiendo el usuario"""

        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print("{} is connected with {}".format(username,address))

        msg = "ChatBot: {} joined the chat!".format(username).encode()

        broadcast(msg,client)

        client.send("Connected to server".encode())

        # un Hilo para cada conexion
        thread = threading.Thread(target=handle_msg,args=(client,))
        thread.start()

recieve_connection()
