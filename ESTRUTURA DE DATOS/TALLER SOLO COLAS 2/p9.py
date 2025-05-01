class Vehiculo:
    def __init__(self, id_vehiculo, tiempo_llegada, tiempo_paso):
        self.id = id_vehiculo
        self.tiempo_llegada = tiempo_llegada  # Momento en que el vehículo llega al cruce
        self.tiempo_paso = tiempo_paso  # Tiempo que tarda en atravesar el cruce
        self.tiempo_salida = None  # Momento en que termina de pasar el cruce
    
    def calcular_tiempo_espera(self):
        if self.tiempo_salida is None:
            return None
        # Tiempo desde llegada hasta que comienza a pasar (tiempo_salida - tiempo_paso es cuando comenzó a pasar)
        return (self.tiempo_salida - self.tiempo_paso) - self.tiempo_llegada
    
    def __str__(self):
        return f"Vehículo {self.id}: llegada={self.tiempo_llegada}, tiempo_paso={self.tiempo_paso}"


class Calle:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_vehiculos = []
        self.vehiculos_pasados = []
        self.semaforo = "rojo"  # Puede ser "verde" o "rojo"
        self.tiempo_ultimo_cambio = 0
        self.tiempo_actual_paso = 0  # Tiempo acumulado pasando vehículos en el ciclo actual de verde
    
    def agregar_vehiculo(self, vehiculo):
        self.cola_vehiculos.append(vehiculo)
        return f"Vehículo {vehiculo.id} añadido a la cola de la calle {self.nombre}"
    
    def cambiar_semaforo(self, nuevo_estado, tiempo_actual):
        self.semaforo = nuevo_estado
        self.tiempo_ultimo_cambio = tiempo_actual
        self.tiempo_actual_paso = 0
        return f"Semáforo de calle {self.nombre} cambiado a {nuevo_estado} en tiempo {tiempo_actual}"
    
    def pasar_vehiculos(self, tiempo_actual, duracion_verde):
        """Permite el paso de vehículos cuando el semáforo está en verde"""
        if self.semaforo != "verde" or not self.cola_vehiculos:
            return []
        
        vehiculos_pasados_ahora = []
        tiempo_disponible = duracion_verde - self.tiempo_actual_paso
        
        while self.cola_vehiculos and tiempo_disponible > 0:
            proximo_vehiculo = self.cola_vehiculos[0]
            
            # Si el vehículo puede pasar completamente en el tiempo disponible
            if proximo_vehiculo.tiempo_paso <= tiempo_disponible:
                vehiculo = self.cola_vehiculos.pop(0)
                vehiculo.tiempo_salida = tiempo_actual + proximo_vehiculo.tiempo_paso
                self.tiempo_actual_paso += proximo_vehiculo.tiempo_paso
                tiempo_disponible -= proximo_vehiculo.tiempo_paso
                self.vehiculos_pasados.append(vehiculo)
                vehiculos_pasados_ahora.append(vehiculo)
            else:
                # No hay suficiente tiempo para que pase completamente
                break
        
        return vehiculos_pasados_ahora
    
    def estadisticas(self):
        """Calcula estadísticas para esta calle"""
        if not self.vehiculos_pasados:
            return {
                "vehiculos_en_cola": len(self.cola_vehiculos),
                "vehiculos_pasados": 0,
                "tiempo_espera_promedio": 0,
                "mensaje": f"Calle {self.nombre}: No hay vehículos que hayan pasado"
            }
        
        tiempos_espera = [v.calcular_tiempo_espera() for v in self.vehiculos_pasados]
        tiempo_promedio = sum(tiempos_espera) / len(tiempos_espera)
        
        return {
            "vehiculos_en_cola": len(self.cola_vehiculos),
            "vehiculos_pasados": len(self.vehiculos_pasados),
            "tiempo_espera_promedio": tiempo_promedio,
            "mensaje": f"Calle {self.nombre}: {len(self.vehiculos_pasados)} vehículos pasados, tiempo promedio de espera: {tiempo_promedio:.2f}"
        }


