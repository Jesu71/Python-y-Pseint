# Crear una lista vacía para almacenar los números.
numeros = []

# Leer valores hasta que se ingrese 0.
while True:
    num = int(input("Ingresa un número entero (0 para terminar): "))
    if num == 0:
        break
    numeros.append(num)

# Mostrar los números en orden ascendente.
print("Los números que ingresaste, ordenados de menor a mayor, son:")
print(sorted(numeros))