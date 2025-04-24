# Definir una matriz de 4x4.
filas = 4
columnas = 4
matriz = []

# Llenar la matriz con valores ingresados por el usuario.
print("Ingrese los valores de la matriz 4x4:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        num = int(input(f"Ingrese el número en la posición [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Encontrar el número mayor y su posición.
mayor = matriz[0][0]
posicion = (0, 0)

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            posicion = (i, j)

# imprimir la matriz y el resultado.
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

print(f"\nEl número mayor es {mayor} y está en la posición {posicion}")