# Lista vacía
numeros = []

# Permitir al usuario ingresar números indefinidamente.
print("Ingrese números. Ingrese -1 para eliminar el último número, o 0 para finalizar.")
while True:
    try:
        numero = int(input("Ingrese un número: "))

        if numero == 0:
            print("Finalizando la ejecución.")
            break
        elif numero == -1:
            if numeros:
                numeros.pop()
                print("Último número eliminado.")
            else:
                print("La lista está vacía, no se puede eliminar ningún número.")
        else:
            numeros.append(numero)
            print(f"Número {numero} agregado a la lista.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Mostrar la lista final.
print("La lista final de números es:", numeros)