class Operacion:
    def __init__(self, tipo, monto, fecha):
        """
        Inicializa una nueva operación financiera
        
        Parámetros:
        - tipo: str - Tipo de operación ('depósito' o 'retiro')
        - monto: float - Cantidad de dinero de la operación
        - fecha: str - Fecha en que se realizó la operación
        """
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha
    
    def __str__(self):
        """Representación en cadena de la operación para visualización"""
        return f"[{self.fecha}] {self.tipo.capitalize()}: ${self.monto:.2f}"


class PilaOperaciones:
    def __init__(self):
        """Inicializa una pila vacía para almacenar operaciones"""
        self.items = []
    
    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        return len(self.items) == 0
    
    def apilar(self, operacion):
        """
        Agrega una operación al tope de la pila
        
        Parámetros:
        - operacion: Operacion - La operación a agregar
        """
        self.items.append(operacion)
        return f"Operación de {operacion.tipo} por ${operacion.monto:.2f} registrada correctamente"
    
    def desapilar(self):
        """
        Elimina y devuelve la operación del tope de la pila
        
        Retorna:
        - La operación más reciente o None si la pila está vacía
        """
        if self.esta_vacia():
            return None
        return self.items.pop()
    
    def tope(self):
        """
        Devuelve la operación en el tope de la pila sin eliminarla
        
        Retorna:
        - La operación más reciente o None si la pila está vacía
        """
        if self.esta_vacia():
            return None
        return self.items[-1]
    
    def tamano(self):
        """Retorna el número de operaciones en la pila"""
        return len(self.items)


