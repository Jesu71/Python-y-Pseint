class Cliente:
    def __init__(self, nombre, documento, motivo):
        # Inicializa un cliente con nombre, documento y motivo.
        self.nombre = nombre
        self.documento = documento
        self.motivo = motivo
    
    def __str__(self):
        # Representación en texto del cliente.
        return f"Cliente: {self.nombre}, Documento: {self.documento}, Motivo: {self.motivo}"

class Cola:
    def __init__(self):
        # Inicializa una cola vacía.
        self.items = []
    
    def esta_vacia(self):
        # Verifica si la cola está vacía.
        return len(self.items) == 0
    
    def encolar(self, cliente):
        # Agrega un cliente al final de la cola.
        self.items.append(cliente)
        return f"Cliente {cliente.nombre} agregado a la cola."
    
    def desencolar(self):
        # Elimina y retorna el cliente del frente.
        if self.esta_vacia():
            return None
        return self.items.pop(0)
    
    def frente(self):
        # Retorna el cliente del frente sin eliminarlo.
        if self.esta_vacia():
            return None
        return self.items[0]
    
    def tamano(self):
        # Retorna el número de clientes en la cola.
        return len(self.items)
    
    def vaciar(self):
        # Vacía la cola.
        self.items = []
        return "La cola ha sido vaciada."

class CentroSoporte:
    def __init__(self):
        # Inicializa el centro con una cola vacía.
        self.cola_clientes = Cola()
    
    def registrar_cliente(self, nombre, documento, motivo):
        # Registra un cliente en la cola.
        nuevo_cliente = Cliente(nombre, documento, motivo)
        return self.cola_clientes.encolar(nuevo_cliente)
    
    def mostrar_estado_cola(self):
        # Muestra los clientes en la cola.
        if self.cola_clientes.esta_vacia():
            return "No hay clientes en espera."
        
        estado = []
        for i, cliente in enumerate(self.cola_clientes.items, 1):
            estado.append(f"{i}. {cliente}")
        
        return estado
    
    def atender_siguiente_cliente(self):
        # Atiende al siguiente cliente.
        cliente = self.cola_clientes.desencolar()
        if cliente is None:
            return "No hay clientes en espera."
        return f"Atendiendo a: {cliente}"
    
    def clientes_en_espera(self):
        # Retorna el número de clientes en espera.
        return self.cola_clientes.tamano()
    
    def buscar_cliente_por_nombre(self, nombre):
        # Busca un cliente por nombre.
        if self.cola_clientes.esta_vacia():
            return "No hay clientes en la cola."
        
        resultados = []
        for i, cliente in enumerate(self.cola_clientes.items, 1):
            if nombre.lower() in cliente.nombre.lower():
                resultados.append(f"Cliente {cliente.nombre} en posición {i}.")
        
        if not resultados:
            return f"No se encontró ningún cliente con el nombre '{nombre}'."
        
        return resultados
    
    def reiniciar_cola(self, confirmacion):
        # Reinicia la cola si se confirma.
        if confirmacion.lower() == 'si':
            self.cola_clientes.vaciar()
            return "Cola reiniciada."
        else:
            return "Operación cancelada."

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear el centro de soporte.
    centro = CentroSoporte()
    
    # Registrar clientes.
    centro.registrar_cliente("Ana Gómez", "12345678", "Problema con impresora")
    centro.registrar_cliente("Juan Pérez", "87654321", "Configuración de red")
    centro.registrar_cliente("María López", "23456789", "Actualización de software")
    centro.registrar_cliente("Carlos Rodríguez", "98765432", "Problema con email")
    centro.registrar_cliente("Ana María Silva", "34567890", "Instalación de programa")
    
    # Mostrar estado de la cola.
    print("ESTADO ACTUAL DE LA COLA:")
    estado = centro.mostrar_estado_cola()
    for linea in estado:
        print(linea)
    
    # Mostrar clientes en espera.
    print(f"\nClientes en espera: {centro.clientes_en_espera()}")
    
    # Buscar cliente por nombre.
    print("\nBÚSQUEDA DE CLIENTE:")
    resultados = centro.buscar_cliente_por_nombre("Ana")
    if isinstance(resultados, list):
        for resultado in resultados:
            print(resultado)
    else:
        print(resultados)
    
    # Atender al siguiente cliente.
    print("\nATENDIENDO AL SIGUIENTE CLIENTE:")
    print(centro.atender_siguiente_cliente())
    
    # Mostrar estado de la cola después de atender.
    print("\nESTADO DE LA COLA DESPUÉS DE ATENDER:")
    estado = centro.mostrar_estado_cola()
    for linea in estado:
        print(linea)
    
    # Mostrar clientes en espera después de atender.
    print(f"\nClientes en espera ahora: {centro.clientes_en_espera()}")
    
    # Reiniciar cola con confirmación.
    print("\nREINICIAR COLA:")
    confirmacion = input("¿Está seguro de reiniciar la cola? (si/no): ")
    print(centro.reiniciar_cola(confirmacion))
    
    # Verificar estado final.
    print("\nESTADO FINAL DE LA COLA:")
    estado = centro.mostrar_estado_cola()
    if isinstance(estado, list):
        for linea in estado:
            print(linea)
    else:
        print(estado)