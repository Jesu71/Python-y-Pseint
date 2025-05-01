# Crear el primer archivo con números de 0 a 100.
with open("numeros_0_100.txt", "w") as archivo1:
    for num in range(101):
        archivo1.write(f"{num}\n")
        
# Crear el segundo con números de 50 a 200.
with open("numeros_50_200.txt", "w") as archivo2:
    for num in range(50, 201):
        archivo2.write(f"{num}\n")
print("Archivos 'numeros_0_100.txt' y 'numeros_50_200.txt' creados.")