class AppFinanciera:
    def __init__(self):
        """Inicializa la aplicación financiera con una pila vacía de operaciones"""
        self.pila_operaciones = PilaOperaciones()
        self.saldo = 0.0
    
    def registrar_operacion(self, tipo, monto, fecha):
        """
        Registra una nueva operación financiera
        
        Parámetros:
        - tipo: str - Tipo de operación ('depósito' o 'retiro')
        - monto: float - Cantidad de dinero
        - fecha: str - Fecha de la operación
        
        Retorna:
        - Mensaje de confirmación o error
        """
        # Validar que el monto sea positivo
        if monto <= 0:
            return "Error: El monto debe ser mayor que cero"
        
        # Validar que no se retire más dinero del disponible
        if tipo.lower() == 'retiro' and monto > self.saldo:
            return f"Error: Saldo insuficiente. Su saldo actual es ${self.saldo:.2f}"
        
        # Actualizar el saldo
        if tipo.lower() == 'depósito' or tipo.lower() == 'deposito':
            self.saldo += monto
        elif tipo.lower() == 'retiro':
            self.saldo -= monto
        else:
            return "Error: Tipo de operación inválido. Use 'depósito' o 'retiro'"
        
        # Crear y registrar la operación
        nueva_operacion = Operacion(tipo.lower(), monto, fecha)
        mensaje = self.pila_operaciones.apilar(nueva_operacion)
        return f"{mensaje}. Saldo actual: ${self.saldo:.2f}"
    
    def mostrar_historial(self):
        """
        Muestra el historial completo desde la operación más reciente
        
        Retorna:
        - Lista de operaciones o mensaje si no hay operaciones
        """
        if self.pila_operaciones.esta_vacia():
            return "No hay operaciones registradas"
        
        # Crear una copia de la pila para no alterar la original
        pila_temp = PilaOperaciones()
        historial = []
        
        # Desapilar todas las operaciones y mostrarlas
        while not self.pila_operaciones.esta_vacia():
            operacion = self.pila_operaciones.desapilar()
            historial.append(operacion)
            pila_temp.apilar(operacion)
        
        # Volver a apilar todas las operaciones en la pila original
        while not pila_temp.esta_vacia():
            self.pila_operaciones.apilar(pila_temp.desapilar())
        
        return historial
    
    def eliminar_ultima_operacion(self, confirmacion):
        """
        Elimina la última operación registrada (con confirmación)
        
        Parámetros:
        - confirmacion: str - Confirmación del usuario ('si' o 'no')
        
        Retorna:
        - Mensaje de confirmación o cancelación
        """
        if self.pila_operaciones.esta_vacia():
            return "No hay operaciones para eliminar"
        
        if confirmacion.lower() != 'si':
            return "Operación cancelada"
        
        # Obtener la última operación para mostrarla
        ultima_operacion = self.pila_operaciones.desapilar()
        
        # Revertir el efecto de la operación en el saldo
        if ultima_operacion.tipo == 'depósito' or ultima_operacion.tipo == 'deposito':
            self.saldo -= ultima_operacion.monto
        else:  # retiro
            self.saldo += ultima_operacion.monto
            
        return f"Última operación eliminada: {ultima_operacion}. Nuevo saldo: ${self.saldo:.2f}"
    
    def mostrar_totales(self):
        """
        Muestra el total de retiros y depósitos
        
        Retorna:
        - Diccionario con totales o mensaje si no hay operaciones
        """
        if self.pila_operaciones.esta_vacia():
            return "No hay operaciones registradas"
        
        # Crear una copia de la pila para no alterar la original
        pila_temp = PilaOperaciones()
        total_depositos = 0.0
        total_retiros = 0.0
        num_depositos = 0
        num_retiros = 0
        
        # Recorrer todas las operaciones y calcular los totales
        while not self.pila_operaciones.esta_vacia():
            operacion = self.pila_operaciones.desapilar()
            
            if operacion.tipo == 'depósito' or operacion.tipo == 'deposito':
                total_depositos += operacion.monto
                num_depositos += 1
            else:  # retiro
                total_retiros += operacion.monto
                num_retiros += 1
                
            pila_temp.apilar(operacion)
        
        # Volver a apilar todas las operaciones en la pila original
        while not pila_temp.esta_vacia():
            self.pila_operaciones.apilar(pila_temp.desapilar())
        
        return {
            "num_depositos": num_depositos,
            "total_depositos": total_depositos,
            "num_retiros": num_retiros,
            "total_retiros": total_retiros
        }
    
    def mostrar_saldo(self):
        """
        Muestra el saldo final acumulado
        
        Retorna:
        - Saldo actual
        """
        return self.saldo


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear la aplicación financiera
    app = AppFinanciera()
    
    # Registrar algunas operaciones
    print(app.registrar_operacion("depósito", 1000.00, "2025-04-10"))
    print(app.registrar_operacion("retiro", 200.50, "2025-04-12"))
    print(app.registrar_operacion("depósito", 350.75, "2025-04-15"))
    print(app.registrar_operacion("retiro", 50.00, "2025-04-18"))
    print(app.registrar_operacion("depósito", 1200.00, "2025-04-20"))
    
    # Mostrar el historial completo
    print("\nHISTORIAL DE OPERACIONES (desde la más reciente):")
    historial = app.mostrar_historial()
    for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")
    
    # Mostrar totales
    print("\nTOTALES:")
    totales = app.mostrar_totales()
    print(f"Depósitos: {totales['num_depositos']} operaciones por un total de ${totales['total_depositos']:.2f}")
    print(f"Retiros: {totales['num_retiros']} operaciones por un total de ${totales['total_retiros']:.2f}")
    
    # Mostrar saldo actual
    print(f"\nSALDO ACTUAL: ${app.mostrar_saldo():.2f}")
    
    # Eliminar la última operación
    print("\nELIMINAR ÚLTIMA OPERACIÓN:")
    confirmacion = input("¿Está seguro de eliminar la última operación? (si/no): ")
    print(app.eliminar_ultima_operacion(confirmacion))
    
    # Mostrar historial actualizado
    print("\nHISTORIAL ACTUALIZADO:")
    historial = app.mostrar_historial()
    for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")
    
    # Mostrar saldo actualizado
    print(f"\nSALDO ACTUALIZADO: ${app.mostrar_saldo():.2f}")