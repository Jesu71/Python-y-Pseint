# Pedir las dimensiones del campo.
ancho = float(input("¿Cuál es el ancho del campo en pies? "))
largo = float(input("¿Y la longitud del campo en pies? "))

# Calcular el área en pies cuadrados y luego convertir a acres.
pies_cuadrados = ancho * largo
acres = pies_cuadrados / 43560
# Mostrar el resultado.
print(f"El área del campo es de {acres:.2f} acres.")