# Dos listas de tamaño 4 con valores numéricos.
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

# Tercera lista para almacenar los resultados.
lista_resultado = [0] * 4

# Sumar elemento a elemento ambas listas y almacenar los resultados.
for i in range(4):
    lista_resultado[i] = lista1[i] + lista2[i]

# Imprimir resultado.
print("La lista resultado de la suma es:", lista_resultado)