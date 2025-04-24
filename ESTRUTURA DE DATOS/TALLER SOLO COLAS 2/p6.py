import time
import random
from collections import deque, defaultdict
from datetime import datetime
from queue import PriorityQueue
import statistics


class Message:
    """Clase que representa un mensaje en el sistema de chat."""
    
    def __init__(self, message_id, sender, recipient, content, message_type="text", priority=3):
        """
        Inicializa un nuevo mensaje.
        
        Args:
            message_id: Identificador único del mensaje
            sender: ID o nombre del remitente
            recipient: ID o nombre del destinatario
            content: Contenido del mensaje
            message_type: Tipo de mensaje ('text', 'image', 'video')
            priority: Prioridad del mensaje (1: Alta, 2: Media, 3: Baja)
        """
        self.message_id = message_id
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.message_type = message_type
        self.priority = priority
        
        # Tiempos de registro
        self.creation_time = time.time()  # Cuando se crea el mensaje
        self.queue_entry_time = None      # Cuando entra en la cola
        self.processing_start_time = None # Cuando comienza a procesarse
        self.delivery_time = None         # Cuando se entrega al destinatario
        
        # Tamaño simulado para mensajes no textuales
        if message_type == "image":
            self.size = random.randint(100, 2000)  # KB
        elif message_type == "video":
            self.size = random.randint(1000, 10000)  # KB
        else:
            self.size = len(content)  # Caracteres para texto
    
    def __lt__(self, other):
        """
        Comparador para ordenar mensajes por prioridad en la cola de prioridad.
        Permite que PriorityQueue ordene los mensajes.
        """
        return self.priority < other.priority
    
    def get_wait_time(self):
        """Calcula el tiempo que el mensaje estuvo en cola."""
        if self.queue_entry_time is None or self.processing_start_time is None:
            return None
        return self.processing_start_time - self.queue_entry_time
    
    def get_processing_time(self):
        """Calcula el tiempo de procesamiento del mensaje."""
        if self.processing_start_time is None or self.delivery_time is None:
            return None
        return self.delivery_time - self.processing_start_time
    
    def get_total_time(self):
        """Calcula el tiempo total desde la creación hasta la entrega."""
        if self.creation_time is None or self.delivery_time is None:
            return None
        return self.delivery_time - self.creation_time
    
    def __str__(self):
        return f"Mensaje {self.message_id} - De: {self.sender}, Para: {self.recipient}, Tipo: {self.message_type}, Prioridad: {self.priority}"


