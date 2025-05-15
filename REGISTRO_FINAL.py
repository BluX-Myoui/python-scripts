import time

    

num_ips = input("Cuantas IPS desea poner: ")

print(f"DE ACUERDO EL NUMERO SOLICITADO FUE {num_ips}")
time.sleep(2)
print("⏳ESPERA PORFAVOR...")
time.sleep(3) 

with open("registro_final.txt", "w") as archivo:
    archivo.write("--- SOLICITUD DE IPS ---\n\n")

    archivo.write("Lista de IPS\n")
    for i in range(int(num_ips)):
        ip = input((f"ESCRIBA SU IP {i+1}: "))
        time.sleep(0.3)
        archivo.write(f"    - IP {ip}\n")

    archivo.write(f"\n\n --- TAREA COMPLETADA ---\n\n")
    time.sleep(2)
print("✅ SUS IPS FUERON GRADADAS EN 'registro final.txt' ✅ ")


