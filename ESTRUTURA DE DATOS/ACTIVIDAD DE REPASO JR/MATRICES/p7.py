def sumar_matrices(matriz1, matriz2):
    # Verificar que las matrices tengan las mismas dimensiones.
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    # Nueva matriz para almacenar el resultado de la suma.
    n = len(matriz1)
    m = len(matriz1[0])
    matriz_resultado = [[0] * m for _ in range(n)]

    # Sumar elemento a elemento las dos matrices.
    for i in range(n):
        for j in range(m):
            matriz_resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return matriz_resultado

# Ejemplo de uso.
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matriz_suma = sumar_matrices(matriz1, matriz2)

# Imprimir la matriz resultante.
for fila in matriz_suma:
    print(fila)