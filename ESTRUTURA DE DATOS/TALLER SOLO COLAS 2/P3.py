import random
class PriorityQueue:
    def __init__(self):
        self.items = []
        self.original_positions = []  # Para rastrear las posiciones originales.

    # Insertar con prioridad (números de dos dígitos tienen prioridad sobre números de tres dígitos).
    def enqueue(self, value):
        position = len(self.items)
        
        # Si la cola está vacía, simplemente insertamos.
        if self.is_empty():
            self.items.append(value)
            self.original_positions.append(position)
            return
        
        is_double_digit = 10 <= value <= 99
        
        # Encontrar la posición correcta para insertar.
        i = 0
        for i in range(len(self.items)):
            current_is_double_digit = 10 <= self.items[i] <= 99
            
            # Si el valor actual es de dos dígitos y el elemento en la cola es de tres dígitos.
            if is_double_digit and not current_is_double_digit:
                break
        
        # Insertar en la posición correcta.
        self.items.insert(i, value)
        self.original_positions.insert(i, position)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def get_items(self):
        return self.items
    
    def find_max_min_positions(self):
        if self.is_empty():
            return {"max": -1, "min": -1}
        
        max_value = self.items[0]
        min_value = self.items[0]
        max_index = 0
        min_index = 0
        
        # Encontrar los índices de los valores máximo y mínimo.
        for i in range(1, len(self.items)):
            if self.items[i] > max_value:
                max_value = self.items[i]
                max_index = i
            if self.items[i] < min_value:
                min_value = self.items[i]
                min_index = i
        
        # Devolver las posiciones originales.
        return {
            "max": self.original_positions[max_index],
            "min": self.original_positions[min_index],
            "max_value": max_value,
            "min_value": min_value
        }

# Función para generar un número aleatorio entre min y max (inclusive).
def get_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Programa principal.
def main():
    queue = PriorityQueue()
    generated_numbers = []
    
    print("Generando 50 números aleatorios entre 1 y 250...")
    
    # Generar 50 números aleatorios e insertarlos en la cola.
    for i in range(50):
        random_num = get_random_number(1, 250)
        generated_numbers.append(random_num)
        queue.enqueue(random_num)
    
    print("Números generados en orden de generación:")
    print(generated_numbers)
    
    print("\nCola después de insertar todos los números (con prioridad para números de dos dígitos):")
    print(queue.get_items())
    
    # Encontrar las posiciones del máximo y mínimo.
    result = queue.find_max_min_positions()
    
    print(f"\nEl número con mayor valor ({result['max_value']}) se encuentra en la posición: {result['max']}")
    print(f"El número con menor valor ({result['min_value']}) se encuentra en la posición: {result['min']}")

if __name__ == "__main__":
    main()