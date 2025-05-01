def valor_mediano(a, b, c):
    # Ordenar los tres números y devolver el del medio
    return sorted([a, b, c])[1]

mediano = valor_mediano(5, 1, 9)
print(f"El valor mediano es {mediano}.")