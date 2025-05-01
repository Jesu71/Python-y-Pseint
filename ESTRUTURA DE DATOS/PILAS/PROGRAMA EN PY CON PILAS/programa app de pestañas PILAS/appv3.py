class Pila:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        return "No hay pestañas abiertas."

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return "No hay pestañas abiertas."

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def buscar_pestaña(self, nombre):
        # Crear pila auxiliar para buscar sin modificar la original.
        pila_auxiliar = Pila()
        indice = -1
        
        while not self.empty():
            pestaña_actual = self.pop()
            
            # Comparar sin distinguir mayúsculas y minúsculas.
            if pestaña_actual.lower() == nombre.lower():
                indice = 0  # Marca que se encontró.
            
            # Apilar en la pila auxiliar.
            pila_auxiliar.push(pestaña_actual)
        
        # Restaurar la pila original.
        while not pila_auxiliar.empty():
            self.push(pila_auxiliar.pop())
        
        return indice

    def eliminar_pestaña(self, nombre):
        # Crear pila auxiliar para eliminar sin modificar la original.
        pila_auxiliar = Pila()
        eliminado = False
        
        while not self.empty():
            pestaña_actual = self.pop()
            
            # Comparar sin distinguir mayúsculas y minúsculas.
            if not eliminado and pestaña_actual.lower() == nombre.lower():
                eliminado = True
                continue  # Salta esta pestaña
            
            # Apilar en la pila auxiliar.
            pila_auxiliar.push(pestaña_actual)
        
        # Restaurar la pila original.
        while not pila_auxiliar.empty():
            self.push(pila_auxiliar.pop())
        
        return eliminado

def menu():
    pila = Pila()
    while True:
        print("\nMenú de navegación por pestañas:")
        print("1. Abrir nueva pestaña")
        print("2. Cerrar pestaña actual")
        print("3. Ver pestaña actual")
        print("4. Verificar si hay pestañas abiertas")
        print("5. Contar pestañas abiertas")
        print("6. Cerrar todas las pestañas")
        print("7. Buscar y ver pestaña")
        print("8. Eliminar pestaña específica")
        print("9. Listar todas las pestañas")
        print("10. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Ingresa el nombre de la pestaña: ")
            pila.push(nombre)
            print(f"Pestaña '{nombre}' abierta.")
        
        elif opcion == "2":
            if not pila.empty():
                print(f"Cerrando pestaña: {pila.pop()}")
            else:
                print("No hay pestañas abiertas.")
        
        elif opcion == "3":
            print(f"Pestaña actual: {pila.top()}")
        
        elif opcion == "4":
            print("Hay pestañas abiertas." if not pila.empty() else "No hay pestañas abiertas.")
        
        elif opcion == "5":
            print(f"Número de pestañas abiertas: {pila.size()}")
        
        elif opcion == "6":
            pila.clear()
            print("Todas las pestañas han sido cerradas.")
        
        elif opcion == "7":
            if not pila.empty():
                nombre = input("Ingresa el nombre de la pestaña a buscar: ")
                indice = pila.buscar_pestaña(nombre)
                if indice != -1:
                    print(f"Pestaña encontrada: {nombre}")
                else:
                    print("Pestaña no encontrada.")
            else:
                print("No hay pestañas abiertas.")
        
        elif opcion == "8":
            if not pila.empty():
                nombre = input("Ingresa el nombre de la pestaña a eliminar: ")
                if pila.eliminar_pestaña(nombre):
                    print(f"Pestaña '{nombre}' eliminada.")
                else:
                    print("Pestaña no encontrada.")
            else:
                print("No hay pestañas abiertas.")
        
        elif opcion == "9":
            if not pila.empty():
                print("Pestañas abiertas:")
                pila_temporal = Pila()
                contador = 1
                while not pila.empty():
                    pestaña = pila.pop()
                    print(f"{contador}. {pestaña}")
                    pila_temporal.push(pestaña)
                    contador += 1
                
                # Restaurar la pila original
                while not pila_temporal.empty():
                    pila.push(pila_temporal.pop())
            else:
                print("No hay pestañas abiertas.")
        
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()