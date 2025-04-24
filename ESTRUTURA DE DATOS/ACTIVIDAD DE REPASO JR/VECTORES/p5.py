# Función para realizar operaciones sobre el vector.
def analizar_vector(vector):
    # a.) Contar números positivos.
    positivos = sum(1 for num in vector if num > 0)
    
    # b.) Sumar números positivos.
    suma_positivos = sum(num for num in vector if num > 0)
    
    # c.) Restar números negativos.
    resta_negativos = sum(abs(num) for num in vector if num < 0)
    
    return positivos, suma_positivos, resta_negativos
def main():
    # Vector ejemplo.
    vector = [-4, 7, -2, 10, 5, -8, 3, -1, 6]
    
    # Realizamos las operaciones.
    cant_positivos, suma_pos, resta_neg = analizar_vector(vector)
    
    # print los resultados.
    print(f"Vector original: {vector}")
    print(f"a. Cantidad de números positivos: {cant_positivos}")
    print(f"b. Suma de números positivos: {suma_pos}")
    print(f"c. Resta de números negativos: {resta_neg}")

if __name__ == "__main__":
    main()