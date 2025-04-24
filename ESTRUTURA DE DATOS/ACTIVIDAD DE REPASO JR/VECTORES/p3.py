# Definir dos vectores con los mismos numeros inventados por mi.
vector1 = [1, 2, 3, 4, 5]
vector2 = [6, 7, 8, 9, 10]

# Sumar los elementos correspondientes de ambos.
suma_elementos = [a + b for a, b in zip(vector1, vector2)]

# Sumar todos los elementos del vector resultante.
resultado = sum(suma_elementos)

# Guardar el resultado en un nuevo vector de una sola posición. 
vector_resultado = [resultado]

# Imprimir el resultado.
print("El vector resultado es:", vector_resultado)