import time
import random
from collections import deque
import heapq

class Document:
    """Clase que representa un documento para imprimir"""
    def __init__(self, doc_id, name, pages):
        self.id = doc_id
        self.name = name
        self.pages = pages  # Número de páginas (determina el tiempo de impresión)
        self.arrival_time = time.time()  # Momento en que se envía a la cola
        self.start_print_time = None  # Momento en que comienza a imprimirse
        self.finish_time = None  # Momento en que termina de imprimirse
    
    def get_print_time(self):
        """Retorna el tiempo estimado de impresión (1 segundo por página)"""
        return self.pages
    
    def get_waiting_time(self):
        """Calcula el tiempo de espera antes de comenzar a imprimir"""
        if self.start_print_time is None:
            return None
        return self.start_print_time - self.arrival_time
    
    def get_total_time(self):
        """Calcula el tiempo total desde la llegada hasta la finalización"""
        if self.finish_time is None:
            return None
        return self.finish_time - self.arrival_time


class SinglePrinterSystem:
    """Sistema de impresión con una sola impresora"""
    def __init__(self):
        self.queue = deque()  # Cola de documentos
        self.current_document = None  # Documento actualmente en impresión
        self.completed_documents = []  # Documentos ya impresos
        self.current_time = 0  # Tiempo simulado actual
        self.doc_counter = 0  # Contador para IDs de documentos
    
    def add_document(self, name, pages):
        """Añade un nuevo documento a la cola de impresión"""
        doc_id = self.doc_counter
        self.doc_counter += 1
        
        document = Document(doc_id, name, pages)
        document.arrival_time = self.current_time  # Usar tiempo simulado
        
        self.queue.append(document)
        print(f"[Tiempo: {self.current_time}s] Documento #{doc_id} '{name}' ({pages} páginas) añadido a la cola")
        return doc_id
    
    def start_next_document(self):
        """Comienza a imprimir el siguiente documento en la cola"""
        if not self.queue or self.current_document:
            return False
        
        self.current_document = self.queue.popleft()
        self.current_document.start_print_time = self.current_time
        
        waiting_time = self.current_document.get_waiting_time()
        print(f"[Tiempo: {self.current_time}s] Comenzando a imprimir documento #{self.current_document.id} '{self.current_document.name}'")
        print(f"  - Tiempo de espera: {waiting_time:.1f}s")
        
        return True
    
    def update(self, elapsed_seconds):
        """Actualiza el estado del sistema después de que pasa un tiempo determinado"""
        self.current_time += elapsed_seconds
        
        # Si hay un documento imprimiéndose, actualizar su progreso
        if self.current_document:
            remaining_time = self.current_document.get_print_time() - (self.current_time - self.current_document.start_print_time)
            
            # Si el documento ha terminado de imprimirse
            if remaining_time <= 0:
                self.current_document.finish_time = self.current_time
                
                waiting_time = self.current_document.get_waiting_time()
                print_time = self.current_document.get_print_time()
                total_time = self.current_document.get_total_time()
                
                print(f"[Tiempo: {self.current_time}s] Documento #{self.current_document.id} '{self.current_document.name}' completado")
                print(f"  - Tiempo de espera: {waiting_time:.1f}s")
                print(f"  - Tiempo de impresión: {print_time}s")
                print(f"  - Tiempo total: {total_time:.1f}s")
                
                self.completed_documents.append(self.current_document)
                self.current_document = None
                
                # Intentar imprimir el siguiente documento
                self.start_next_document()
        
        # Si no hay documento imprimiéndose, intentar comenzar uno
        elif not self.current_document:
            self.start_next_document()
    
    def get_statistics(self):
        """Calcula y muestra estadísticas sobre los documentos procesados"""
        if not self.completed_documents:
            print("No hay documentos completados para mostrar estadísticas")
            return
        
        total_docs = len(self.completed_documents)
        total_pages = sum(doc.pages for doc in self.completed_documents)
        total_waiting_time = sum(doc.get_waiting_time() for doc in self.completed_documents)
        avg_waiting_time = total_waiting_time / total_docs
        
        print("\n=== ESTADÍSTICAS DEL SISTEMA DE IMPRESIÓN ===")
        print(f"Total de documentos procesados: {total_docs}")
        print(f"Total de páginas impresas: {total_pages}")
        print(f"Tiempo promedio de espera: {avg_waiting_time:.2f}s")
        print(f"Tiempo total de operación: {self.current_time:.1f}s")
        
        # Documento con mayor tiempo de espera
        max_wait_doc = max(self.completed_documents, key=lambda x: x.get_waiting_time())
        print(f"Documento con mayor tiempo de espera: #{max_wait_doc.id} '{max_wait_doc.name}' ({max_wait_doc.get_waiting_time():.1f}s)")


