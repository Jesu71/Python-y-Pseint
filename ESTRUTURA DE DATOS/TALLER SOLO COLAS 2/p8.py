class Llamada:
    def __init__(self, id_llamada, tiempo_llegada, tiempo_estimado_resolucion):
        self.id_llamada = id_llamada
        self.tiempo_llegada = tiempo_llegada  # Momento en que la llamada entra al sistema
        self.tiempo_estimado_resolucion = tiempo_estimado_resolucion
        self.tiempo_inicio_atencion = None
        self.tiempo_fin_atencion = None
        self.operador_asignado = None
    
    def calcular_tiempo_espera(self, tiempo_actual):
        if self.tiempo_inicio_atencion:
            return self.tiempo_inicio_atencion - self.tiempo_llegada
        return tiempo_actual - self.tiempo_llegada
    
    def __str__(self):
        return f"Llamada {self.id_llamada}: llegada={self.tiempo_llegada}, estimado={self.tiempo_estimado_resolucion}"


class Operador:
    def __init__(self, id_operador):
        self.id_operador = id_operador
        self.llamada_actual = None
        self.tiempo_disponible = 0
        self.llamadas_atendidas = 0
        self.tiempo_total_atencion = 0
    
    def esta_disponible(self, tiempo_actual):
        return tiempo_actual >= self.tiempo_disponible and self.llamada_actual is None
    
    def asignar_llamada(self, llamada, tiempo_actual):
        self.llamada_actual = llamada
        llamada.operador_asignado = self
        llamada.tiempo_inicio_atencion = tiempo_actual
        self.tiempo_disponible = tiempo_actual + llamada.tiempo_estimado_resolucion
    
    def finalizar_llamada(self, tiempo_actual):
        if self.llamada_actual:
            self.llamada_actual.tiempo_fin_atencion = tiempo_actual
            tiempo_atencion = tiempo_actual - self.llamada_actual.tiempo_inicio_atencion
            self.tiempo_total_atencion += tiempo_atencion
            self.llamadas_atendidas += 1
            llamada_finalizada = self.llamada_actual
            self.llamada_actual = None
            return llamada_finalizada
        return None
    
    def obtener_eficiencia(self):
        if self.llamadas_atendidas == 0:
            return 0
        return self.tiempo_total_atencion / self.llamadas_atendidas
    
    def __str__(self):
        estado = "Ocupado" if self.llamada_actual else "Disponible"
        return f"Operador {self.id_operador}: {estado}, disponible en: {self.tiempo_disponible}"


class CentroAtencion:
    def __init__(self, num_operadores):
        self.cola_llamadas = []
        self.operadores = [Operador(i+1) for i in range(num_operadores)]
        self.tiempo_actual = 0
        self.llamadas_completadas = []
    
    def agregar_llamada(self, llamada):
        """Añade una nueva llamada a la cola"""
        llamada.tiempo_llegada = self.tiempo_actual
        self.cola_llamadas.append(llamada)
        print(f"Llamada {llamada.id_llamada} añadida a la cola en tiempo {self.tiempo_actual}")
    
    def asignar_llamadas(self):
        """Asigna llamadas en cola a operadores disponibles"""
        operadores_disponibles = [op for op in self.operadores if op.esta_disponible(self.tiempo_actual)]
        
        while operadores_disponibles and self.cola_llamadas:
            operador = operadores_disponibles.pop(0)
            llamada = self.cola_llamadas.pop(0)
            operador.asignar_llamada(llamada, self.tiempo_actual)
            print(f"Tiempo {self.tiempo_actual}: Llamada {llamada.id_llamada} asignada a Operador {operador.id_operador}")
    
    def actualizar_estado(self):
        """Actualiza el estado del centro avanzando el tiempo"""
        # Encontrar el próximo evento (finalización de llamada o nueva llamada)
        proximo_tiempo = float('inf')
        
        for op in self.operadores:
            if op.llamada_actual and op.tiempo_disponible < proximo_tiempo:
                proximo_tiempo = op.tiempo_disponible
        
        if proximo_tiempo < float('inf'):
            self.tiempo_actual = proximo_tiempo
            
            # Finalizar llamadas completadas
            for op in self.operadores:
                if op.tiempo_disponible == self.tiempo_actual and op.llamada_actual:
                    llamada_finalizada = op.finalizar_llamada(self.tiempo_actual)
                    if llamada_finalizada:
                        self.llamadas_completadas.append(llamada_finalizada)
                        print(f"Tiempo {self.tiempo_actual}: Llamada {llamada_finalizada.id_llamada} finalizada")
        else:
            # Si no hay eventos próximos, avanzamos el tiempo manualmente
            self.tiempo_actual += 1
    
    def simular_hasta(self, tiempo_final):
        """Simula el funcionamiento del centro hasta un tiempo determinado"""
        while self.tiempo_actual < tiempo_final:
            self.asignar_llamadas()
            self.actualizar_estado()
            
            # Si no hay más eventos y la cola está vacía, podemos terminar
            if not self.cola_llamadas and all(op.llamada_actual is None for op in self.operadores):
                break
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas sobre el funcionamiento del centro"""
        print("\n--- ESTADÍSTICAS DEL CENTRO DE ATENCIÓN ---")
        
        if not self.llamadas_completadas:
            print("No hay llamadas completadas para mostrar estadísticas")
            return
        
        # Tiempo promedio de espera
        tiempo_total_espera = sum(llamada.tiempo_inicio_atencion - llamada.tiempo_llegada 
                                for llamada in self.llamadas_completadas)
        tiempo_promedio_espera = tiempo_total_espera / len(self.llamadas_completadas)
        print(f"Tiempo promedio de espera: {tiempo_promedio_espera:.2f} unidades")
        
        # Tiempo promedio de manejo
        tiempo_total_manejo = sum(llamada.tiempo_fin_atencion - llamada.tiempo_inicio_atencion 
                                 for llamada in self.llamadas_completadas)
        tiempo_promedio_manejo = tiempo_total_manejo / len(self.llamadas_completadas)
        print(f"Tiempo promedio de manejo: {tiempo_promedio_manejo:.2f} unidades")
        
        # Estadísticas por operador
        print("\nEstadísticas por operador:")
        for op in self.operadores:
            if op.llamadas_atendidas > 0:
                eficiencia = op.obtener_eficiencia()
                print(f"Operador {op.id_operador}: {op.llamadas_atendidas} llamadas, tiempo promedio {eficiencia:.2f} unidades")
            else:
                print(f"Operador {op.id_operador}: sin llamadas atendidas")
        
        # Llamadas en cola
        if self.cola_llamadas:
            print(f"\nLlamadas aún en cola: {len(self.cola_llamadas)}")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear un centro con 3 operadores
    centro = CentroAtencion(3)
    
    # Agregar algunas llamadas con diferentes tiempos estimados de resolución
    centro.agregar_llamada(Llamada(1, centro.tiempo_actual, 5))
    centro.agregar_llamada(Llamada(2, centro.tiempo_actual, 3))
    centro.agregar_llamada(Llamada(3, centro.tiempo_actual, 7))
    
    # Avanzar el tiempo para procesar las llamadas iniciales
    centro.simular_hasta(10)
    
    # Agregar más llamadas
    centro.agregar_llamada(Llamada(4, centro.tiempo_actual, 4))
    centro.agregar_llamada(Llamada(5, centro.tiempo_actual, 6))
    
    # Continuar la simulación hasta el final
    centro.simular_hasta(30)
    
    # Mostrar estadísticas finales
    centro.mostrar_estadisticas()