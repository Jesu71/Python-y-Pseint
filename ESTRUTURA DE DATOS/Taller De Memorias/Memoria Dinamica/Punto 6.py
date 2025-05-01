# Lista vacía
nombres = []

# Pedir al usuario ingresar nombres.
while True:
    nombre = input("Ingrese un nombre (o deje vacío para terminar): ")
    if nombre == "":
        break
    nombres.append(nombre)

# Mostrar la lista final con todos los nombres ya dados.
print("La lista de nombres ingresados es:", nombres)