class MultiPrinterSystem:
    """Sistema de impresión con múltiples impresoras"""
    def __init__(self, num_printers, strategy="equitable"):
        self.num_printers = num_printers
        self.strategy = strategy  # "equitable" o "least_wait"
        self.printers = [{"id": i, "document": None, "finish_time": 0} for i in range(num_printers)]
        self.queue = deque()  # Cola de documentos
        self.completed_documents = []  # Documentos ya impresos
        self.current_time = 0  # Tiempo simulado actual
        self.doc_counter = 0  # Contador para IDs de documentos
    
    def add_document(self, name, pages):
        """Añade un nuevo documento a la cola de impresión"""
        doc_id = self.doc_counter
        self.doc_counter += 1
        
        document = Document(doc_id, name, pages)
        document.arrival_time = self.current_time  # Usar tiempo simulado
        
        self.queue.append(document)
        print(f"[Tiempo: {self.current_time}s] Documento #{doc_id} '{name}' ({pages} páginas) añadido a la cola")
        return doc_id
    
    def assign_to_printer(self):
        """Asigna documentos a impresoras disponibles según la estrategia elegida"""
        if not self.queue:
            return False
        
        available_printers = [p for p in self.printers if p["document"] is None]
        if not available_printers:
            return False
        
        if self.strategy == "equitable":
            # Estrategia equitativa: asignar al primer printer disponible
            printer = available_printers[0]
            document = self.queue.popleft()
            
            printer["document"] = document
            document.start_print_time = self.current_time
            printer["finish_time"] = self.current_time + document.get_print_time()
            
            waiting_time = document.get_waiting_time()
            print(f"[Tiempo: {self.current_time}s] Impresora #{printer['id']} comienza a imprimir documento #{document.id} '{document.name}'")
            print(f"  - Tiempo de espera: {waiting_time:.1f}s")
            
            return True
            
        elif self.strategy == "least_wait":
            # Estrategia de menor tiempo de espera: asignar a la impresora que terminará antes
            document = self.queue.popleft()
            
            # Encontrar la impresora que terminará antes
            printer = min(self.printers, key=lambda p: p["finish_time"] if p["document"] is None else float('inf'))
            
            # Si todas las impresoras están ocupadas, usar la que terminará primero
            if printer["document"] is not None:
                printer = min(self.printers, key=lambda p: p["finish_time"])
                
                # Actualizar el tiempo actual al momento en que la impresora estará disponible
                time_jump = printer["finish_time"] - self.current_time
                if time_jump > 0:
                    self.update(time_jump)
                    return self.assign_to_printer()  # Intentar asignar nuevamente
            
            printer["document"] = document
            document.start_print_time = self.current_time
            printer["finish_time"] = self.current_time + document.get_print_time()
            
            waiting_time = document.get_waiting_time()
            print(f"[Tiempo: {self.current_time}s] Impresora #{printer['id']} comienza a imprimir documento #{document.id} '{document.name}'")
            print(f"  - Tiempo de espera: {waiting_time:.1f}s")
            
            return True
    
    def update(self, elapsed_seconds):
        """Actualiza el estado del sistema después de que pasa un tiempo determinado"""
        self.current_time += elapsed_seconds
        
        # Verificar impresoras que han terminado
        for printer in self.printers:
            if printer["document"] and self.current_time >= printer["finish_time"]:
                document = printer["document"]
                document.finish_time = self.current_time
                
                waiting_time = document.get_waiting_time()
                print_time = document.get_print_time()
                total_time = document.get_total_time()
                
                print(f"[Tiempo: {self.current_time}s] Impresora #{printer['id']} completó documento #{document.id} '{document.name}'")
                print(f"  - Tiempo de espera: {waiting_time:.1f}s")
                print(f"  - Tiempo de impresión: {print_time}s")
                print(f"  - Tiempo total: {total_time:.1f}s")
                
                self.completed_documents.append(document)
                printer["document"] = None
                
                # Intentar asignar un nuevo documento a esta impresora
                self.assign_to_printer()
        
        # Intentar asignar documentos a impresoras disponibles
        while self.assign_to_printer():
            pass
    
    def get_statistics(self):
        """Calcula y muestra estadísticas sobre los documentos procesados"""
        if not self.completed_documents:
            print("No hay documentos completados para mostrar estadísticas")
            return
        
        total_docs = len(self.completed_documents)
        total_pages = sum(doc.pages for doc in self.completed_documents)
        total_waiting_time = sum(doc.get_waiting_time() for doc in self.completed_documents)
        avg_waiting_time = total_waiting_time / total_docs
        
        print(f"\n=== ESTADÍSTICAS DEL SISTEMA DE IMPRESIÓN ({self.num_printers} IMPRESORAS) ===")
        print(f"Estrategia: {'Equitativa' if self.strategy == 'equitable' else 'Menor tiempo de espera'}")
        print(f"Total de documentos procesados: {total_docs}")
        print(f"Total de páginas impresas: {total_pages}")
        print(f"Tiempo promedio de espera: {avg_waiting_time:.2f}s")
        print(f"Tiempo total de operación: {self.current_time:.1f}s")
        
        # Documento con mayor tiempo de espera
        max_wait_doc = max(self.completed_documents, key=lambda x: x.get_waiting_time())
        print(f"Documento con mayor tiempo de espera: #{max_wait_doc.id} '{max_wait_doc.name}' ({max_wait_doc.get_waiting_time():.1f}s)")


