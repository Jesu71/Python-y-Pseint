# matriz de 5x5 con números al azar dados por mi.
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Extraer la diagonal principal y almacenarla en un vector.
diagonal_principal = [matriz[i][i] for i in range(5)]

# Imprimir el vector resultante.
print("El vector de la diagonal principal es:", diagonal_principal)