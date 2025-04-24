def procesar_lista(lista):
    mayor = max(lista)  # Encuentra el mayor de todos.
    suma_pares = sum(x for x in lista if x % 2 == 0)  # Suma de los números pares.
    invertida = lista[::-1]  # Inviertir lista.

    return mayor, suma_pares, invertida

# Ejemplo de uso
numeros = [100, 200, 300, 400, 500]
mayor, suma_pares, invertida = procesar_lista(numeros)

print("Mayor:", mayor)
print("Suma de pares:", suma_pares)
print("Lista invertida:", invertida)