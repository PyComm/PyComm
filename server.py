import socket
from unidecode import unidecode

# Definir host y puerto
HOST = '127.0.0.1'
PORT = 65435

# Crear un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # Asociar el socket al host y puerto
        s.bind((HOST, PORT))
        s.listen()
        # Esperar a que se conecte un cliente
        conn, addr = s.accept()
        with conn:
            print('Conexión establecida desde', addr)
            while True:
                # Recibir el mensaje del cliente
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                # Decodificar el mensaje utilizando el algoritmo César
                decoded_data = ''
                for char in data:
                    if char.isalpha():
                        if char.isupper():
                            shifted_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
                        else:
                            shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                    elif char.isdigit():
                        if int(char) < 5:
                            shifted_char = str(int(char) + 5)
                        else:
                            shifted_char = str(int(char) - 5)
                    else:
                        shifted_char = char
                    decoded_data += shifted_char
                print('Mensaje recibido del cliente:', decoded_data)
                # Enviar una respuesta al cliente
                response = input('Ingrese una respuesta al cliente: ')
                response = unidecode(response)
                # Codificar la respuesta utilizando el algoritmo César
                encoded_response = ''
                for char in response:
                    if char.isalpha():
                        if char.isupper():
                            shifted_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
                        else:
                            shifted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
                    elif char.isdigit():
                        shifted_char = str((int(char) - 5) % 10)
                    else:
                        shifted_char = char
                    encoded_response += shifted_char
                conn.sendall(encoded_response.encode('utf-8'))
    except OSError as e:
        print(f"Ocurrió un error al tratar de crear o usar un socket: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
