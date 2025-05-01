class Alerta:
    def __init__(self, tipo, prioridad, hora):
        # Inicializa una alerta con tipo, prioridad y hora.
        self.tipo = tipo
        self.prioridad = prioridad
        self.hora = hora
    
    def __str__(self):
        # Representación en texto de la alerta.
        return f"[{self.hora}] {self.tipo} - Prioridad: {self.prioridad}"

class PilaAlertas:
    def __init__(self):
        # Inicializa una pila vacía.
        self.items = []
    
    def esta_vacia(self):
        # Verifica si la pila está vacía.
        return len(self.items) == 0
    
    def apilar(self, alerta):
        # Agrega una alerta al tope de la pila.
        self.items.append(alerta)
        return f"Alerta de {alerta.tipo} registrada con éxito"
    
    def desapilar(self):
        # Elimina y retorna la alerta del tope.
        if self.esta_vacia():
            return None
        return self.items.pop()
    
    def tope(self):
        # Retorna la alerta en el tope sin eliminarla.
        if self.esta_vacia():
            return None
        return self.items[-1]
    
    def tamano(self):
        # Retorna el número de alertas en la pila.
        return len(self.items)
    
    def vaciar(self):
        # Elimina todas las alertas de la pila.
        self.items = []
        return "Todas las alertas han sido eliminadas"

class SistemaSeguridad:
    def __init__(self):
        # Inicializa el sistema con una pila vacía.
        self.pila_alertas = PilaAlertas()
    
    def registrar_alerta(self, tipo, prioridad, hora):
        # Registra una nueva alerta en el sistema.
        nueva_alerta = Alerta(tipo, prioridad, hora)
        return self.pila_alertas.apilar(nueva_alerta)
    
    def mostrar_todas_alertas(self):
        # Muestra todas las alertas en orden inverso.
        if self.pila_alertas.esta_vacia():
            return "No hay alertas registradas"
        
        pila_temp = PilaAlertas()
        alertas_ordenadas = []
        
        while not self.pila_alertas.esta_vacia():
            alerta = self.pila_alertas.desapilar()
            alertas_ordenadas.append(alerta)
            pila_temp.apilar(alerta)
        
        while not pila_temp.esta_vacia():
            self.pila_alertas.apilar(pila_temp.desapilar())
        
        return alertas_ordenadas
    
    def revisar_ultima_alerta(self):
        # Elimina y retorna la última alerta ingresada.
        alerta = self.pila_alertas.desapilar()
        if alerta is None:
            return "No hay alertas para revisar"
        return f"Alerta revisada: {alerta}"
    
    def hay_alertas_pendientes(self):
        # Verifica si hay alertas pendientes.
        return not self.pila_alertas.esta_vacia()
    
    def borrar_todas_alertas(self):
        # Elimina todas las alertas del sistema.
        return self.pila_alertas.vaciar()
    
    def mostrar_alertas_alta_prioridad(self):
        # Muestra solo las alertas con prioridad alta.
        if self.pila_alertas.esta_vacia():
            return "No hay alertas registradas"
        
        pila_temp = PilaAlertas()
        alertas_alta_prioridad = []
        
        while not self.pila_alertas.esta_vacia():
            alerta = self.pila_alertas.desapilar()
            if alerta.prioridad.lower() == 'alto':
                alertas_alta_prioridad.append(alerta)
            pila_temp.apilar(alerta)
        
        while not pila_temp.esta_vacia():
            self.pila_alertas.apilar(pila_temp.desapilar())
        
        if not alertas_alta_prioridad:
            return "No hay alertas de alta prioridad"
        
        return alertas_alta_prioridad

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear el sistema de seguridad.
    sistema = SistemaSeguridad()
    
    # Registrar algunas alertas.
    sistema.registrar_alerta("Movimiento", "alto", "08:30")
    sistema.registrar_alerta("Temperatura", "medio", "09:15")
    sistema.registrar_alerta("Apertura de puerta", "alto", "10:45")
    sistema.registrar_alerta("Ventana abierta", "bajo", "11:20")
    sistema.registrar_alerta("Movimiento", "alto", "12:05")
    
    # Mostrar todas las alertas.
    print("TODAS LAS ALERTAS (más reciente primero):")
    alertas = sistema.mostrar_todas_alertas()
    for i, alerta in enumerate(alertas, 1):
        print(f"{i}. {alerta}")
    
    # Verificar si hay alertas pendientes.
    print("\nHay alertas pendientes:", sistema.hay_alertas_pendientes())
    
    # Mostrar solo alertas de alta prioridad.
    print("\nALERTAS DE ALTA PRIORIDAD:")
    alertas_altas = sistema.mostrar_alertas_alta_prioridad()
    if isinstance(alertas_altas, list):
        for i, alerta in enumerate(alertas_altas, 1):
            print(f"{i}. {alerta}")
    else:
        print(alertas_altas)
    
    # Revisar la última alerta.
    print("\nRevisando última alerta:")
    print(sistema.revisar_ultima_alerta())
    
    # Mostrar todas las alertas después de revisar una.
    print("\nALERTAS DESPUÉS DE REVISAR LA ÚLTIMA:")
    alertas = sistema.mostrar_todas_alertas()
    for i, alerta in enumerate(alertas, 1):
        print(f"{i}. {alerta}")
    
    # Borrar todas las alertas.
    print("\n" + sistema.borrar_todas_alertas())
    
    # Verificar si hay alertas pendientes después de borrar todas.
    print("Hay alertas pendientes después de borrar:", sistema.hay_alertas_pendientes())