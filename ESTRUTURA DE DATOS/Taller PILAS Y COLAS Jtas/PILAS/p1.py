class Pila:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        return None

    def empty(self):
        return len(self.stack) == 0

def invertir_cadena(cadena):
    # Crear una pila.
    pila = Pila()
    
    # Insertar cada carácter de la cadena en la pila.
    for caracter in cadena:
        pila.push(caracter)
    
    # Construir la cadena invertida.
    cadena_invertida = ""
    while not pila.empty():
        cadena_invertida += pila.pop()
    
    return cadena_invertida

# Función principal.
def main():
    # Solicitar cadena al usuario.
    cadena_original = input("Ingresa una cadena para invertir: ")
    
    # Invertir la cadena.
    cadena_invertida = invertir_cadena(cadena_original)
    
    # Mostrar resultados.
    print("Cadena original:", cadena_original)
    print("Cadena invertida:", cadena_invertida)

if __name__ == "__main__":
    main()