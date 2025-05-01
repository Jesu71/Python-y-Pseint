class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        #Agrega un elemento a la pila.
        self.items.append(item)
    
    def desapilar(self):
        #Elimina y devuelve el último elemento de la pila.
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise Exception("La pila está vacía")
    
    def esta_vacia(self):
        #Verifica si la pila está vacía.
        return len(self.items) == 0
    
    def ver_tope(self):
        #Devuelve el elemento en la cima sin eliminarlo.
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise Exception("La pila está vacía")
    
    def __len__(self):
        #Retorna la cantidad de elementos en la pila.
        return len(self.items)

def ordenar_pila_ascendente(pila):
    #Ordena la pila en orden ascendente usando una pila auxiliar.
    pila_auxiliar = Pila()
    
    while not pila.esta_vacia():
        elemento_actual = pila.desapilar()
        
        while (not pila_auxiliar.esta_vacia() and 
               pila_auxiliar.ver_tope() > elemento_actual):
            pila.apilar(pila_auxiliar.desapilar())
        
        pila_auxiliar.apilar(elemento_actual)
    
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())
    
    return pila

def ordenar_pila_descendente(pila):
    #Ordena la pila en orden descendente usando una pila auxiliar.
    pila_auxiliar = Pila()
    
    while not pila.esta_vacia():
        elemento_actual = pila.desapilar()
        
        while (not pila_auxiliar.esta_vacia() and 
               pila_auxiliar.ver_tope() < elemento_actual):
            pila.apilar(pila_auxiliar.desapilar())
        
        pila_auxiliar.apilar(elemento_actual)
    
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())
    
    return pila

def imprimir_pila(pila, nombre):
    #Muestra los elementos de la pila sin modificarlos.
    print(f"{nombre}: ", end="")
    pila_temporal = Pila()
    
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        print(elemento, end=" ")
        pila_temporal.apilar(elemento)
    
    while not pila_temporal.esta_vacia():
        pila.apilar(pila_temporal.desapilar())
    
    print()

def ingresar_elementos_pila(tipo):
    #Permite al usuario ingresar números o caracteres en una pila.
    pila = Pila()
    
    if tipo == "numeros":
        print("\nIngrese números reales ('fin' para terminar):")
        while True:
            entrada = input("Número: ")
            if entrada.lower() == 'fin':
                break
            try:
                pila.apilar(float(entrada))
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
    
    elif tipo == "caracteres":
        print("\nIngrese caracteres ('fin' para terminar):")
        while True:
            entrada = input("Caracter: ")
            if entrada.lower() == 'fin':
                break
            if len(entrada) == 1:
                pila.apilar(entrada)
            else:
                print("Ingrese solo un caracter a la vez.")
    
    return pila

def main():
    print("Ordenamiento de pilas")
    print("=====================")
    
    #Pila de números reales ordenada ascendentemente.
    pila_numeros = ingresar_elementos_pila("numeros")
    
    print("\nPila de números original:")
    imprimir_pila(pila_numeros, "Números")
    
    ordenar_pila_ascendente(pila_numeros)
    
    print("\nPila de números ordenada ascendentemente:")
    imprimir_pila(pila_numeros, "Números")
    
    #Pila de caracteres ordenada ascendente y descendente.
    pila_caracteres = ingresar_elementos_pila("caracteres")
    
    print("\nPila de caracteres original:")
    imprimir_pila(pila_caracteres, "Caracteres")
    
    #Crear copias de la pila original.
    pila_caracteres_ascendente = Pila()
    pila_caracteres_descendente = Pila()
    pila_temp = Pila()
    
    while not pila_caracteres.esta_vacia():
        pila_temp.apilar(pila_caracteres.desapilar())
    
    while not pila_temp.esta_vacia():
        caracter = pila_temp.desapilar()
        pila_caracteres.apilar(caracter)
        pila_caracteres_ascendente.apilar(caracter)
        pila_caracteres_descendente.apilar(caracter)
    
    ordenar_pila_ascendente(pila_caracteres_ascendente)
    
    print("\nPila de caracteres ordenada ascendentemente:")
    imprimir_pila(pila_caracteres_ascendente, "Caracteres")
    
    ordenar_pila_descendente(pila_caracteres_descendente)
    
    print("\nPila de caracteres ordenada descendentemente:")
    imprimir_pila(pila_caracteres_descendente, "Caracteres")

if __name__ == "__main__":
    main()