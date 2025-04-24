import time
from collections import deque
from datetime import datetime

class ChatMessageQueue:
    def __init__(self):
        # Inicializa la cola y los registros de mensajes.
        self.queue = deque()
        self.message_logs = []
    
    def enqueue_message(self, sender_id, recipient_id, content):
        # Añade un mensaje a la cola.
        timestamp = time.time()
        message = {
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'content': content,
            'timestamp': timestamp,
            'enqueued_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.queue.append(message)
        print(f"Mensaje añadido a la cola: {sender_id} -> {recipient_id}")
        return timestamp
    
    def dequeue_message(self):
        # Desencola el próximo mensaje.
        if not self.queue:
            print("La cola está vacía. No hay mensajes para procesar.")
            return None
        
        message = self.queue.popleft()
        current_time = time.time()
        wait_time = current_time - message['timestamp']
        
        # Registra el procesamiento del mensaje.
        log_entry = {
            'message_id': id(message),
            'sender_id': message['sender_id'],
            'recipient_id': message['recipient_id'],
            'enqueued_at': message['enqueued_at'],
            'dequeued_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'wait_time_seconds': wait_time
        }
        self.message_logs.append(log_entry)
        
        print(f"Mensaje procesado: {message['sender_id']} -> {message['recipient_id']}")
        print(f"Tiempo en cola: {wait_time:.2f} segundos")
        
        return message
    
    def get_queue_size(self):
        # Retorna el tamaño de la cola.
        return len(self.queue)
    
    def view_message_logs(self):
        # Retorna los registros de mensajes procesados.
        return self.message_logs

    def get_average_wait_time(self):
        # Calcula el tiempo promedio de espera.
        if not self.message_logs:
            return 0
        
        total_wait_time = sum(log['wait_time_seconds'] for log in self.message_logs)
        return total_wait_time / len(self.message_logs)


# Ejemplo de uso del sistema de cola de mensajes para chat.
if __name__ == "__main__":
    # Crear una instancia de la cola de mensajes.
    chat_queue = ChatMessageQueue()
    
    # Simular la llegada de mensajes.
    print("Simulando llegada de mensajes...")
    chat_queue.enqueue_message("usuario1", "usuario2", "Hola, ¿cómo estás?")
    time.sleep(0.5)  # Simula tiempo entre mensajes.
    
    chat_queue.enqueue_message("usuario3", "usuario1", "¿Alguien disponible para reunión?")
    time.sleep(0.3)
    
    chat_queue.enqueue_message("usuario2", "usuario1", "Recibí tu mensaje, todo bien!")
    time.sleep(0.2)
    
    # Procesar mensajes.
    print("\nProcesando mensajes de la cola:")
    while chat_queue.get_queue_size() > 0:
        message = chat_queue.dequeue_message()
        time.sleep(0.5)  # Simula tiempo de procesamiento.
    
    # Mostrar estadísticas.
    print("\nEstadísticas de mensajes procesados:")
    print(f"Total de mensajes procesados: {len(chat_queue.message_logs)}")
    print(f"Tiempo promedio en cola: {chat_queue.get_average_wait_time():.2f} segundos")
    
    # Mostrar logs detallados.
    print("\nRegistros detallados de mensajes:")
    for log in chat_queue.view_message_logs():
        print(f"Mensaje de {log['sender_id']} a {log['recipient_id']}")
        print(f"Encolado: {log['enqueued_at']} | Desencolado: {log['dequeued_at']}")
        print(f"Tiempo en cola: {log['wait_time_seconds']:.2f} segundos")
        print("-" * 40)