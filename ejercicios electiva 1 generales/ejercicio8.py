# Crear un conjunto para almacenar palabras únicas.
palabras = set()

# Leer palabras hasta que se ingrese "fin en minuscula".
while True:
    palabra = input("Ingresa una palabra (escribe 'fin' para terminar): ")
    if palabra == "fin":
        break
    palabras.add(palabra)
# Mostrar las palabras ingresadas sin repetir.
print("Las palabras que ingresaste son:")
for palabra in palabras:
    print(palabra)