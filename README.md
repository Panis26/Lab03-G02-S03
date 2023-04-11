# Lab03-G02-S03

# Instrucciones de ejecución
## TCP

Para no tener que descargar el ambiente de haskell, podemos ejecutar los archivos compilados para correr el servidor y el cliente.

1. Dentro de la carpeta server, corremos el archivo fileGenerator.exe para generar los archivos. Solo se tiene que hacer una vez.
2. Ahora podemos ejecutar el archivo tcp.exe para correr el servidor. Primero pregunta el archivo a mandar y la cantidad de clientes concurrentes. Luego de esto, el servidor queda esperando a que los clientes se conecten. (Como se usa el puerto 80 puede que ocurra un error de permisos, en este caso correr el programa con sudo)
3. Ahora corremos el cliente con el archivo client.exe. Este se puede correr cuantas veces se quiera usando la linea de comandos.

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
