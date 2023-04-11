import argparse
import os
import socket
import time

# Parse command line arguments
parser = argparse.ArgumentParser(description='UDP client that requests a file from a server')
parser.add_argument('server_address', help='Server address to connect to')
parser.add_argument('filename', help='Name of the file to request from the server')
parser.add_argument('client_name', help='Name of the client')
args = parser.parse_args()

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

# Send the filename to the server
sock.sendto(args.filename.encode(), (args.server_address, 8000))

# Receive the file data from the server in chunks
with open(f"./ArchivosRecibidos/Client-{args.client_name}-{args.filename}", "wb") as f:
    star_time = time.time()
    first_packet_time = None
    while True:
        try:
            chunk, server_address = sock.recvfrom(64000)
            if chunk == b'EOF':
                break
            if not chunk:
                break
            if not first_packet_time:
                first_packet_time = time.time()
            f.write(chunk)
        except socket.timeout:
            print('Server timed out')
            break
    end_time = time.time()

#Calcular el tiempo de transferencia
if first_packet_time:
    transfer_time = end_time - first_packet_time
else:
    transfer_time = 0

#Tamaño del archivo generado
tamano = os.path.getsize(f"./ArchivosRecibidos/Client-{args.client_name}-{args.filename}")

# Close the socket
sock.close()

# Se crea el archivo de log Ejemplo:<año-mes-dia-hora-minuto-segundo-log.txt>
log_dir = 'Logs'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
with open (f"./{log_dir}/{time.strftime('%Y-%m-%d-%H-%M-%S')}-log.txt", "w") as log_file:
    log_file.write(f"Filename: {args.filename}\n")
    log_file.write(f"File size: {tamano/1000000} MB\n")
    log_file.write(f"Transfer time: {transfer_time} seconds\n")
    log_file.write(f"Succesfully received: {tamano>0} -> {args.filename} from server at {args.server_address}\n")
    
    #Cerrar el archivo de log
    log_file.close()


print(f'Successfully received {tamano} bytes from server at {args.server_address} and saved to {args.filename}.')