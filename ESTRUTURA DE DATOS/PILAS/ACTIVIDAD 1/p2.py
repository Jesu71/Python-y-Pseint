def esta_vacia(pila):
    """
    Verifica si una pila está vacía.
    
    Args:
        pila (list): La pila a verificar
        
    Returns:
        bool: True si la pila está vacía, False en caso contrario
    """
    return len(pila) == 0

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
            pila.append(elemento)  # Agregamos el elemento a la pila.
            print(f"Elemento '{elemento}' agregado a la pila.")
    
    # Verificamos si la pila está vacía.
    if esta_vacia(pila):
        print("La pila está vacía (True)")
    else:
        print(f"La pila no está vacía (False). Contiene {len(pila)} elementos: {pila}")

if __name__ == "__main__":
    main()