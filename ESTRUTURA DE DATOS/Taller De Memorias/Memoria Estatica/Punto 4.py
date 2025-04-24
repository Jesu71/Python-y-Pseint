# Lista con 6 números enteros.
numeros = [34, 7, 23, 32, 5, 62]

# Implementacion el algoritmo de ordenamiento de burbuja.
n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Intercambiar los elementos.
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Imprimir la lista ordenada.
print("La lista ordenada en orden ascendente es:", numeros)