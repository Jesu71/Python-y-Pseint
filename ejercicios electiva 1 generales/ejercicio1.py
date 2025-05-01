# Pedir las dimensiones de la habitación.
ancho = float(input("¿Cuál es el ancho de la habitación? (en pies o metros): "))
largo = float(input("¿Y el largo? (en pies o metros): "))

# Calculo del área.
area = ancho * largo
# Mostrar el resultado.
print(f"El área de la habitación es de {area:.2f} unidades cuadradas.")