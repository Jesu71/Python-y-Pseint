from abc import ABC, abstractmethod
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class Vehiculo(ABC):
    marca: str
    modelo: str
    velocidad_maxima: int
    caracteristicas: Dict[str, Any] = field(default_factory=dict)

    @abstractmethod
    def arrancar_motor(self) -> str:
        pass

    def agregar_caracteristica(self, clave: str, valor: Any) -> None:
        self.caracteristicas[clave] = valor

    def obtener_info(self) -> Dict[str, Any]:
        return {
            "Tipo": self.__class__.__name__,
            "Marca": self.marca,
            "Modelo": self.modelo,
            "Velocidad Maxima": f"{self.velocidad_maxima} km/h",
            "Caracteristicas": self.caracteristicas
        }

@dataclass
class Coche(Vehiculo):
    def arrancar_motor(self) -> str:
        return "Arranca con un suave pero poderoso sonido del motor"

@dataclass
class Bicicleta(Vehiculo):
    def arrancar_motor(self) -> str:
        return "No tiene motor, comienza a pedalear!!"

@dataclass
class Motocicleta(Vehiculo):
    def arrancar_motor(self) -> str:
        return "Arranca con un potente rugido del motor runruuun!!!"

class FabricaVehiculos:
    @staticmethod
    def obtener_vehiculo(tipo_vehiculo: str, **kwargs) -> Vehiculo:
        vehiculos = {
            "coche": Coche,
            "bicicleta": Bicicleta,
            "motocicleta": Motocicleta
        }
        
        if tipo_vehiculo not in vehiculos:
            raise ValueError(f"Tipo de Vehículo Desconocido: {tipo_vehiculo}")
        
        return vehiculos[tipo_vehiculo](**kwargs)

def imprimir_info_vehiculo(vehiculo: Vehiculo) -> None:
    info = vehiculo.obtener_info()
    print("\n" + "="*40)
    print(f"     {info['Tipo'].upper()}")
    print("="*40)
    for clave, valor in info.items():
        if clave != "Tipo":
            print(f"{clave:.<20} {valor}")
    print(f"{'Accion':.<20} {vehiculo.arrancar_motor()}")
    print("="*40)

def main():
    fabrica = FabricaVehiculos()

    try:
        vehiculos = [
            fabrica.obtener_vehiculo("coche", marca="Toyota", modelo="TXL PRADO", velocidad_maxima=180),
            fabrica.obtener_vehiculo("bicicleta", marca="GW", modelo="BMX G1+", velocidad_maxima=25),
            fabrica.obtener_vehiculo("motocicleta", marca="Kawasaki", modelo="Z100", velocidad_maxima=270)
        ]

        vehiculos[0].agregar_caracteristica("tipo_combustible", "Gasolina")
        vehiculos[1].agregar_caracteristica("material_cuadro", "aluminio")
        vehiculos[2].agregar_caracteristica("cilindrada", "1000cc")

        for vehiculo in vehiculos:
            imprimir_info_vehiculo(vehiculo)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()