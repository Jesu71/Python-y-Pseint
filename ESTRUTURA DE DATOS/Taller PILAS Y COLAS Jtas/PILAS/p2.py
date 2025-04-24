class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        #Agrega un elemento a la pila.
        self.items.append(item)
    
    def desapilar(self):
        #Extrae y devuelve el último elemento de la pila.
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise Exception("La pila está vacía")
    
    def esta_vacia(self):
        #Verifica si la pila está vacía.
        return len(self.items) == 0

def decimal_a_binario(decimal):
    """
    Convierte un número decimal a su representación binaria usando una pila
    
    Args:
        decimal (int): Número decimal a convertir
    
    Returns:
        str: Representación binaria del número
    """
    # Caso especial para el 0.
    if decimal == 0:
        return "0"
    
    # Crear pila para almacenar los restos.
    pila = Pila()
    
    # Número decimal temporal para las divisiones.
    numero = decimal
    
    # Realizar divisiones sucesivas por 2.
    while numero > 0:
        # Obtener el resto de la división.
        resto = numero % 2
        
        # Apilar el resto.
        pila.apilar(resto)
        
        # Realizar división entera.
        numero //= 2
    
    # Construir número binario extrayendo de la pila.
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    
    return binario

def main():
    # Pruebas con diferentes números decimales.
    numeros = [10, 42, 255, 0, 7]
    
    print("Conversión Decimal a Binario:")
    for num in numeros:
        binario = decimal_a_binario(num)
        print(f"{num} -> {binario}")

if __name__ == "__main__":
    main()