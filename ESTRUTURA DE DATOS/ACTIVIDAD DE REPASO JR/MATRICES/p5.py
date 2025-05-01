# Matriz de 10x10 inicializada con ceros.
matriz = [[0 for _ in range(10)] for _ in range(10)]

# Asignar el valor 1 a los elementos de la diagonal principal.
for i in range(10):
    matriz[i][i] = 1

# Imprimir la matriz resultante.
for fila in matriz:
    print(fila)