class Cola:
    def __init__(self):
        # Inicializa una lista vacía para representar la cola.
        self.cola = []

    def encolar(self, elemento):
        # Agrega un elemento al final de la cola.
        self.cola.append(elemento)
        print(f"Elemento {elemento} encolado.")

    def esta_vacia(self):
        # Verifica si la cola está vacía.
        return len(self.cola) == 0

    def tamaño(self):
        # Retorna el tamaño de la cola.
        return len(self.cola)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase Cola.
    cola = Cola()

    # Ingresar cinco elementos.
    elementos = [1, 2, 3, 4, 5]
    for elem in elementos:
        cola.encolar(elem)

    # Mostrar el tamaño actual de la cola.
    print("Tamaño de la cola después de ingresar cinco elementos:", cola.tamaño()) 