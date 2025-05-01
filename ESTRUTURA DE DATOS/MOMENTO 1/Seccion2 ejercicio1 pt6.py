import random
def main():
    # R// a. Declarar un vector estático de tamaño 15.
    vector = [0] * 15
    
    # R// b. Llenar el vector con valores aleatorios entre 1 y 100.
    for i in range(len(vector)):
        vector[i] = random.randint(1, 100)
    
    # R// c. Imprimir el vector original.
    print("Vector original:")
    print(vector)
    
    # R// d. Ordenar el vector de forma ascendente.
    vector.sort()
    print("\nVector ordenado de forma ascendente:")
    print(vector)
    
    # R// e. Buscar un número ingresado por el usuario
    numero_usuario = int(input("\nIngresa un número para buscar en el vector: "))
    
    if numero_usuario in vector:
        print(f"El número {numero_usuario} SÍ está en el vector.")
    else:
        print(f"El número {numero_usuario} NO está en el vector.")
        # - Agregar el número al vector si este valida que no esta el mismo.
        vector.append(numero_usuario)
        print(f"Se ha agregado el número {numero_usuario} al vector.")
        
        # - Ordenar de manera descendente.
        vector.sort(reverse=True)
        print("\nVector actualizado y ordenado de forma descendente:")
        print(vector)

if __name__ == "__main__":
    main()