class CruceSemaforizado:
    def __init__(self, calles, duracion_verde, duracion_rojo):
        self.calles = {calle.nombre: calle for calle in calles}
        self.duracion_verde = duracion_verde
        self.duracion_rojo = duracion_rojo
        self.tiempo_actual = 0
        self.total_vehiculos_procesados = 0
        
        # Inicializamos los semáforos (el primero en verde, los demás en rojo)
        nombres_calles = list(self.calles.keys())
        self.calles[nombres_calles[0]].cambiar_semaforo("verde", 0)
        for nombre in nombres_calles[1:]:
            self.calles[nombre].cambiar_semaforo("rojo", 0)
        
        self.indice_calle_verde = 0
        self.nombres_calles = nombres_calles
    
    def agregar_vehiculo(self, vehiculo, nombre_calle):
        """Agrega un vehículo a la cola de una calle específica"""
        if nombre_calle in self.calles:
            mensaje = self.calles[nombre_calle].agregar_vehiculo(vehiculo)
            return mensaje
        return f"Error: La calle {nombre_calle} no existe en este cruce"
    
    def ciclo_semaforos(self):
        """Cambia los semáforos según el ciclo establecido"""
        self.indice_calle_verde = (self.indice_calle_verde + 1) % len(self.nombres_calles)
        nueva_calle_verde = self.nombres_calles[self.indice_calle_verde]
        
        # Cambiamos todos a rojo primero
        for nombre, calle in self.calles.items():
            if calle.semaforo == "verde":
                calle.cambiar_semaforo("rojo", self.tiempo_actual)
        
        # Luego cambiamos la siguiente calle a verde
        self.calles[nueva_calle_verde].cambiar_semaforo("verde", self.tiempo_actual)
        
        return f"Ciclo de semáforos cambiado. Ahora calle {nueva_calle_verde} en verde."
    
    def actualizar(self):
        """Actualiza el estado del cruce: permite el paso de vehículos y cambia semáforos"""
        # Verificar si es momento de cambiar los semáforos
        calle_verde = None
        for nombre, calle in self.calles.items():
            if calle.semaforo == "verde":
                calle_verde = calle
                if self.tiempo_actual - calle.tiempo_ultimo_cambio >= self.duracion_verde:
                    self.ciclo_semaforos()
                    break
        
        # Permitir que pasen vehículos en la calle con semáforo verde
        vehiculos_pasados = []
        for nombre, calle in self.calles.items():
            if calle.semaforo == "verde":
                nuevos_vehiculos = calle.pasar_vehiculos(self.tiempo_actual, self.duracion_verde)
                vehiculos_pasados.extend(nuevos_vehiculos)
                self.total_vehiculos_procesados += len(nuevos_vehiculos)
                
                for v in nuevos_vehiculos:
                    print(f"Tiempo {self.tiempo_actual}: Vehículo {v.id} pasó por la calle {nombre}")
        
        # Avanzar el tiempo
        self.tiempo_actual += 1
        return vehiculos_pasados
    
    def simular(self, duracion_simulacion):
        """Ejecuta la simulación por un período determinado"""
        print(f"Iniciando simulación por {duracion_simulacion} unidades de tiempo")
        
        for t in range(duracion_simulacion):
            self.tiempo_actual = t
            self.actualizar()
        
        print(f"Simulación completada en tiempo {self.tiempo_actual}")
    
    def estadisticas_globales(self):
        """Genera estadísticas globales del cruce"""
        total_vehiculos_en_cola = 0
        total_vehiculos_pasados = 0
        sum_tiempos_espera = 0
        num_vehiculos_con_espera = 0
        
        # Recopilar estadísticas de cada calle
        estadisticas_calles = {}
        for nombre, calle in self.calles.items():
            stats = calle.estadisticas()
            estadisticas_calles[nombre] = stats
            
            total_vehiculos_en_cola += stats["vehiculos_en_cola"]
            total_vehiculos_pasados += stats["vehiculos_pasados"]
            
            if stats["vehiculos_pasados"] > 0:
                sum_tiempos_espera += stats["tiempo_espera_promedio"] * stats["vehiculos_pasados"]
                num_vehiculos_con_espera += stats["vehiculos_pasados"]
        
        # Calcular promedios globales
        tiempo_espera_promedio_global = 0
        if num_vehiculos_con_espera > 0:
            tiempo_espera_promedio_global = sum_tiempos_espera / num_vehiculos_con_espera
        
        flujo_vehiculos = 0
        if self.tiempo_actual > 0:
            flujo_vehiculos = total_vehiculos_pasados / self.tiempo_actual
        
        print("\n----- ESTADÍSTICAS GLOBALES DEL CRUCE -----")
        print(f"Tiempo total de simulación: {self.tiempo_actual}")
        print(f"Total vehículos procesados: {total_vehiculos_pasados}")
        print(f"Vehículos aún en cola: {total_vehiculos_en_cola}")
        print(f"Tiempo promedio de espera: {tiempo_espera_promedio_global:.2f}")
        print(f"Flujo de vehículos: {flujo_vehiculos:.2f} vehículos/unidad de tiempo")
        
        print("\n----- ESTADÍSTICAS POR CALLE -----")
        for nombre, stats in estadisticas_calles.items():
            print(stats["mensaje"])
        
        return {
            "tiempo_simulacion": self.tiempo_actual,
            "vehiculos_procesados": total_vehiculos_pasados,
            "vehiculos_en_cola": total_vehiculos_en_cola,
            "tiempo_espera_promedio": tiempo_espera_promedio_global,
            "flujo_vehiculos": flujo_vehiculos,
            "estadisticas_calles": estadisticas_calles
        }


# Ejemplo de uso del sistema
if __name__ == "__main__":
    import random
    
    # Crear cuatro calles para un cruce típico
    calle_norte = Calle("Norte")
    calle_sur = Calle("Sur")
    calle_este = Calle("Este")
    calle_oeste = Calle("Oeste")
    
    # Crear el cruce con las calles y los tiempos de semáforo
    cruce = CruceSemaforizado([calle_norte, calle_sur, calle_este, calle_oeste], 
                              duracion_verde=20, duracion_rojo=60)
    
    # Generar vehículos aleatorios para la simulación
    for i in range(1, 101):
        # Elegir una calle aleatoria
        calle_random = random.choice(["Norte", "Sur", "Este", "Oeste"])
        
        # Tiempo aleatorio de llegada entre 0 y 100
        tiempo_llegada = random.randint(0, 100)
        
        # Tiempo de paso entre 1 y 5 unidades
        tiempo_paso = random.randint(1, 5)
        
        # Crear y agregar el vehículo
        vehiculo = Vehiculo(i, tiempo_llegada, tiempo_paso)
        cruce.agregar_vehiculo(vehiculo, calle_random)
    
    # Ejecutar la simulación por 200 unidades de tiempo
    cruce.simular(200)
    
    # Mostrar estadísticas finales
    cruce.estadisticas_globales()