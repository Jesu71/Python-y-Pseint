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
    
    def ver_tope(self):
        #Muestra el elemento en la cima de la pila sin extraerlo.
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise Exception("La pila está vacía")

def verificar_balance(secuencia):
    """
    Verifica si la secuencia de llaves, paréntesis y corchetes está balanceada
    
    Args:
        secuencia (str): Cadena de caracteres a verificar
    
    Returns:
        bool: True si está balanceada, False en caso contrario
    """
    # Pila para almacenar los caracteres de apertura.
    pila = Pila()
    
    # Diccionario de mapeo de caracteres de cierre a apertura.
    mapeo_cierre = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Conjunto de caracteres de apertura.
    caracteres_apertura = set(mapeo_cierre.values())
    
    # Conjunto de caracteres de cierre.
    caracteres_cierre = set(mapeo_cierre.keys())
    
    # Recorrer cada caracter de la secuencia.
    for caracter in secuencia:
        # Si es un caracter de apertura, apilar.
        if caracter in caracteres_apertura:
            pila.apilar(caracter)
        
        # Si es un caracter de cierre
        elif caracter in caracteres_cierre:
            # Verificar si la pila está vacía (cierre sin apertura).
            if pila.esta_vacia():
                return False
            
            # Verificar si el último caracter de apertura coincide.
            if pila.ver_tope() == mapeo_cierre[caracter]:
                pila.desapilar()
            else:
                return False
    
    # La secuencia está balanceada si la pila queda vacía.
    return pila.esta_vacia()

def main():
    # Casos de prueba
    casos_prueba = [
        "({[]})",       # Balanceado perfecto
        "([)]",         # No balanceado (orden incorrecto)
        "{[()]}",       # Balanceado anidado
        "((()))",       # Balanceado simple
        "({[}])",       # No balanceado
        "",             # Cadena vacía (considerada balanceada)
        "(((",          # No balanceado (sin cierre)
        ")))",          # No balanceado (sin apertura)
        "({)}",         # No balanceado
        "[]{()}([])"    # Balanceado complejo
    ]
    
    print("Verificación de Balance de Llaves, Paréntesis y Corchetes:")
    
    # Probar cada caso.
    for secuencia in casos_prueba:
        resultado = verificar_balance(secuencia)
        print(f"Secuencia: {secuencia}")
        print(f"Balanceada: {resultado}\n")

if __name__ == "__main__":
    main()