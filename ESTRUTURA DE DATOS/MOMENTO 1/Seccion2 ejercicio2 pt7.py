import numpy as np

n = int(input("Ingrese el tamaño de la matriz (n x n): "))
matriz = np.array([list(map(int, input().split())) for _ in range(n)])

print("\nMatriz ingresada:\n", matriz)
print("\nSuma de cada fila:", matriz.sum(axis=1))
print("\nSuma de la diagonal principal:", np.trace(matriz))