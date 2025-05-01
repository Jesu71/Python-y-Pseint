# Crear un arreglo vacío de 5. 
arreglo = [0] * 5

# Pedir al usuario que ingrese los datos.
for i in range(5):
    numero = float(input(f"Ingrese el número para la posición {i + 1}: "))
    arreglo[i] = numero

# Imprimir el arreglo listo.
print("El arreglo lleno es:", arreglo)