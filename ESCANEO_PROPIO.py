import time

print("--- BUENOS DIAS ---")
time.sleep(1)
print("EL dia de hoy guardaremos el escaneo de una IPS y PUERTOS en un txt.")
time.sleep(3)

ips = []

for i in range(3):
    ip = input(f"Dame la IP {i+1} : ")
    ips.append(ip)

puertos =[]   
for i2 in range(3):
    puerto = input(f"Dame el PUERTO {i2+1} : ")
    puertos.append(puerto)

with open("mi_log.txt", "w") as archivo:
    archivo.write("---- ESCANEO INICIADO ----")
   
    archivo.write(f"Escaneo de la IP: {ips}\n")
    archivo.write(f"Escaneo del Puerto: {puertos}\n")

    for puerto in puertos:
        print(f"Escanenando Puertos {puerto}...")
        time.sleep(1)
        
        if int(puerto) % 2 == 0:
            estado = "Abierto"
        else:
            estado = "Cerrado"
        archivo.write(f"    - Puerto {puerto}: {estado} \n")
print("Escaneo guardado en 'mi_log.txt'")