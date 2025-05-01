# Clase para representar a un cliente del banco.
class Cliente:
    def __init__(self, id, nombre, edad, saldo):
        # Inicializa los atributos del cliente
        self.id = id            # Identificador único del cliente
        self.nombre = nombre    # Nombre completo del cliente
        self.edad = edad        # Edad del cliente
        self.saldo = saldo      # Saldo actual del cliente
    
    def __str__(self):
        # Método para convertir los datos del cliente en una cadena formateada
        # El saldo se formatea con separadores de miles y dos decimales
        return f"ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Saldo: ${self.saldo:,.2f}"

# Clase para manejar la cola de clientes del banco
class ColaBanco:
    def __init__(self):
        # Inicializa una lista vacía que funcionará como cola
        self.cola = []
    
    def agregar_cliente(self, cliente):
        # Agrega un nuevo cliente al final de la cola
        self.cola.append(cliente)
        
    def mostrar_clientes(self):
        # Verifica si hay clientes en la cola
        if not self.cola:
            return "No hay clientes en la cola"
        # Une todos los clientes en un string, cada uno en una nueva línea
        return "\n".join(str(cliente) for cliente in self.cola)
    
    def esta_vacia(self):
        # Verifica si la cola está vacía
        return len(self.cola) == 0

# Función principal que ejecuta el programa
def main():
    # Crea una nueva instancia de la cola del banco
    cola_banco = ColaBanco()
    
    # Bucle principal del programa
    while True:
        # Muestra el menú de opciones
        print("\n=== Sistema de Gestión de Clientes del Banco ===")
        print("1. Agregar nuevo cliente")
        print("2. Mostrar todos los clientes")
        print("3. Salir")
        
        # Obtiene la opción del usuario
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            # Opción para agregar un nuevo cliente
            try:
                # Solicita los datos del nuevo cliente
                id = input("Ingrese ID del cliente: ")
                nombre = input("Ingrese nombre del cliente: ")
                edad = int(input("Ingrese edad del cliente: "))
                saldo = float(input("Ingrese saldo del cliente: "))
                
                # Crea un nuevo objeto Cliente y lo añade a la cola
                nuevo_cliente = Cliente(id, nombre, edad, saldo)
                cola_banco.agregar_cliente(nuevo_cliente)
                print("\n¡Cliente agregado exitosamente!")
                
            except ValueError:
                # Manejo de errores para entradas inválidas
                print("\nError: Por favor ingrese datos válidos")
                
        elif opcion == "2":
            # Opción para mostrar todos los clientes en la cola
            print("\n=== Clientes en el Banco ===")
            print(cola_banco.mostrar_clientes())
            
        elif opcion == "3":
            # Opción para salir del programa
            print("\n¡Gracias por usar el sistema!")
            break
            
        else:
            # Mensaje de error para opciones inválidas
            print("\nOpción no válida. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()