class StandardChatQueueSystem:
    """Sistema estándar de cola de mensajes para chat en tiempo real."""
    
    def __init__(self):
        self.message_queue = deque()  # Cola de mensajes pendientes
        self.processed_messages = []  # Historial de mensajes procesados
        self.message_counter = 0      # Contador para generar IDs de mensajes
        
        # Factores de simulación para tiempos de procesamiento
        self.server_load = 1.0  # Factor de carga del servidor (1.0 = normal)
        self.connection_quality = 1.0  # Factor de calidad de conexión (1.0 = buena)
    
    def create_message(self, sender, recipient, content, message_type="text"):
        """
        Crea un nuevo mensaje y lo devuelve (sin encolarlo).
        
        Returns:
            Message: El mensaje creado
        """
        self.message_counter += 1
        message = Message(self.message_counter, sender, recipient, content, message_type)
        return message
    
    def enqueue_message(self, message):
        """
        Añade un mensaje a la cola de procesamiento.
        
        Args:
            message: El mensaje a encolar
            
        Returns:
            Message: El mensaje encolado
        """
        message.queue_entry_time = time.time()
        self.message_queue.append(message)
        print(f"Mensaje encolado: {message}")
        return message
    
    def dequeue_message(self):
        """
        Extrae el siguiente mensaje de la cola para procesarlo.
        
        Returns:
            Message: El mensaje a procesar o None si la cola está vacía
        """
        if not self.message_queue:
            return None
        
        message = self.message_queue.popleft()
        message.processing_start_time = time.time()
        print(f"Procesando mensaje: {message}")
        return message
    
    def process_message(self, message):
        """
        Procesa un mensaje, simulando el tiempo de procesamiento según el tipo.
        
        Args:
            message: El mensaje a procesar
            
        Returns:
            Message: El mensaje procesado
        """
        # Simular tiempo de procesamiento según tipo de mensaje
        if message.message_type == "text":
            process_time = 0.1 * self.server_load * self.connection_quality
        elif message.message_type == "image":
            process_time = (0.2 + message.size/1000) * self.server_load * self.connection_quality
        elif message.message_type == "video":
            process_time = (0.5 + message.size/2000) * self.server_load * self.connection_quality
        else:
            process_time = 0.2 * self.server_load * self.connection_quality
        
        # Simular el procesamiento
        time.sleep(process_time)
        
        # Marcar tiempo de entrega
        message.delivery_time = time.time()
        
        # Añadir al historial
        self.processed_messages.append(message)
        
        print(f"Mensaje entregado: {message}")
        print(f"Tiempo en cola: {message.get_wait_time():.4f} segundos")
        print(f"Tiempo de procesamiento: {message.get_processing_time():.4f} segundos")
        print(f"Tiempo total: {message.get_total_time():.4f} segundos")
        
        return message
    
    def process_all_queue(self):
        """Procesa todos los mensajes pendientes en la cola."""
        print(f"\nProcesando {len(self.message_queue)} mensajes en cola...")
        while self.message_queue:
            message = self.dequeue_message()
            self.process_message(message)
    
    def get_queue_statistics(self):
        """
        Calcula estadísticas sobre los mensajes procesados.
        
        Returns:
            dict: Diccionario con estadísticas
        """
        if not self.processed_messages:
            return {"status": "No hay mensajes procesados"}
        
        wait_times = [msg.get_wait_time() for msg in self.processed_messages]
        processing_times = [msg.get_processing_time() for msg in self.processed_messages]
        total_times = [msg.get_total_time() for msg in self.processed_messages]
        
        stats = {
            "total_messages": len(self.processed_messages),
            "avg_wait_time": statistics.mean(wait_times),
            "max_wait_time": max(wait_times),
            "min_wait_time": min(wait_times),
            "avg_processing_time": statistics.mean(processing_times),
            "avg_total_time": statistics.mean(total_times)
        }
        
        return stats
    
    def print_statistics(self):
        """Muestra estadísticas sobre los mensajes procesados."""
        stats = self.get_queue_statistics()
        
        if "status" in stats:
            print(stats["status"])
            return
        
        print("\n===== ESTADÍSTICAS DEL SISTEMA DE MENSAJERÍA =====")
        print(f"Total de mensajes procesados: {stats['total_messages']}")
        print(f"Tiempo promedio en cola: {stats['avg_wait_time']:.4f} segundos")
        print(f"Tiempo máximo en cola: {stats['max_wait_time']:.4f} segundos")
        print(f"Tiempo mínimo en cola: {stats['min_wait_time']:.4f} segundos")
        print(f"Tiempo promedio de procesamiento: {stats['avg_processing_time']:.4f} segundos")
        print(f"Tiempo promedio total (envío a entrega): {stats['avg_total_time']:.4f} segundos")
        
        # Estadísticas por tipo de mensaje
        msg_types = defaultdict(list)
        for msg in self.processed_messages:
            msg_types[msg.message_type].append(msg.get_total_time())
        
        print("\nTiempo promedio por tipo de mensaje:")
        for msg_type, times in msg_types.items():
            avg_time = statistics.mean(times)
            print(f"- {msg_type}: {avg_time:.4f} segundos")


