class Pedido:
    def __init__(self, numero_orden, platillo, tiempo_preparacion):
        # Inicializa un pedido con número, platillo y tiempo.
        self.numero_orden = numero_orden
        self.platillo = platillo
        self.tiempo_preparacion = tiempo_preparacion
    
    def __str__(self):
        # Representación en texto del pedido.
        return f"Orden #{self.numero_orden}: {self.platillo} - {self.tiempo_preparacion} minutos"

class ColaPedidos:
    def __init__(self):
        # Inicializa una cola de pedidos vacía.
        self.pedidos = []
        self.ultimo_numero_orden = 0
    
    def esta_vacia(self):
        # Verifica si la cola está vacía.
        return len(self.pedidos) == 0
    
    def añadir_pedido(self, platillo, tiempo_preparacion):
        # Añade un pedido a la cola.
        self.ultimo_numero_orden += 1
        nuevo_pedido = Pedido(self.ultimo_numero_orden, platillo, tiempo_preparacion)
        self.pedidos.append(nuevo_pedido)
        print(f"Pedido añadido: {nuevo_pedido}")
        return nuevo_pedido
    
    def ver_pedidos(self):
        # Muestra todos los pedidos en la cola.
        if self.esta_vacia():
            print("No hay pedidos en cola.")
            return
        
        print("\n--- PEDIDOS EN COLA ---")
        for i, pedido in enumerate(self.pedidos):
            print(f"{i+1}. {pedido}")
        print("---------------------")
    
    def atender_pedido(self):
        # Atiende el primer pedido de la cola.
        if self.esta_vacia():
            print("No hay pedidos para atender.")
            return None
        
        pedido_atendido = self.pedidos.pop(0)
        print(f"Atendiendo: {pedido_atendido}")
        return pedido_atendido
    
    def calcular_tiempo_total(self):
        # Calcula el tiempo total de preparación.
        if self.esta_vacia():
            return 0
        
        tiempo_total = sum(pedido.tiempo_preparacion for pedido in self.pedidos)
        return tiempo_total
    
    def pedidos_largos(self):
        # Muestra pedidos con tiempo > 20 minutos.
        pedidos_mayor_20 = [p for p in self.pedidos if p.tiempo_preparacion > 20]
        
        if not pedidos_mayor_20:
            print("No hay pedidos con tiempo de preparación mayor a 20 minutos.")
            return
        
        print("\n--- PEDIDOS CON TIEMPO > 20 MINUTOS ---")
        for i, pedido in enumerate(pedidos_mayor_20):
            print(f"{i+1}. {pedido}")
        print("-------------------------------------")
    
    def cancelar_pedido(self, numero_orden):
        # Cancela un pedido por número de orden.
        for i, pedido in enumerate(self.pedidos):
            if pedido.numero_orden == numero_orden:
                confirmacion = input(f"¿Está seguro de cancelar la orden #{numero_orden} - {pedido.platillo}? (s/n): ")
                if confirmacion.lower() == 's':
                    pedido_cancelado = self.pedidos.pop(i)
                    print(f"Pedido cancelado: {pedido_cancelado}")
                    return True
                else:
                    print("Cancelación abortada.")
                    return False
        
        print(f"No se encontró un pedido con número de orden {numero_orden}.")
        return False

def menu_principal():
    # Muestra el menú principal del sistema.
    cola = ColaPedidos()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE PEDIDOS ===")
        print("1. Añadir pedido")
        print("2. Ver todos los pedidos")
        print("3. Atender pedido actual")
        print("4. Calcular tiempo total de preparación")
        print("5. Mostrar pedidos con tiempo > 20 minutos")
        print("6. Cancelar pedido")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            # Añadir un nuevo pedido.
            platillo = input("Nombre del platillo: ")
            while True:
                try:
                    tiempo = int(input("Tiempo estimado de preparación (minutos): "))
                    if tiempo <= 0:
                        print("El tiempo debe ser un número positivo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            cola.añadir_pedido(platillo, tiempo)
        
        elif opcion == "2":
            # Ver todos los pedidos en cola.
            cola.ver_pedidos()
        
        elif opcion == "3":
            # Atender el pedido actual.
            cola.atender_pedido()
        
        elif opcion == "4":
            # Calcular tiempo total de preparación.
            tiempo_total = cola.calcular_tiempo_total()
            print(f"Tiempo total estimado de preparación pendiente: {tiempo_total} minutos")
        
        elif opcion == "5":
            # Mostrar pedidos con tiempo > 20 minutos.
            cola.pedidos_largos()
        
        elif opcion == "6":
            # Cancelar un pedido por número de orden.
            if cola.esta_vacia():
                print("No hay pedidos para cancelar.")
                continue
                
            cola.ver_pedidos()
            while True:
                try:
                    num_orden = int(input("Ingrese el número de orden a cancelar: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            cola.cancelar_pedido(num_orden)
        
        elif opcion == "0":
            # Salir del sistema.
            print("¡Gracias por utilizar el sistema de gestión de pedidos!")
            break
        
        else:
            # Opción inválida.
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()