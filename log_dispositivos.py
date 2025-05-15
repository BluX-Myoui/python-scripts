#SIMULKADOR DE ESCANEO
import time
ips = []

for i in range (3):
    ip = input(f"DAME LA IP {i+1}: ")
    ips.append(ip)

puertos = [21, 22, 23, 80, 443]

with open("log_dispositivos.txt", "w") as archivo:
    archivo.write("--- SIMULADOR DE ESCANEO DE DISPOSITVOS ---\n\n")

    archivo.write("-IPS DADAS-\n")
    for ip in  ips:
        archivo.write(F"    - IP: {ip}\n")
    archivo.write("\n")

    archivo.write("-PUERTOS-\n")
    for puerto in puertos:
        print(f"ESCANEANDO PUERTO {puerto}...")
        time.sleep(2)

        if puerto < 30:
            estado = "ANTIGUO"
        else:
            estado = "MODERNO"
        archivo.write(f"    - PUERTO {puerto}: {estado}\n")
    
    archivo.write("\nTAREA COMPLEATADA\n")
print("TRABAJO COMPLETADO Y GUARDADO EN 'log_dispositivos.txt'")