class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        #Agrega un elemento a la pila.
        self.items.append(item)
    
    def desapilar(self):
        #Extrae y devuelve el último elemento de la pila.
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise Exception("La pila está vacía")
    
    def esta_vacia(self):
        #Verifica si la pila está vacía.
        return len(self.items) == 0
    
    def ver_tope(self):
        #Muestra el elemento en la cima de la pila sin extraerlo.
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise Exception("La pila está vacía")
    
    def __len__(self):
        #Devuelve la cantidad de elementos en la pila.
        return len(self.items)

def ordenar_pila(pila_original):
    """
    Ordena una pila de números enteros en orden ascendente utilizando una pila auxiliar
    
    Args:
        pila_original (Pila): Pila de números a ordenar
    
    Returns:
        Pila: Pila ordenada en orden ascendente
    """
    # Pila auxiliar para el ordenamiento
    pila_ordenada = Pila()
    
    # Continuar mientras haya elementos en la pila original.
    while not pila_original.esta_vacia():
        # Extraer el elemento actual de la pila original.
        elemento_actual = pila_original.desapilar()
        
        # Mover elementos de pila_ordenada a pila_original.
        # si son mayores que el elemento actual
        while (not pila_ordenada.esta_vacia() and 
               pila_ordenada.ver_tope() > elemento_actual):
            pila_original.apilar(pila_ordenada.desapilar())
        
        # Insertar el elemento actual en la posición correcta.
        pila_ordenada.apilar(elemento_actual)
    
    # Restaurar la pila original ordenada.
    while not pila_ordenada.esta_vacia():
        pila_original.apilar(pila_ordenada.desapilar())
    
    return pila_original

def imprimir_pila(pila, nombre):
    """
    Imprime los elementos de una pila
    
    Args:
        pila (Pila): Pila a imprimir
        nombre (str): Nombre de la pila para identificación
    """
    print(f"{nombre}: ", end="")
    pila_temporal = Pila()
    
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        print(elemento, end=" ")
        pila_temporal.apilar(elemento)
    
    # Restaurar la pila original.
    while not pila_temporal.esta_vacia():
        pila.apilar(pila_temporal.desapilar())
    
    print()  

def main():
    # Casos de prueba.
    casos_prueba = [
        [5, 2, 9, 1, 7, 6, 3],
        [10, 5, 15, 20, 3, 8],
        [1, 2, 3, 4, 5],  # Ya ordenada
        [5, 4, 3, 2, 1],  # Orden inverso
        []  # Pila vacía
    ]
    
    for i, numeros in enumerate(casos_prueba, 1):
        print(f"\nCaso de prueba {i}:")
        
        # Crear pila.
        pila = Pila()
        
        # Apilar números en orden inverso (para mantener orden original).
        for numero in reversed(numeros):
            pila.apilar(numero)
        
        # Imprimir pila original.
        print("Pila original:")
        imprimir_pila(pila, "Números")
        
        # Ordenar pila.
        pila_ordenada = ordenar_pila(pila)
        
        # Imprimir pila ordenada.
        print("Pila ordenada:")
        imprimir_pila(pila_ordenada, "Números")

if __name__ == "__main__":
    main()