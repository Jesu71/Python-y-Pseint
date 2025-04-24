# Arreglo de tamaño fijo (5 elementos) para almacenar las calificaciones.
notas = [0] * 5

# Pedir al usuario que ingrese las calificaciones.
for i in range(5):
    while True:
        try:
            nota = float(input(f"Ingrese la calificación {i + 1}: "))
            notas[i] = nota
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Calcular el promedio de las mismas dadas.
promedio = sum(notas) / len(notas)

# Imprimir el promedio calculado.
print("El promedio de las calificaciones es:", promedio)