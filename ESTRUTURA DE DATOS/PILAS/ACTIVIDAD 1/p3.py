def numero_elementos(pila):
    """
    Devuelve el número de elementos en la pila.
    
    Args:
        pila (list): La pila a verificar
        
    Returns:
        int: Número de elementos en la pila
    """
    return len(pila)

def mostrar_elementos(pila):
    """
    Muestra todos los elementos de la pila.
    
    Args:
        pila (list): La pila cuyos elementos se mostrarán
    """
    if len(pila) == 0:
        print("La pila está vacía, no hay elementos para mostrar.")
    else:
        print("Elementos de la pila (desde el tope hasta la base):")
        for i in range(len(pila) - 1, -1, -1):
            print(f"{len(pila) - i}. {pila[i]}")

def main():
    # Inicia con una pila vacía.
    pila = []
    
    # Preguntamos al usuario si desea agregar elementos.
    respuesta = input("¿Deseas agregar elementos a la pila? (s/n): ")
    
    if respuesta.lower() == "s":
        while True:
            elemento = input("Ingresa un elemento (o 'salir' para terminar): ")
            if elemento.lower() == 'salir':
                break
            pila.append(elemento)  # Agregamos el elemento a la pila
            print(f"Elemento '{elemento}' agregado a la pila.")
    
    # Obtenemos y mostramos el número de elementos.
    num_elementos = numero_elementos(pila)
    print(f"\nLa pila contiene {num_elementos} elementos.")
    
    # Mostramos los elementos de la pila.
    mostrar_elementos(pila)

if __name__ == "__main__":
    main()