def simulate_single_printer():
    """Simula un sistema de impresión con una sola impresora"""
    print("=== SIMULACIÓN DE SISTEMA DE IMPRESIÓN CON UNA IMPRESORA ===")
    
    system = SinglePrinterSystem()
    
    # Documentos de ejemplo
    documents = [
        {"name": "Informe Mensual", "pages": 15},
        {"name": "Contrato", "pages": 5},
        {"name": "Presentación", "pages": 20},
        {"name": "Factura", "pages": 2},
        {"name": "Manual", "pages": 30},
        {"name": "Carta", "pages": 1},
        {"name": "Reporte Anual", "pages": 45},
        {"name": "Memo", "pages": 3}
    ]
    
    # Añadir documentos iniciales
    for doc in documents[:4]:  # Primeros 4 documentos
        system.add_document(doc["name"], doc["pages"])
    
    # Simular el paso del tiempo
    for i in range(1, 61):  # Simular 60 segundos
        # Cada 15 segundos, añadir un nuevo documento (si quedan)
        if i % 15 == 0 and len(documents) > 4 + (i // 15):
            doc = documents[4 + (i // 15) - 1]
            system.add_document(doc["name"], doc["pages"])
        
        system.update(1)  # Avanzar 1 segundo
    
    # Procesar los documentos restantes
    while system.queue or system.current_document:
        system.update(1)
    
    # Mostrar estadísticas
    system.get_statistics()


def simulate_multi_printer(num_printers=3, strategy="equitable"):
    """Simula un sistema de impresión con múltiples impresoras"""
    print(f"\n=== SIMULACIÓN DE SISTEMA DE IMPRESIÓN CON {num_printers} IMPRESORAS ===")
    print(f"Estrategia: {'Equitativa' if strategy == 'equitable' else 'Menor tiempo de espera'}")
    
    system = MultiPrinterSystem(num_printers, strategy)
    
    # Documentos de ejemplo (los mismos que en la simulación anterior)
    documents = [
        {"name": "Informe Mensual", "pages": 15},
        {"name": "Contrato", "pages": 5},
        {"name": "Presentación", "pages": 20},
        {"name": "Factura", "pages": 2},
        {"name": "Manual", "pages": 30},
        {"name": "Carta", "pages": 1},
        {"name": "Reporte Anual", "pages": 45},
        {"name": "Memo", "pages": 3}
    ]
    
    # Añadir documentos iniciales
    for doc in documents[:4]:  # Primeros 4 documentos
        system.add_document(doc["name"], doc["pages"])
    
    # Simular el paso del tiempo
    for i in range(1, 61):  # Simular 60 segundos
        # Cada 15 segundos, añadir un nuevo documento (si quedan)
        if i % 15 == 0 and len(documents) > 4 + (i // 15):
            doc = documents[4 + (i // 15) - 1]
            system.add_document(doc["name"], doc["pages"])
        
        system.update(1)  # Avanzar 1 segundo
    
    # Procesar los documentos restantes
    while system.queue or any(p["document"] is not None for p in system.printers):
        system.update(1)
    
    # Mostrar estadísticas
    system.get_statistics()


if __name__ == "__main__":
    # Simular sistema con una impresora
    simulate_single_printer()
    
    # Simular sistema con múltiples impresoras (estrategia equitativa)
    simulate_multi_printer(3, "equitable")
    
    # Simular sistema con múltiples impresoras (estrategia de menor tiempo de espera)
    simulate_multi_printer(3, "least_wait")