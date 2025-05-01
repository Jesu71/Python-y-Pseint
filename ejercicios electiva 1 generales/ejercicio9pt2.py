# Leer ambos archivos y almacenar los números en un conjunto (para eliminar duplicados).
numeros_pares = set()

# Leer el archivo de 0 a 100.
with open("numeros_0_100.txt", "r") as archivo1:
    for linea in archivo1:
        num = int(linea.strip())
        if num % 2 == 0:
            numeros_pares.add(num)

# Leer el de 50 a 200.
with open("numeros_50_200.txt", "r") as archivo2:
    for linea in archivo2:
        num = int(linea.strip())
        if num % 2 == 0:
            numeros_pares.add(num)

# Crear un nuevo archivo con los números pares, ordenados de mayor a menor
with open("numeros_pares.txt", "w") as archivo_pares:
    for num in sorted(numeros_pares, reverse=True):
        archivo_pares.write(f"{num}\n")
print("Archivo 'numeros_pares.txt' creado con números pares, sin repetidos y en orden descendente.")