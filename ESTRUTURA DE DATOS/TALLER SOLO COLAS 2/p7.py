import time
import random
import heapq
from collections import defaultdict, deque
from datetime import datetime, timedelta
import statistics

class Paciente:
    """Clase para representar a un paciente en la sala de emergencias."""
    # Contador para asignar ID único a cada paciente y mantener el orden FIFO dentro de la misma prioridad
    contador_id = 0
    
    # Mapeo de niveles de gravedad a prioridad numérica (menor número = mayor prioridad)
    NIVELES_GRAVEDAD = {
        "crítico": 0,
        "severo": 1,
        "moderado": 2,
        "leve": 3
    }
    
    def __init__(self, nombre, gravedad, descripcion=""):
        """
        Inicializa un paciente.
        
        Args:
            nombre: Nombre del paciente
            gravedad: Nivel de gravedad ("crítico", "severo", "moderado", "leve")
            descripcion: Descripción breve del problema médico
        """
        Paciente.contador_id += 1
        self.id = Paciente.contador_id
        self.nombre = nombre
        self.gravedad = gravedad
        self.descripcion = descripcion
        self.hora_llegada = datetime.now()
        self.hora_atencion = None
        self.tiempo_espera = None
        self.doctor_asignado = None
        
        # Validar nivel de gravedad
        if gravedad not in self.NIVELES_GRAVEDAD:
            raise ValueError(f"Nivel de gravedad inválido: {gravedad}")
        
        # Prioridad numérica para la cola de prioridad
        self.prioridad_numerica = self.NIVELES_GRAVEDAD[gravedad]
    
    def calcular_tiempo_espera(self):
        """Calcula el tiempo de espera entre llegada y atención."""
        if self.hora_atencion:
            self.tiempo_espera = (self.hora_atencion - self.hora_llegada).total_seconds() / 60  # en minutos
            return self.tiempo_espera
        return None
    
    def __lt__(self, otro):
        """
        Comparador para ordenar pacientes en la cola de prioridad.
        Si tienen la misma prioridad, se compara por ID (orden de llegada).
        """
        if self.prioridad_numerica == otro.prioridad_numerica:
            return self.id < otro.id
        return self.prioridad_numerica < otro.prioridad_numerica
    
    def __str__(self):
        return f"Paciente #{self.id}: {self.nombre} - {self.gravedad.upper()}"


class Doctor:
    """Clase para representar a un doctor en el hospital."""
    
    def __init__(self, id, nombre, especialidad, eficiencia=1.0):
        """
        Inicializa un doctor.
        
        Args:
            id: Identificador único del doctor
            nombre: Nombre del doctor
            especialidad: Especialidad médica
            eficiencia: Factor de eficiencia que afecta la velocidad de atención (>1 más rápido, <1 más lento)
        """
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.eficiencia = eficiencia
        self.paciente_actual = None
        self.disponible = True
        self.pacientes_atendidos = 0
        self.tiempo_total_atencion = 0  # en minutos
    
    def atender_paciente(self, paciente):
        """
        Asigna un paciente al doctor para ser atendido.
        
        Args:
            paciente: Objeto Paciente a atender
        """
        self.paciente_actual = paciente
        self.disponible = False
        paciente.doctor_asignado = self
        paciente.hora_atencion = datetime.now()
        
        # Calcular tiempo de espera del paciente
        paciente.calcular_tiempo_espera()
        
        return paciente
    
    def finalizar_atencion(self, tiempo_atencion):
        """
        Finaliza la atención del paciente actual.
        
        Args:
            tiempo_atencion: Tiempo que tomó atender al paciente en minutos
        """
        if self.paciente_actual:
            self.pacientes_atendidos += 1
            self.tiempo_total_atencion += tiempo_atencion
            paciente_atendido = self.paciente_actual
            self.paciente_actual = None
            self.disponible = True
            return paciente_atendido
        return None
    
    def tiempo_promedio_atencion(self):
        """Calcula el tiempo promedio de atención por paciente."""
        if self.pacientes_atendidos == 0:
            return 0
        return self.tiempo_total_atencion / self.pacientes_atendidos
    
    def __str__(self):
        estado = "DISPONIBLE" if self.disponible else f"Atendiendo a {self.paciente_actual.nombre}"
        return f"Dr. {self.nombre} ({self.especialidad}) - {estado}"


