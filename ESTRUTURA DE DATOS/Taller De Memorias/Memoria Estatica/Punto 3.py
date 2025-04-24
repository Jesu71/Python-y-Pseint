# Lista con 10 números predefinidos.
numeros = [10, 39, 40, 77, 20, 19, 22, 34, 22, 99]

# Solicitar un número al usuario.
numero_buscar = int(input("Ingrese el número a buscar: "))

# Verificar si el número está en la misma.
if numero_buscar in numeros:
    print(f"El número {numero_buscar} está en la lista.")
else:
    print(f"El número {numero_buscar} no está en la lista.")  