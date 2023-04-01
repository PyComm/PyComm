import socket

# Definir host y puerto
HOST = '127.0.0.1'
PORT = 65431

# Crear un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar el socket al host y puerto
    s.connect((HOST, PORT))
    while True:
        # Pedir al usuario que ingrese un mensaje
        message = input('Ingrese un mensaje: ')
        # Codificar el mensaje utilizando el algoritmo César
        encoded_message = ''
        for char in message:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
                encoded_message += shifted_char
            else:
                encoded_message += char
        # Enviar el mensaje al servidor
        s.sendall(encoded_message.encode())
        # Esperar la respuesta del servidor
        data = s.recv(1024)
        # Decodificar la respuesta utilizando el algoritmo César
        decoded_response = ''
        for char in data.decode():
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                decoded_response += shifted_char
            else:
                decoded_response += char
        print('Respuesta recibida del servidor:', decoded_response)
