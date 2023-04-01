import socket

# Definir host y puerto
HOST = '127.0.0.1'
PORT = 65431

# Crear un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Asociar el socket al host y puerto
    s.bind((HOST, PORT))
    s.listen()
    # Esperar a que se conecte un cliente
    conn, addr = s.accept()
    with conn:
        print('Conexión establecida desde', addr)
        while True:
            # Recibir el mensaje del cliente
            data = conn.recv(1024)
            if not data:
                break
            # Decodificar el mensaje utilizando el algoritmo César
            decoded_data = ''
            for char in data.decode():
                if char.isalpha():
                    shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                    decoded_data += shifted_char
                else:
                    decoded_data += char
            print('Mensaje recibido del cliente:', decoded_data)
            # Enviar una respuesta al cliente
            response = input('Ingrese una respuesta al cliente: ')
            # Codificar la respuesta utilizando el algoritmo César
            encoded_response = ''
            for char in response:
                if char.isalpha():
                    shifted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
                    encoded_response += shifted_char
                else:
                    encoded_response += char
            conn.sendall(encoded_response.encode())
