def esta_vacia(pila):
    """
    Verifica si una pila está vacía.
    
    Args:
        pila (list): La pila a verificar
        
    Returns:
        bool: True si la pila está vacía, False en caso contrario
    """
    return len(pila) == 0

def vaciar_pila(pila):
    """
    Elimina todos los elementos de la pila uno por uno hasta que quede vacía.
    
    Args:
        pila (list): La pila a vaciar
    """
    print("Eliminando elementos de la pila:")
    while not esta_vacia(pila):
        elemento = pila.pop()  # Elimina y devuelve el elemento del tope.
        print(f"Elemento eliminado: {elemento}")
    
    print("La pila ahora está vacía.")

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
    
    # Verificamos si la pila está vacía inicialmente.
    if esta_vacia(pila):
        print("La pila está vacía, no hay elementos para eliminar.")
    else:
        print(f"La pila contiene {len(pila)} elementos antes de comenzar a vaciarla.")
        # Vaciamos la pila elemento por elemento.
        vaciar_pila(pila)
        
    # Verificamos nuevamente después de vaciar.
    if esta_vacia(pila):
        print("Verificación final: La pila está vacía (True)")
    else:
        print("Verificación final: La pila no está vacía (False)")

if __name__ == "__main__":
    main()