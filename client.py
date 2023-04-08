import socket
from unidecode import unidecode

# Definir host y puerto
HOST = '127.0.0.1'
PORT = 65435

# Crear un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar el socket al host y puerto
    s.connect((HOST, PORT))
    while True:
        # Pedir al usuario que ingrese un mensaje
        message = input('Ingrese un mensaje: ')
        message = unidecode(message)
        # Codificar el mensaje utilizando el algoritmo César
        encoded_message = ''
        for char in message:
            if char.isalpha():
                if char.isupper():
                    shifted_char = chr((ord(char) - ord('A') - 3) % 26 + ord('a'))
                else:
                    shifted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('A'))
                encoded_message += shifted_char
            elif char.isdigit():
                shifted_char = (int(char)-5)%10
                encoded_message += str(shifted_char)
            else:
                encoded_message += char
        # Enviar el mensaje al servidor
        s.sendall(encoded_message.encode('utf-8'))
        # Esperar la respuesta del servidor
        data = s.recv(1024).decode('utf-8')
        # Decodificar la respuesta utilizando el algoritmo César
        decoded_response = ''
        for char in data:
            if char.isalpha():
                if char.isupper():
                    shifted_char = chr((ord(char) - ord('A') + 3) % 26 + ord('a'))
                else:
                    shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('A'))
                decoded_response += shifted_char
            elif char.isdigit():
                if int(char) < 5:
                    shifted_char = (int(char)+5)
                else:
                    shifted_char = int(char)-5
                decoded_response += str(shifted_char)
            else:
                decoded_response += char

        print('Respuesta recibida del servidor:', decoded_response)