class PriorityChatQueueSystem(StandardChatQueueSystem):
    """Sistema de cola de mensajes con prioridades para chat en tiempo real."""
    
    def __init__(self):
        super().__init__()
        # Reemplazar cola estándar por cola de prioridad
        self.message_queue = PriorityQueue()
    
    def create_message(self, sender, recipient, content, message_type="text", priority=3):
        """
        Crea un nuevo mensaje con prioridad.
        
        Args:
            priority: Nivel de prioridad (1: Alta, 2: Media, 3: Baja)
            
        Returns:
            Message: El mensaje creado
        """
        self.message_counter += 1
        message = Message(
            self.message_counter, 
            sender, 
            recipient, 
            content, 
            message_type, 
            priority
        )
        return message
    
    def enqueue_message(self, message):
        """
        Añade un mensaje a la cola de prioridad.
        
        Args:
            message: El mensaje a encolar
            
        Returns:
            Message: El mensaje encolado
        """
        message.queue_entry_time = time.time()
        # En PriorityQueue, el primer elemento de la tupla determina la prioridad
        # Usamos tiempo de creación como desempate para mensajes con la misma prioridad
        self.message_queue.put((message.priority, message.creation_time, message))
        print(f"Mensaje encolado (prioridad {message.priority}): {message}")
        return message
    
    def dequeue_message(self):
        """
        Extrae el mensaje de mayor prioridad de la cola.
        
        Returns:
            Message: El mensaje a procesar o None si la cola está vacía
        """
        if self.message_queue.empty():
            return None
        
        # Extraer el mensaje (el tercer elemento de la tupla)
        _, _, message = self.message_queue.get()
        message.processing_start_time = time.time()
        print(f"Procesando mensaje (prioridad {message.priority}): {message}")
        return message
    
    def process_all_queue(self):
        """Procesa todos los mensajes pendientes en la cola de prioridad."""
        print(f"\nProcesando cola de prioridad...")
        while not self.message_queue.empty():
            message = self.dequeue_message()
            self.process_message(message)
    
    def print_statistics(self):
        """Muestra estadísticas sobre los mensajes procesados, incluyendo prioridades."""
        super().print_statistics()
        
        if not self.processed_messages:
            return
        
        # Estadísticas por nivel de prioridad
        priority_stats = defaultdict(list)
        for msg in self.processed_messages:
            priority_stats[msg.priority].append(msg.get_total_time())
        
        print("\nTiempo promedio por nivel de prioridad:")
        priority_names = {1: "Alta", 2: "Media", 3: "Baja"}
        for priority, times in sorted(priority_stats.items()):
            avg_time = statistics.mean(times)
            name = priority_names.get(priority, str(priority))
            print(f"- Prioridad {name}: {avg_time:.4f} segundos")


def demo_standard_queue():
    """Demostración del sistema estándar de cola de mensajes."""
    print("\n===== DEMOSTRACIÓN DEL SISTEMA ESTÁNDAR DE COLA DE MENSAJES =====")
    system = StandardChatQueueSystem()
    
    # Crear y encolar mensajes de diferentes tipos
    msgs = [
        system.create_message("Usuario1", "Usuario2", "Hola, ¿cómo estás?"),
        system.create_message("Usuario3", "Usuario1", "Te envío esta imagen", "image"),
        system.create_message("Usuario2", "Usuario3", "Mira este video", "video"),
        system.create_message("Usuario1", "Usuario3", "¿Viste mi mensaje?"),
        system.create_message("Usuario3", "Usuario2", "Aquí está el documento que pediste", "image")
    ]
    
    for msg in msgs:
        system.enqueue_message(msg)
    
    # Procesar todos los mensajes
    system.process_all_queue()
    
    # Mostrar estadísticas
    system.print_statistics()


def demo_priority_queue():
    """Demostración del sistema de cola de mensajes con prioridades."""
    print("\n===== DEMOSTRACIÓN DEL SISTEMA DE COLA CON PRIORIDADES =====")
    system = PriorityChatQueueSystem()
    
    # Crear y encolar mensajes con diferentes prioridades y tipos
    msgs = [
        system.create_message("Usuario1", "Usuario2", "¡URGENTE! Necesito respuesta inmediata", "text", 1),
        system.create_message("Usuario3", "Usuario1", "Te envío esta imagen", "image", 2),
        system.create_message("Usuario2", "Usuario3", "Mira este video cuando puedas", "video", 3),
        system.create_message("Usuario1", "Usuario3", "Importante: reunión en 5 minutos", "text", 1),
        system.create_message("Usuario3", "Usuario2", "Documento para revisión", "image", 2)
    ]
    
    for msg in msgs:
        system.enqueue_message(msg)
    
    # Procesar todos los mensajes
    system.process_all_queue()
    
    # Mostrar estadísticas
    system.print_statistics()


if __name__ == "__main__":
    # Ejecutar las demostraciones
    demo_standard_queue()
    demo_priority_queue()