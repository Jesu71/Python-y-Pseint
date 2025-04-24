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

def separar_pares_impares(pila_original):
    """
    Separa los números pares e impares de una pila en dos pilas diferentes
    
    Args:
        pila_original (Pila): Pila original con números enteros
    
    Returns:
        tuple: Una tupla con dos pilas (pila_pares, pila_impares)
    """
    # Pilas para almacenar pares e impares.
    pila_pares = Pila()
    pila_impares = Pila()
    
    # Pila auxiliar para no perder el orden original.
    pila_auxiliar = Pila()
    
    # Separar elementos mientras la pila original no esté vacía.
    while not pila_original.esta_vacia():
        # Desapilar elemento de la pila original
        numero = pila_original.desapilar()
        
        # Apilar en pila auxiliar para conservar el orden.
        pila_auxiliar.apilar(numero)
        
        # Clasificar el número.
        if numero % 2 == 0:
            pila_pares.apilar(numero)
        else:
            pila_impares.apilar(numero)
    
    # Restaurar la pila original.
    while not pila_auxiliar.esta_vacia():
        pila_original.apilar(pila_auxiliar.desapilar())
    
    return pila_pares, pila_impares

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
    # Crear pila de ejemplo.
    pila_original = Pila()
    numeros = [5, 12, 7, 20, 15, 8, 3, 16]
    
    # Apilar números en orden inverso (para mantener orden original).
    for numero in reversed(numeros):
        pila_original.apilar(numero)
    
    print("Pila original:")
    imprimir_pila(pila_original, "Números")
    
    # Separar pares e impares.
    pila_pares, pila_impares = separar_pares_impares(pila_original)
    
    # Imprimir resultados.
    print("\nResultado de separación:")
    imprimir_pila(pila_pares, "Pares")
    imprimir_pila(pila_impares, "Impares")
    
    # Mostrar pila original restaurada
    print("\nPila original restaurada:")
    imprimir_pila(pila_original, "Números")

if __name__ == "__main__":
    main()