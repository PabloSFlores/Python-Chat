# Servidor para la transmisión de mensajes
import socket
from datetime import datetime

# Crear socket UDp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Unir la tupla
server_socket.bind(("localhost", 8080))
# Usuarios {(ip: puerto): username}
users = {}


# Función que reenvia el mensaje a todas las direcciones de los usuarios menos al que envió el mensaje
# Imprime el mensaje y lo reenvia
def broadcast(message, omit_address):
    print(message)
    for address in users:
        if not omit_address == address:
            server_socket.sendto(message.encode(), address)

# Servidor siempre escuchando
while True:
    # Manejo de excepciones
    try:
        # Obtener la información de los usuarios descomponiendo el la respuesta de recvfrom
        data, address = server_socket.recvfrom(1024)

        # Agregar usuario si es nuevo
        if not address in users:
            users[address] = data.decode("utf-8")
            enter_message = f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {users[address]} entró al chat."
            broadcast(enter_message, address)
            continue

        # Eliminar al usuario del diccionario si decide salir
        if "SALIR" in data.decode("utf-8"):
            leave_message = f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {users[address]} salió del chat."
            users.pop(address)
            broadcast(leave_message, address)
        
        # Mensaje normal
        else:
            message = f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {data.decode()}"
            broadcast(message, address)
    except ConnectionResetError:
        print("Error")
