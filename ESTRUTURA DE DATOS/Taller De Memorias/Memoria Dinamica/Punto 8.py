# Lista vacía para representar la pila.
pila = []

# Función para agregar un elemento a la pila (push).
def push(elemento):
    pila.append(elemento)
    print(f"Elemento {elemento} agregado a la pila.")

# Función para eliminar el último elemento agregado (pop).
def pop():
    if pila:
        elemento = pila.pop()
        print(f"Elemento {elemento} eliminado de la pila.")
    else:
        print("La pila está vacía, no se puede eliminar ningún elemento.")

# Función para mostrar la pila.
def mostrar_pila():
    print("Estado actual de la pila:", pila)

# CONSOLA. 
while True:
    print("\nOpciones:")
    print("1. Push (agregar elemento)")
    print("2. Pop (eliminar elemento)")
    print("3. Mostrar pila")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        push(elemento)
    elif opcion == "2":
        pop()
    elif opcion == "3":
        mostrar_pila()
    elif opcion == "4":
        print("Finalizando la ejecución.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")