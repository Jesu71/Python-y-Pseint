import random

# Vector de 10 posiciones.
vector = [0] * 10

# Llenar el vector mismo con números aleatorios entre 1 y 100.
for i in range(10):
    vector[i] = random.randint(1, 100)

# Imprimir el mismo lleno.
print("El vector lleno con números aleatorios es:", vector)
