import socket
import datetime
import sys
from unidecode import unidecode
import os

# Definir host y puerto
HOST = '127.0.0.1'
PORT = 65435

# Crear el directorio si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Crear un archivo de log con fecha y hora
log_filename = "logs/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
log_file = open(log_filename, "w")

# Crear un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
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
                        shifted_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
                    else:
                        shifted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
                    encoded_message += shifted_char
                elif char.isdigit():
                    shifted_char = str((int(char) - 5) % 10)
                    encoded_message += shifted_char
                else:
                    encoded_message += char
            
            # Enviar el mensaje al servidor
            s.sendall(encoded_message.encode('utf-8'))
            
            # Guardar el mensaje en el archivo de log con fecha y hora
            timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
            log_file.write(f"{timestamp} Cliente: {message}\n")
    
            # Esperar la respuesta del servidor
            data = s.recv(1024).decode('utf-8')
    
            # Decodificar la respuesta utilizando el algoritmo César
            decoded_response = ''
            for char in data:
                if char.isalpha():
                    if char.isupper():
                        shifted_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
                    else:
                        shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                    decoded_response += shifted_char
                elif char.isdigit():
                    shifted_char = str((int(char) + 5) % 10)
                    decoded_response += shifted_char
                else:
                    decoded_response += char
            
    
            print('Respuesta recibida del servidor:', decoded_response)
            # Guardar el mensaje en el archivo de log con fecha y hora
            timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
            log_file.write(f"{timestamp} Servidor: {decoded_response}\n")

    except KeyboardInterrupt:
        print('Saliendo del programa...')
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        log_file.write(f"{timestamp} Info: Programa terminado.\n")
        sys.exit(0)

    except ConnectionRefusedError:
        print('Error: No se pudo conectar al servidor.')
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        log_file.write(f"{timestamp} Warning: No se pudo conectar al servidor.\n")
        
    except socket.timeout:
        print('Error: Tiempo de espera agotado.')
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        log_file.write(f"{timestamp} Warning: Tiempo de espera agotado.\n")
        

    except:
        print('Error desconocido')
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        log_file.write(f"{timestamp} Error desconocido\n")

log_file.close()