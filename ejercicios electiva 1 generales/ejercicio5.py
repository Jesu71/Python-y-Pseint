# Crear y abrir un txt para escribir la matriz.
with open("tabla_multiplicacion.txt", "w") as archivo:
    # Generar la matriz.
    for i in range(1, 11):
        for j in range(1, 11):
            archivo.write(f"{i} x {j} = {i*j}\t")
        archivo.write("\n") 
print("La matriz de multiplicación se ha guardado en 'tabla_multiplicacion.txt'.")
