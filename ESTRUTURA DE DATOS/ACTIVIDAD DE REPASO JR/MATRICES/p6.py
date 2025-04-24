# Matriz de 5x6 con números, incluyendo ceros, positivos y negativos.
matriz = [
    [0, -1, 2, 3, 0, -4],
    [5, 0, -6, 7, 8, 9],
    [0, -10, 11, 0, 12, -13],
    [14, 15, 0, -16, 17, 18],
    [0, 19, -20, 21, 0, 22]
]

# Contadores para ceros, positivos y negativos.
contador_ceros = 0
contador_positivos = 0
contador_negativos = 0

# Recorrer la matriz y contar los números.
for fila in matriz:
    for numero in fila:
        if numero == 0:
            contador_ceros += 1
        elif numero > 0:
            contador_positivos += 1
        else:
            contador_negativos += 1

# Imprimir los resultados.
print("Cantidad de ceros:", contador_ceros)
print("Cantidad de números positivos:", contador_positivos)
print("Cantidad de números negativos:", contador_negativos)