class Turno:
    """Clase para representar un turno de trabajo en el hospital."""
    
    def __init__(self, nombre, hora_inicio, hora_fin, doctores):
        """
        Inicializa un turno de trabajo.
        
        Args:
            nombre: Nombre del turno (ej: "Mañana", "Tarde", "Noche")
            hora_inicio: Hora de inicio del turno (formato 24h, ej: 8 para 8:00 AM)
            hora_fin: Hora de fin del turno (formato 24h, ej: 16 para 4:00 PM)
            doctores: Lista de doctores asignados al turno
        """
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.doctores = doctores
    
    def esta_activo(self, hora_actual=None):
        """
        Verifica si el turno está activo en la hora especificada.
        
        Args:
            hora_actual: Hora a verificar (por defecto, la hora actual)
            
        Returns:
            bool: True si el turno está activo, False en caso contrario
        """
        if hora_actual is None:
            hora_actual = datetime.now().hour
            
        # Manejar turnos que cruzan la medianoche
        if self.hora_inicio < self.hora_fin:
            return self.hora_inicio <= hora_actual < self.hora_fin
        else:  # Por ejemplo, turno de 22:00 a 6:00
            return hora_actual >= self.hora_inicio or hora_actual < self.hora_fin
    
    def get_doctores_disponibles(self):
        """Retorna la lista de doctores disponibles en el turno actual."""
        return [doctor for doctor in self.doctores if doctor.disponible]
    
    def __str__(self):
        return f"Turno {self.nombre} ({self.hora_inicio}:00 - {self.hora_fin}:00) - {len(self.doctores)} doctores"


