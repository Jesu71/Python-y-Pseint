# Clase para almacenar y gestionar los votos
class AlmacenVotos:
    def __init__(self):
        self.votos = {}

    def agregar_voto(self, candidato):
        # Añadir el voto al candidato o crear entrada si no existe
        self.votos[candidato] = self.votos.get(candidato, 0) + 1

    def obtener_votos(self):
        # Retorna el diccionario de votos
        return self.votos


# Gestión del sistema de votación
class SistemaVotacion:
    def __init__(self):
        self.almacen = AlmacenVotos()
        self.candidatos = []

    def agregar_candidato(self, nombre):
        # Añadir un candidato al sistema
        if nombre not in self.candidatos:
            self.candidatos.append(nombre)
            print(f"Candidato '{nombre}' añadido.")
        else:
            print(f"El candidato '{nombre}' ya existe.")

    def mostrar_candidatos(self):
        # Muestra los candidatos actuales
        print("Candidatos:")
        for idx, candidato in enumerate(self.candidatos, 1):
            print(f"{idx}. {candidato}")

    def votar(self, candidato):
        # Verificar si el candidato existe antes de votar
        if candidato in self.candidatos:
            self.almacen.agregar_voto(candidato)
            print(f"Voto registrado para: {candidato}")
        else:
            print(f"El candidato '{candidato}' no existe. Voto no registrado.")

    def mostrar_resultados(self):
        # Mostrar el conteo de votos
        resultados = self.almacen.obtener_votos()
        if resultados:
            print("\nResultados de la votación:")
            for candidato, conteo in resultados.items():
                print(f"{candidato}: {conteo} voto(s)")
        else:
            print("No hay votos registrados aún.")


# Interfaz para interactuar con el sistema de votación
class AplicacionVotacion:
    def __init__(self):
        self.sistema = SistemaVotacion()

    def iniciar(self):
        # Menú para gestionar el sistema de votación
        while True:
            print("\n1: Agregar candidato")
            print("2: Mostrar candidatos")
            print("3: Votar")
            print("4: Ver resultados")
            print("5: Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                nombre = input("Introduce el nombre del candidato: ")
                self.sistema.agregar_candidato(nombre)
            elif opcion == '2':
                self.sistema.mostrar_candidatos()
            elif opcion == '3':
                self.sistema.mostrar_candidatos()
                candidato = input("Introduce el nombre del candidato para votar: ")
                self.sistema.votar(candidato)
            elif opcion == '4':
                self.sistema.mostrar_resultados()
            elif opcion == '5':
                print("Gracias por votar. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el sistema de votación
if __name__ == "__main__":
    AplicacionVotacion().iniciar()
