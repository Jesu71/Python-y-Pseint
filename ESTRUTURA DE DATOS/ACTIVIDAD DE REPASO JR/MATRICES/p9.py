def multiplicar_matrices(A, B):
    # Obtener las dimensiones de las matrices.
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Verificar que el número de columnas de A sea igual al número de filas de B.
    if n != len(B):
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

    # Crear una matriz C de dimensiones m*p inicializada con ceros.
    C = [[0] * p for _ in range(m)]

    # Calcular el producto de las matrices A y B.
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Ejemplo de uso.
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

C = multiplicar_matrices(A, B)

# Imprimir la matriz resultante.
for fila in C:
    print(fila)