#Se generan archivos .bin de 100MB y 250MB de "0" en la carpeta "Archivos"

import os
import sys

def main():
    #Genera archivos de 100MB
    with open("UDP/udp-server/Archivos/100MB.bin", "wb") as f:
        f.seek(100 * 1024 * 1024 - 1)
        f.write(b"\0")
    #Genera archivos de 250MB
    with open("UDP/udp-server/Archivos/250MB.bin", "wb") as f:
        f.seek(250 * 1024 * 1024 - 1)
        f.write(b"\0")

if __name__ == "__main__":
    main()
