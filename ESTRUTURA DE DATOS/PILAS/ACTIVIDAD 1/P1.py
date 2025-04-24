class Pila:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)
        print(f"Elemento {elemento} agregado a la pila.")

    def mostrar_pila(self):
        print("Elementos en la pila:", self.elementos)

def main():
    pila = Pila()
    while True:
        elemento = input("Ingrese un elemento para agregar a la pila (o escriba 'salir' para terminar): ")
        if elemento.lower() == 'salir':
            break
        pila.agregar_elemento(elemento)

    pila.mostrar_pila()

if __name__ == "__main__":
    main()