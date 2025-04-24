# Diccionario vacío para almacenar información de estudiantes
estudiantes = {}

# Función para agregar un estudiante.
def agregar_estudiante(nombre, edad):
    if nombre in estudiantes:
        print(f"El estudiante {nombre} ya existe en el registro.")
    else:
        estudiantes[nombre] = edad
        print(f"Estudiante {nombre} agregado con éxito.")

# Función para eliminar un estudiante.
def eliminar_estudiante(nombre):
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado con éxito.")
    else:
        print(f"El estudiante {nombre} no existe en el registro.")

# Función para modificar la edad de un estudiante.
def modificar_estudiante(nombre, nueva_edad):
    if nombre in estudiantes:
        estudiantes[nombre] = nueva_edad
        print(f"Edad del estudiante {nombre} modificada a {nueva_edad}.")
    else:
        print(f"El estudiante {nombre} no existe en el registro.")

# Función para mostrar todos los estudiantes.
def mostrar_estudiantes():
    if estudiantes:
        print("Lista de estudiantes:")
        for nombre, edad in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {edad}")
    else:
        print("No hay estudiantes registrados.")

# CONSOLA. 
while True:
    print("\nOpciones:")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Modificar estudiante")
    print("4. Mostrar estudiantes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = input("Ingrese la edad del estudiante: ")
        agregar_estudiante(nombre, edad)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")
        eliminar_estudiante(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante a modificar: ")
        nueva_edad = input("Ingrese la nueva edad del estudiante: ")
        modificar_estudiante(nombre, nueva_edad)
    elif opcion == "4":
        mostrar_estudiantes()
    elif opcion == "5":
        print("Finalizando la ejecución.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")