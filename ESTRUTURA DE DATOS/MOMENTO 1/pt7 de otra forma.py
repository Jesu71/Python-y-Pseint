def crear_matriz(n):
    # Crea una matriz n x n
    return [[0] * n for _ in range(n)]

def ingresar_valores(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def suma_filas(matriz):
    return [sum(fila) for fila in matriz]

def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def main():
    n = int(input("Ingrese el tamaño de la matriz (n x n): "))

    # Crear matriz.
    matriz = crear_matriz(n)

    # Ingresar valores.
    ingresar_valores(matriz)

    # Imprimir matriz original.
    print("\nMatriz original:")
    imprimir_matriz(matriz)

    # Calcular y mostrar la suma de cada fila.
    sumas_filas = suma_filas(matriz)
    print("\nSuma de cada fila:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i}: {suma}")

    # Calcular y mostrar la suma de la diagonal principal.
    suma_diagonal = suma_diagonal_principal(matriz)
    print(f"\nSuma de la diagonal principal: {suma_diagonal}")

    # En Python, la memoria se libera automáticamente cuando las variables salen de ámbito.
    # No es necesario liberar memoria manualmente.

if __name__ == "__main__":
    main()