import random

# Matriz de 7x7 con números aleatorios entre 1 y 100.
matriz = [[random.randint(1, 100) for _ in range(7)] for _ in range(7)]

# Calcular la suma de cada fila y almacenarla en un vector.
suma_filas = [sum(fila) for fila in matriz]

# Calcular la suma de cada columna y almacenarla en otro vector.
suma_columnas = [sum(matriz[i][j] for i in range(7)) for j in range(7)]

# Imprimir todo.
print("Matriz:")
for fila in matriz:
    print(fila)

print("\nSuma de cada fila:", suma_filas)
print("Suma de cada columna:", suma_columnas)