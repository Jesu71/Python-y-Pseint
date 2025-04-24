def transponer_matriz(A):
    # Obtener las dimensiones de la matriz original.
    m = len(A)
    n = len(A[0])

    # Crear una nueva matriz para almacenar la transpuesta, de dimensiones n*m.
    A_transpuesta = [[0] * m for _ in range(n)]

    # Intercambiar filas por columnas.
    for i in range(m):
        for j in range(n):
            A_transpuesta[j][i] = A[i][j]

    return A_transpuesta

# Ejemplo de uso.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

A_transpuesta = transponer_matriz(A)

# Imprimir la matriz transpuesta. 
for fila in A_transpuesta:
    print(fila)