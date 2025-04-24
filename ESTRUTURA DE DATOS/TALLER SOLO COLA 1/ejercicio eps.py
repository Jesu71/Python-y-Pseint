import time
from datetime import datetime
from collections import deque

class SistemaGestionTurnos:
    def __init__(self):
        # Inicializa la cola de turnos y los atendidos.
        self.cola_turnos = deque()
        self.turnos_atendidos = []
        self.contador_turnos = 1  # Contador de turnos secuenciales.
    
    def generar_turno(self, nombre, tipo_consulta):
        # Genera un nuevo turno y lo añade a la cola.
        hora_actual = datetime.now()
        turno = {
            'numero': self.contador_turnos,
            'nombre': nombre,
            'tipo_consulta': tipo_consulta,
            'hora_llegada': hora_actual,
            'tiempo_espera': None,
            'hora_atencion': None
        }
        self.cola_turnos.append(turno)
        self.contador_turnos += 1
        return turno
    
    def atender_turno(self):
        # Atiende al próximo turno en la cola.
        if not self.cola_turnos:
            return None
        turno = self.cola_turnos.popleft()
        hora_actual = datetime.now()
        tiempo_espera = (hora_actual - turno['hora_llegada']).total_seconds() / 60
        turno['hora_atencion'] = hora_actual
        turno['tiempo_espera'] = tiempo_espera
        self.turnos_atendidos.append(turno)
        return turno
    
    def visualizar_cola(self):
        # Devuelve los turnos pendientes en la cola.
        return list(self.cola_turnos)
    
    def visualizar_atendidos(self):
        # Devuelve los turnos que ya fueron atendidos.
        return self.turnos_atendidos
    
    def total_en_espera(self):
        # Devuelve el número de personas en espera.
        return len(self.cola_turnos)

def mostrar_menu():
    # Muestra el menú principal del sistema.
    print("\n===== SISTEMA DE GESTIÓN DE TURNOS EPS =====")
    print("1. Generar nuevo turno")
    print("2. Visualizar turnos en espera")
    print("3. Atender próximo turno")
    print("4. Ver historial de turnos atendidos")
    print("5. Salir")
    print("===========================================")

def formatear_tiempo(minutos):
    # Formatea el tiempo en minutos a un formato legible.
    if minutos < 1:
        return f"{int(minutos * 60)} segundos"
    elif minutos < 60:
        return f"{minutos:.1f} minutos"
    else:
        horas = int(minutos / 60)
        mins = minutos % 60
        return f"{horas} hora{'s' if horas > 1 else ''} y {mins:.1f} minutos"

def main():
    # Función principal del sistema.
    sistema = SistemaGestionTurnos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            # Generar un nuevo turno.
            print("\n----- GENERAR NUEVO TURNO -----")
            nombre = input("Nombre del usuario: ")
            print("\nTipos de consulta disponibles:")
            print("1. Medicina General")
            print("2. Especialista")
            print("3. Laboratorio")
            print("4. Farmacia")
            tipo_opcion = input("Seleccione el tipo de consulta (1-4): ")
            tipos_consulta = {
                "1": "Medicina General",
                "2": "Especialista",
                "3": "Laboratorio",
                "4": "Farmacia"
            }
            if tipo_opcion in tipos_consulta:
                tipo_consulta = tipos_consulta[tipo_opcion]
                turno = sistema.generar_turno(nombre, tipo_consulta)
                print("\n¡Turno generado con éxito!")
                print(f"Número de turno: {turno['numero']}")
                print(f"Nombre: {turno['nombre']}")
                print(f"Tipo de consulta: {turno['tipo_consulta']}")
                print(f"Hora de llegada: {turno['hora_llegada'].strftime('%H:%M:%S')}")
                print(f"Personas en espera: {sistema.total_en_espera()}")
            else:
                print("\nError: Tipo de consulta inválido.")
        
        elif opcion == "2":
            # Visualizar turnos en espera.
            print("\n----- TURNOS EN ESPERA -----")
            turnos = sistema.visualizar_cola()
            if not turnos:
                print("No hay turnos en espera.")
            else:
                print(f"Total de turnos en espera: {len(turnos)}")
                print("\nLista de espera:")
                print("--------------------------------------------------")
                print("| N° |    Nombre    |    Tipo Consulta    | Hora |")
                print("--------------------------------------------------")
                for turno in turnos:
                    hora = turno['hora_llegada'].strftime('%H:%M:%S')
                    print(f"| {turno['numero']:2d} | {turno['nombre'][:12]:12s} | {turno['tipo_consulta'][:20]:20s} | {hora} |")
                print("--------------------------------------------------")
        
        elif opcion == "3":
            # Atender el próximo turno.
            print("\n----- ATENDER TURNO -----")
            turno = sistema.atender_turno()
            if turno:
                print("¡Turno atendido!")
                print(f"Número de turno: {turno['numero']}")
                print(f"Usuario: {turno['nombre']}")
                print(f"Tipo de consulta: {turno['tipo_consulta']}")
                print(f"Hora de llegada: {turno['hora_llegada'].strftime('%H:%M:%S')}")
                print(f"Hora de atención: {turno['hora_atencion'].strftime('%H:%M:%S')}")
                print(f"Tiempo de espera: {formatear_tiempo(turno['tiempo_espera'])}")
            else:
                print("No hay turnos pendientes para atender.")
        
        elif opcion == "4":
            # Ver historial de turnos atendidos.
            print("\n----- HISTORIAL DE TURNOS ATENDIDOS -----")
            turnos = sistema.visualizar_atendidos()
            if not turnos:
                print("No se han atendido turnos todavía.")
            else:
                print(f"Total de turnos atendidos: {len(turnos)}")
                print("\nHistorial:")
                print("--------------------------------------------------------------------")
                print("| N° |    Nombre    |    Tipo Consulta    | Tiempo de Espera       |")
                print("--------------------------------------------------------------------")
                for turno in turnos:
                    tiempo = formatear_tiempo(turno['tiempo_espera'])
                    print(f"| {turno['numero']:2d} | {turno['nombre'][:12]:12s} | {turno['tipo_consulta'][:20]:20s} | {tiempo:22s} |")
                print("--------------------------------------------------------------------")
                tiempo_total = sum(turno['tiempo_espera'] for turno in turnos)
                tiempo_promedio = tiempo_total / len(turnos)
                print(f"\nTiempo promedio de espera: {formatear_tiempo(tiempo_promedio)}")
        
        elif opcion == "5":
            # Salir del programa.
            print("\nGracias por usar el Sistema de Gestión de Turnos EPS.")
            print("Cerrando el programa...")
            break
        
        else:
            # Opción inválida.
            print("\nOpción inválida. Por favor, seleccione una opción del 1 al 5.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()