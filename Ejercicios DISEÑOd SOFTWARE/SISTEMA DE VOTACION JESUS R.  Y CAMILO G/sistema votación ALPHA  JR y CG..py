# Clase gestion de datos
class AlmacenVotos:
    def __init__(self):
        self.votos = {}
    def agregar_voto(self, candidato):
        self.votos[candidato] = self.votos.get(candidato, 0) + 1
    def obtener_votos(self):
        return self.votos

# Gestión de Votos
class SistemaVotacion:
    def __init__(self):
        self.almacen = AlmacenVotos()
    def votar(self, candidato):
        self.almacen.agregar_voto(candidato)
        print(f"Voto registrado para: {candidato}")
    def mostrar_resultados(self):
        for candidato, conteo in self.almacen.obtener_votos().items():
            print(f"{candidato}: {conteo} voto(s)")

# Interfaz
class AplicacionVotacion:
    def __init__(self):
        self.sistema = SistemaVotacion()
    def iniciar(self):
        while True:
            opcion = input("1: Votar, 2: Ver resultados, 3: Salir\nElige: ")
            if opcion == '1':
                self.sistema.votar(input("Nombre del candidato: "))
            elif opcion == '2':
                self.sistema.mostrar_resultados()
            elif opcion == '3':
                print("Gracias por votar. ¡Hasta luego!")
                break

# Correr Sistema de Votación
if __name__ == "__main__":
    AplicacionVotacion().iniciar()