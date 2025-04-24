# Matriz de 5 filas y 6 columnas con números.
matriz = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30]
]

# Calcular la suma de todos los elementos de la matriz.
suma_total = sum(sum(fila) for fila in matriz)

# Imprimir el resultado de la suma echa.
print("La suma de los números almacenados en la matriz es:", suma_total)