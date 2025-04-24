class Operacion:
    def __init__(self, tipo, monto, fecha):
        # Inicializa una operación con tipo, monto y fecha
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha
    
    def __str__(self):
        # Formato de cadena para mostrar la operación
        return f"[{self.fecha}] {self.tipo.capitalize()}: ${self.monto:.2f}"

class PilaOperaciones:
    def __init__(self):
        # Crea una pila vacía
        self.items = []
    
    def esta_vacia(self):
        # Verifica si la pila está vacía
        return len(self.items) == 0
    
    def apilar(self, operacion):
        # Agrega una operación al tope
        self.items.append(operacion)
        return f"Operación de {operacion.tipo} por ${operacion.monto:.2f} registrada correctamente"
    
    def desapilar(self):
        # Quita y devuelve la operación del tope
        if self.esta_vacia():
            return None
        return self.items.pop()
    
    def tope(self):
        # Devuelve la operación del tope sin eliminarla
        if self.esta_vacia():
            return None
        return self.items[-1]
    
    def tamano(self):
        # Retorna el número de operaciones
        return len(self.items)

class AppFinanciera:
    def __init__(self):
        # Inicializa la app con pila vacía y saldo en cero
        self.pila_operaciones = PilaOperaciones()
        self.saldo = 0.0
    
    def registrar_operacion(self, tipo, monto, fecha):
        # Registra un depósito o retiro
        if monto <= 0:
            return "Error: El monto debe ser mayor que cero"
        
        if tipo.lower() == 'retiro' and monto > self.saldo:
            return f"Error: Saldo insuficiente. Su saldo actual es ${self.saldo:.2f}"
        
        if tipo.lower() == 'depósito' or tipo.lower() == 'deposito':
            self.saldo += monto
        elif tipo.lower() == 'retiro':
            self.saldo -= monto
        else:
            return "Error: Tipo de operación inválido. Use 'depósito' o 'retiro'"
        
        nueva_operacion = Operacion(tipo.lower(), monto, fecha)
        mensaje = self.pila_operaciones.apilar(nueva_operacion)
        return f"{mensaje}. Saldo actual: ${self.saldo:.2f}"
    
    def mostrar_historial(self):
        # Muestra operaciones desde la más reciente
        if self.pila_operaciones.esta_vacia():
            return "No hay operaciones registradas"
        
        pila_temp = PilaOperaciones()
        historial = []
        
        # Desapila para mostrar y guarda temporalmente
        while not self.pila_operaciones.esta_vacia():
            operacion = self.pila_operaciones.desapilar()
            historial.append(operacion)
            pila_temp.apilar(operacion)
        
        # Restaura las operaciones originales
        while not pila_temp.esta_vacia():
            self.pila_operaciones.apilar(pila_temp.desapilar())
        
        return historial
    
    def eliminar_ultima_operacion(self, confirmacion):
        # Elimina la última operación si se confirma
        if self.pila_operaciones.esta_vacia():
            return "No hay operaciones para eliminar"
        
        if confirmacion.lower() != 'si':
            return "Operación cancelada"
        
        ultima_operacion = self.pila_operaciones.desapilar()
        
        if ultima_operacion.tipo == 'depósito' or ultima_operacion.tipo == 'deposito':
            self.saldo -= ultima_operacion.monto
        else:
            self.saldo += ultima_operacion.monto
            
        return f"Última operación eliminada: {ultima_operacion}. Nuevo saldo: ${self.saldo:.2f}"
    
    def mostrar_totales(self):
        # Muestra totales de depósitos y retiros
        if self.pila_operaciones.esta_vacia():
            return "No hay operaciones registradas"
        
        pila_temp = PilaOperaciones()
        total_depositos = 0.0
        total_retiros = 0.0
        num_depositos = 0
        num_retiros = 0
        
        # Suma totales según tipo
        while not self.pila_operaciones.esta_vacia():
            operacion = self.pila_operaciones.desapilar()
            
            if operacion.tipo == 'depósito' or operacion.tipo == 'deposito':
                total_depositos += operacion.monto
                num_depositos += 1
            else:
                total_retiros += operacion.monto
                num_retiros += 1
                
            pila_temp.apilar(operacion)
        
        # Restaura la pila original
        while not pila_temp.esta_vacia():
            self.pila_operaciones.apilar(pila_temp.desapilar())
        
        return {
            "num_depositos": num_depositos,
            "total_depositos": total_depositos,
            "num_retiros": num_retiros,
            "total_retiros": total_retiros
        }
    
    def mostrar_saldo(self):
        # Retorna el saldo actual
        return self.saldo

# Ejemplo de uso
if __name__ == "__main__":
    app = AppFinanciera()
    
    print(app.registrar_operacion("depósito", 1000.00, "2025-04-10"))
    print(app.registrar_operacion("retiro", 200.50, "2025-04-12"))
    print(app.registrar_operacion("depósito", 350.75, "2025-04-15"))
    print(app.registrar_operacion("retiro", 50.00, "2025-04-18"))
    print(app.registrar_operacion("depósito", 1200.00, "2025-04-20"))
    
    print("\nHISTORIAL DE OPERACIONES (desde la más reciente):")
    historial = app.mostrar_historial()
    for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")
    
    print("\nTOTALES:")
    totales = app.mostrar_totales()
    print(f"Depósitos: {totales['num_depositos']} operaciones por un total de ${totales['total_depositos']:.2f}")
    print(f"Retiros: {totales['num_retiros']} operaciones por un total de ${totales['total_retiros']:.2f}")
    
    print(f"\nSALDO ACTUAL: ${app.mostrar_saldo():.2f}")
    
    print("\nELIMINAR ÚLTIMA OPERACIÓN:")
    confirmacion = input("¿Está seguro de eliminar la última operación? (si/no): ")
    print(app.eliminar_ultima_operacion(confirmacion))
    
    print("\nHISTORIAL ACTUALIZADO:")
    historial = app.mostrar_historial()
    for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")
    
    print(f"\nSALDO ACTUALIZADO: ${app.mostrar_saldo():.2f}")
