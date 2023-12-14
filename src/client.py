# Cliente que se conecta al servidor para enviar y recibir información
import functions as fun
import socket
import threading

# Función para enviar mensajes
def send(socket, address):
    # Siempre se está escuchando por un nuevo mensaje
    while True:
        message = input()
        # Si decide salir, manda la orden al servidor directamente
        if message == 'SALIR':
            socket.sendto(message.encode('utf-8'), address)
            break
        # En otro caso, envía el mensaje cifrado
        ciphered_message = f"{username}: {fun.cesar_cipher(message, send_key)}"
        socket.sendto(ciphered_message.encode('utf-8'), address)

# Función para recibir mensajes
def receive(socket, address):
    # Envia el nombre de usuario para agregarse a la lista de usuarios
    socket.sendto(username.encode('utf-8'), address)
    # Siempre está escuchando por nuevos mensajes
    while threading_send.is_alive():
        data = socket.recv(1024).decode('utf-8')
        # Validar que no sea un mensaje que envíe yo
        print(data)
        # Si el mensaje tiene contenido, lo descifra con la clave ingresada
        if len(data.split(':')) > 3:
            ciphered_message = data.split(':')[3]
            deciphered_message = fun.cesar_decipher(ciphered_message, receive_key)
            print(f"Mensaje descifrado: {deciphered_message}")

print('- - CHAT | CESAR - -\n' + 'SALIR) Salir del chat')
# Obtener nombre de usuario, llave de envío y llave de recepción
username = input('Ingresa tu nombre de usuario: ')
send_key = int(input('Ingresa tu llave de cifrado para enviar: '))
receive_key = int(input('Ingresa tu llave de cifrado para recibir: '))
# Crear socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Dirección del servidor localhost:8080
server_address = ('localhost', 8080)
# Hilos de recepción y envío
threading_receive = threading.Thread(target=receive, args=(client_socket, server_address), daemon=True)
threading_send = threading.Thread(target=send, args=(client_socket, server_address))
# Inicia hilos
threading_receive.start()
threading_send.start()
threading_send.join()
client_socket.close()
