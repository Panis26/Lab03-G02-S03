import socket
import threading
import time
import os

# Define a function to handle each client request
def handle_request(filename, client_address):
    # If the requested filename matches, send the file to the client in chunks
    with open(f"./Archivos/{filename}", 'rb') as f:
        print(f'Sending {filename} to client at {client_address}...')
        start_time = time.time()
        while True:
            chunk = f.read(64000)
            if not chunk:
                break
            sock.sendto(chunk, client_address)
        time.sleep(0.01)
        sock.sendto(b'EOF', client_address) # Send an empty chunk to signal the end of the file
        end_time = time.time()
        transfer_time = end_time - start_time
        print(f'Successfully sent {filename} to client at {client_address}.')

        #Crear el archivo de log para esa petición
        log_dir = 'Logs'

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        with open (f"./{log_dir}/{time.strftime('%Y-%m-%d-%H-%M-%S')}-log.txt", "w") as log_file:
            log_file.write(f"Filename: {filename}\n")
            log_file.write(f"File size: {os.path.getsize(f'./Archivos/{filename}')/1000000} MB\n")
            log_file.write(f"Transfer time: {transfer_time:.2f} seconds\n")
            log_file.write(f"Succesful delivery: True\n")
            log_file.close()
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8000))

# Serve the file to clients
active_threads = []
while True:
    # Wait for a filename request from a client
    filename, client_address = sock.recvfrom(1024)
    filename = filename.decode()

    # Create a new thread to handle the client request
    t = threading.Thread(target=handle_request, args=(filename, client_address))
    t.start()
    active_threads.append(t)



