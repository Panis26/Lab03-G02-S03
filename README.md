# Lab03-G02-S03

# Instrucciones de ejecución
## TCP
## UDP 
1. Se debe ejecutar el archivo "archivo.py" de la carpeta "udp-server" para la creación de archivos con los tamaños de 100MB y 250MB (Estos son sus nombre respectivos para la pruebas).
2. Se debe realizar la ejecución del archivo udp-server.py 
3. Luego de esto se hace la ejecución del archivo 25-clients.sh que hará la ejecución del archivo udp-client.py 25 veces. Si se corre en windows lo mejor es usar la consola git bash para su ejecución.
4. De lo contrario, se puede ejecutar el archivo udp-client.py en consola asignando los valores requeridos "python udp-client.py <IP> <filename> <numeroCliente>". 
 
  Prueba ejemplo consola:
  python udp-client.py localhost 100MB.bin 1
  python udp-client.py localhost 100MB.bin 2
  python udp-client.py localhost 100MB.bin 3
  python udp-client.py localhost 100MB.bin 4
  python udp-client.py localhost 100MB.bin 5
