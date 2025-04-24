# Lista vacía para representar la cola.
cola = []

# Función para agregar un elemento a la cola (enqueue).
def enqueue(elemento):
    cola.append(elemento)
    print(f"Elemento {elemento} agregado a la cola.")

# Función para eliminar el primer elemento de la cola (dequeue).
def dequeue():
    if cola:
        elemento = cola.pop(0)
        print(f"Elemento {elemento} eliminado de la cola.")
    else:
        print("La cola está vacía, no se puede eliminar ningún elemento.")

# Función para mostrar la cola.
def mostrar_cola():
    print("Estado actual de la cola:", cola)

# CONSOLA.
while True:
    print("\nOpciones:")
    print("1. Enqueue (agregar elemento)")
    print("2. Dequeue (eliminar elemento)")
    print("3. Mostrar cola")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        enqueue(elemento)
    elif opcion == "2":
        dequeue()
    elif opcion == "3":
        mostrar_cola()
    elif opcion == "4":
        print("Finalizando la ejecución.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")