class SalaEmergencias:
    """Sistema de gestión de la sala de emergencias de un hospital."""
    
    def __init__(self):
        self.cola_pacientes = []  # Cola de prioridad (heapq)
        self.pacientes_atendidos = []
        self.turnos = []  # Lista de turnos configurados
        self.turno_actual = None
        self.tiempo_simulacion = 0  # Tiempo simulado en minutos
        
        # Factor de velocidad de simulación (minutos simulados por segundo real)
        self.velocidad_simulacion = 10
        
        # Tasas de llegada de pacientes por nivel de gravedad (pacientes por hora)
        self.tasas_llegada = {
            "crítico": 0.5,   # 1 cada 2 horas en promedio
            "severo": 2,      # 2 por hora en promedio
            "moderado": 5,    # 5 por hora en promedio
            "leve": 8         # 8 por hora en promedio
        }
        
        # Tiempo promedio de atención por nivel de gravedad (en minutos)
        self.tiempos_atencion = {
            "crítico": 120,   # 2 horas en promedio
            "severo": 60,     # 1 hora en promedio
            "moderado": 30,   # 30 minutos en promedio
            "leve": 15        # 15 minutos en promedio
        }
    
    def configurar_turnos(self, turnos):
        """
        Configura los turnos del hospital.
        
        Args:
            turnos: Lista de objetos Turno
        """
        self.turnos = turnos
        self.actualizar_turno_actual()
    
    def actualizar_turno_actual(self, hora=None):
        """
        Actualiza el turno actual según la hora especificada.
        
        Args:
            hora: Hora a verificar (por defecto, la hora actual)
        """
        if not self.turnos:
            return None
        
        for turno in self.turnos:
            if turno.esta_activo(hora):
                self.turno_actual = turno
                return turno
        
        return None
    
    def registrar_paciente(self, paciente):
        """
        Registra un nuevo paciente en la sala de emergencias.
        
        Args:
            paciente: Objeto Paciente a registrar
        """
        # Agregar paciente a la cola de prioridad
        heapq.heappush(self.cola_pacientes, paciente)
        print(f"[{self._formato_tiempo()}] Registrado: {paciente}")
        return paciente
    
    def atender_siguiente_paciente(self):
        """
        Atiende al siguiente paciente de mayor prioridad si hay doctores disponibles.
        
        Returns:
            tuple: (paciente atendido, doctor asignado) o (None, None) si no se puede atender
        """
        if not self.cola_pacientes:
            print(f"[{self._formato_tiempo()}] No hay pacientes en espera.")
            return None, None
        
        if not self.turno_actual:
            print(f"[{self._formato_tiempo()}] No hay turno activo en este momento.")
            return None, None
        
        doctores_disponibles = self.turno_actual.get_doctores_disponibles()
        if not doctores_disponibles:
            print(f"[{self._formato_tiempo()}] No hay doctores disponibles en este momento.")
            return None, None
        
        # Obtener paciente de mayor prioridad
        paciente = heapq.heappop(self.cola_pacientes)
        
        # Asignar doctor (podría mejorar con lógica de asignación más compleja)
        doctor = doctores_disponibles[0]
        
        # Atender paciente
        doctor.atender_paciente(paciente)
        print(f"[{self._formato_tiempo()}] {paciente} está siendo atendido por {doctor.nombre}")
        
        # Calcular tiempo de atención basado en la gravedad y eficiencia del doctor
        tiempo_atencion = self.tiempos_atencion[paciente.gravedad] / doctor.eficiencia
        
        # Registrar la atención
        self.pacientes_atendidos.append({
            'paciente': paciente,
            'doctor': doctor,
            'tiempo_atencion': tiempo_atencion,
            'tiempo_espera': paciente.tiempo_espera
        })
        
        return paciente, doctor
    
    def finalizar_atencion(self, doctor, tiempo_atencion):
        """
        Finaliza la atención de un paciente.
        
        Args:
            doctor: Doctor que finaliza la atención
            tiempo_atencion: Tiempo que tomó la atención en minutos
        """
        paciente = doctor.finalizar_atencion(tiempo_atencion)
        if paciente:
            print(f"[{self._formato_tiempo()}] {doctor.nombre} ha finalizado la atención de {paciente.nombre}")
        return paciente
    
    def generar_emergencia_critica(self):
        """
        Simula la llegada de una emergencia crítica que requiere atención inmediata.
        
        Returns:
            Paciente: El paciente crítico generado
        """
        nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Sofía"]
        situaciones = ["Paro cardíaco", "Accidente grave", "Herida por arma", "Asfixia", "Shock anafiláctico"]
        
        nombre = random.choice(nombres)
        situacion = random.choice(situaciones)
        
        paciente = Paciente(nombre, "crítico", situacion)
        print(f"[{self._formato_tiempo()}] ¡EMERGENCIA CRÍTICA! Llegó {paciente} - {situacion}")
        
        self.registrar_paciente(paciente)
        return paciente
    
    def calcular_estadisticas(self):
        """
        Calcula estadísticas sobre los tiempos de espera y atención.
        
        Returns:
            dict: Diccionario con estadísticas
        """
        if not self.pacientes_atendidos:
            return {"mensaje": "No hay pacientes atendidos para calcular estadísticas"}
        
        # Agrupar por nivel de gravedad
        por_gravedad = defaultdict(list)
        tiempos_espera = []
        
        for registro in self.pacientes_atendidos:
            paciente = registro['paciente']
            gravedad = paciente.gravedad
            tiempo_espera = registro['tiempo_espera']
            
            por_gravedad[gravedad].append(tiempo_espera)
            tiempos_espera.append(tiempo_espera)
        
        # Calcular promedios por gravedad
        promedios = {}
        for gravedad, tiempos in por_gravedad.items():
            promedios[gravedad] = statistics.mean(tiempos)
        
        # Estadísticas generales
        stats = {
            "total_pacientes": len(self.pacientes_atendidos),
            "tiempo_espera_promedio": statistics.mean(tiempos_espera),
            "tiempo_espera_maximo": max(tiempos_espera),
            "tiempo_espera_minimo": min(tiempos_espera),
            "promedios_por_gravedad": promedios,
            "pacientes_en_espera": len(self.cola_pacientes)
        }
        
        return stats
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas de la sala de emergencias."""
        stats = self.calcular_estadisticas()
        
        if "mensaje" in stats:
            print(stats["mensaje"])
            return
        
        print("\n===== ESTADÍSTICAS DE LA SALA DE EMERGENCIAS =====")
        print(f"Total de pacientes atendidos: {stats['total_pacientes']}")
        print(f"Pacientes aún en espera: {stats['pacientes_en_espera']}")
        print(f"Tiempo promedio de espera: {stats['tiempo_espera_promedio']:.2f} minutos")
        print(f"Tiempo máximo de espera: {stats['tiempo_espera_maximo']:.2f} minutos")
        print(f"Tiempo mínimo de espera: {stats['tiempo_espera_minimo']:.2f} minutos")
        
        print("\nTiempo promedio de espera por nivel de gravedad:")
        for gravedad, promedio in stats['promedios_por_gravedad'].items():
            print(f"- {gravedad.capitalize()}: {promedio:.2f} minutos")
        
        print("\nEstadísticas por doctor:")
        doctores = set()
        for turno in self.turnos:
            for doctor in turno.doctores:
                doctores.add(doctor)
        
        for doctor in doctores:
            print(f"- Dr. {doctor.nombre}: {doctor.pacientes_atendidos} pacientes, "
                  f"tiempo promedio de atención: {doctor.tiempo_promedio_atencion():.2f} minutos")
    
    def _formato_tiempo(self):
        """Formatea el tiempo actual de simulación."""
        horas = int(self.tiempo_simulacion / 60)
        minutos = int(self.tiempo_simulacion % 60)
        return f"{horas:02d}:{minutos:02d}"


class SimuladorHospital:
    """Clase para simular el funcionamiento de la sala de emergencias."""
    
    def __init__(self, sala_emergencias):
        self.sala = sala_emergencias
        self.doctores_ocupados = {}  # doctor -> tiempo restante de atención
    
    def setup_inicial(self):
        """Configura los doctores y turnos iniciales."""
        # Crear doctores
        doctores_mañana = [
            Doctor(1, "García", "Medicina General", 1.2),
            Doctor(2, "Rodríguez", "Traumatología", 1.1),
            Doctor(3, "Fernández", "Cardiología", 1.3)
        ]
        
        doctores_tarde = [
            Doctor(4, "López", "Medicina General", 1.0),
            Doctor(5, "Martínez", "Pediatría", 1.1),
            Doctor(6, "Sánchez", "Neurología", 1.2)
        ]
        
        doctores_noche = [
            Doctor(7, "González", "Medicina General", 0.9),
            Doctor(8, "Pérez", "Cirugía", 1.0)
        ]
        
        # Crear turnos
        turnos = [
            Turno("Mañana", 8, 16, doctores_mañana),
            Turno("Tarde", 16, 24, doctores_tarde),
            Turno("Noche", 0, 8, doctores_noche)
        ]
        
        # Configurar turnos en la sala de emergencias
        self.sala.configurar_turnos(turnos)
    
    def generar_paciente_aleatorio(self):
        """
        Genera un paciente con características aleatorias.
        
        Returns:
            Paciente: Un nuevo paciente con datos aleatorios
        """
        nombres = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Sofía", "Miguel", 
                   "Elena", "David", "Lucía", "José", "Carmen", "Luis", "Isabel"]
        
        apellidos = ["García", "Rodríguez", "López", "Martínez", "González", "Pérez", 
                     "Sánchez", "Fernández", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández"]
        
        problemas_leves = ["Dolor de cabeza", "Resfriado", "Dolor muscular", "Corte leve", "Alergia leve"]
        problemas_moderados = ["Fiebre alta", "Esguince", "Infección", "Deshidratación", "Migraña severa"]
        problemas_severos = ["Fractura", "Conmoción cerebral", "Hemorragia", "Apendicitis", "Crisis asmática"]
        problemas_criticos = ["Infarto", "Accidente cerebrovascular", "Trauma mayor", "Shock", "Insuficiencia respiratoria"]
        
        # Determinar aleatoriamente la gravedad basado en la distribución típica
        rand = random.random()
        if rand < 0.05:  # 5% de probabilidad
            gravedad = "crítico"
            problemas = problemas_criticos
        elif rand < 0.20:  # 15% de probabilidad
            gravedad = "severo"
            problemas = problemas_severos
        elif rand < 0.50:  # 30% de probabilidad
            gravedad = "moderado"
            problemas = problemas_moderados
        else:  # 50% de probabilidad
            gravedad = "leve"
            problemas = problemas_leves
        
        nombre = random.choice(nombres) + " " + random.choice(apellidos)
        problema = random.choice(problemas)
        
        return Paciente(nombre, gravedad, problema)
    
    def simular_tiempo(self, duracion_minutos):
        """
        Simula el funcionamiento del hospital durante un período de tiempo.
        
        Args:
            duracion_minutos: Duración de la simulación en minutos
        """
        print(f"\nIniciando simulación por {duracion_minutos} minutos...")
        
        # Configurar tiempo de inicio
        hora_inicio = self.sala.tiempo_simulacion
        hora_fin = hora_inicio + duracion_minutos
        
        while self.sala.tiempo_simulacion < hora_fin:
            # Actualizar turno actual basado en la hora
            hora_actual = (int(hora_inicio / 60) + int(self.sala.tiempo_simulacion / 60)) % 24
            self.sala.actualizar_turno_actual(hora_actual)
            
            # Generar pacientes aleatoriamente según las tasas de llegada
            for gravedad, tasa_hora in self.sala.tasas_llegada.items():
                # Convertir tasa por hora a probabilidad por minuto
                prob_minuto = tasa_hora / 60
                if random.random() < prob_minuto:
                    paciente = self.generar_paciente_aleatorio()
                    # Forzar el nivel de gravedad
                    paciente.gravedad = gravedad
                    paciente.prioridad_numerica = Paciente.NIVELES_GRAVEDAD[gravedad]
                    self.sala.registrar_paciente(paciente)
            
            # Simular emergencias críticas (baja probabilidad)
            if random.random() < 0.001:  # 0.1% de probabilidad por minuto
                self.sala.generar_emergencia_critica()
            
            # Atender pacientes si hay doctores disponibles
            if self.sala.turno_actual:
                for doctor in self.sala.turno_actual.doctores:
                    if doctor.disponible and self.sala.cola_pacientes:
                        paciente, _ = self.sala.atender_siguiente_paciente()
                        if paciente:
                            # Calcular tiempo de atención
                            tiempo_atencion = self.sala.tiempos_atencion[paciente.gravedad] / doctor.eficiencia
                            # Registrar cuándo terminará
                            self.doctores_ocupados[doctor] = tiempo_atencion
            
            # Actualizar doctores ocupados y finalizar atenciones completadas
            doctores_completados = []
            for doctor, tiempo_restante in self.doctores_ocupados.items():
                nuevo_tiempo = tiempo_restante - 1  # Reducir 1 minuto
                if nuevo_tiempo <= 0:
                    self.sala.finalizar_atencion(doctor, self.sala.tiempos_atencion[doctor.paciente_actual.gravedad])
                    doctores_completados.append(doctor)
                else:
                    self.doctores_ocupados[doctor] = nuevo_tiempo
            
            # Eliminar doctores que han completado la atención
            for doctor in doctores_completados:
                del self.doctores_ocupados[doctor]
            
            # Avanzar tiempo de simulación
            self.sala.tiempo_simulacion += 1
            
            # Si se quiere visualizar en tiempo real, añadir pequeña espera
            # time.sleep(1 / self.sala.velocidad_simulacion)
        
        print(f"\nSimulación completada. Tiempo total: {self.sala.tiempo_simulacion} minutos")
    
    def ejecutar_simulacion_completa(self, duracion_horas=24):
        """
        Ejecuta una simulación completa del hospital.
        
        Args:
            duracion_horas: Duración de la simulación en horas
        """
        # Configuración inicial
        self.setup_inicial()
        
        # Convertir horas a minutos
        duracion_minutos = duracion_horas * 60
        
        # Ejecutar simulación
        self.simular_tiempo(duracion_minutos)
        
        # Mostrar estadísticas finales
        self.sala.mostrar_estadisticas()


# Ejecutar una simulación completa si se ejecuta el script directamente
if __name__ == "__main__":
    # Crear sala de emergencias
    sala = SalaEmergencias()
    
    # Crear y configurar simulador
    simulador = SimuladorHospital(sala)
    
    # Ejecutar simulación de 24 horas
    simulador.ejecutar_simulacion_completa(24)