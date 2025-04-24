# Clase que implementa una cola utilizando una lista.
class Cola:
    def __init__(self):
        # Inicializa una lista vacía para representar la cola.
        self.queue = []

    def insertar(self, item):
        # Agrega un elemento al final de la cola.
        self.queue.append(item)

    def eliminar(self):
        # Elimina y devuelve el primer elemento de la cola si no está vacía.
        if not self.vacia():
            return self.queue.pop(0)
        else:
            # Devuelve un mensaje si la cola está vacía.
            return "La cola está vacía."

    def mostrar(self):
        # Devuelve todos los elementos de la cola si no está vacía.
        if not self.vacia():
            return self.queue
        else:
            # Devuelve un mensaje si la cola está vacía.
            return "La cola está vacía."

    def vacia(self):
        # Verifica si la cola está vacía.
        return len(self.queue) == 0


# Función que implementa el menú interactivo para trabajar con la cola.
def menu():
    # Crea una instancia de la clase Cola.
    cola = Cola()
    while True:
        # Muestra el menú de opciones al usuario.
        print("\nMenú:")
        print("1. Insertar un carácter a una cola")
        print("2. Mostrar todos los elementos de la cola")
        print("3. Eliminar un elemento de una cola")
        print("4. Salir")
        # Solicita al usuario que seleccione una opción.
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Opción 1: Insertar un carácter en la cola.
            caracter = input("Ingresa un carácter: ")
            cola.insertar(caracter)
            print(f"'{caracter}' ha sido insertado en la cola.")
        elif opcion == "2":
            # Opción 2: Mostrar todos los elementos de la cola.
            print("Elementos en la cola:", cola.mostrar())
        elif opcion == "3":
            # Opción 3: Eliminar el primer elemento de la cola.
            eliminado = cola.eliminar()
            print(f"Elemento eliminado: {eliminado}")
        elif opcion == "4":
            # Opción 4: Salir del programa.
            print("Saliendo del programa...")
            break
        else:
            # Mensaje de error si la opción ingresada no es válida.
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()