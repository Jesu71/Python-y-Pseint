# Documentación de carro.py

Este archivo define un sistema de clases para representar diferentes tipos de vehículos y una fábrica para crearlos.

## Clases

### Vehiculo (ABC)

Clase abstracta base para todos los vehículos.

#### Atributos:
- `marca`: str
- `modelo`: str
- `velocidad_maxima`: int
- `caracteristicas`: Dict[str, Any]

#### Métodos:
- `arrancar_motor()`: Método abstracto que debe ser implementado por las subclases.
- `agregar_caracteristica(clave: str, valor: Any)`: Agrega una característica al vehículo.
- `obtener_info()`: Retorna un diccionario con la información del vehículo.

### Coche(Vehiculo)

Representa un coche.

#### Métodos:
- `arrancar_motor()`: Implementación específica para coches.

### Bicicleta(Vehiculo)

Representa una bicicleta.

#### Métodos:
- `arrancar_motor()`: Implementación específica para bicicletas.

### Motocicleta(Vehiculo)

Representa una motocicleta.

#### Métodos:
- `arrancar_motor()`: Implementación específica para motocicletas.

### FabricaVehiculos

Fábrica para crear instancias de vehículos.

#### Métodos:
- `obtener_vehiculo(tipo_vehiculo: str, **kwargs)`: Crea y retorna una instancia del tipo de vehículo especificado.

## Funciones

### imprimir_info_vehiculo(vehiculo: Vehiculo)

Imprime la información detallada de un vehículo.

### main()

Función principal que demuestra el uso de las clases y funciones definidas.

## Uso

El script crea instancias de diferentes tipos de vehículos usando la `FabricaVehiculos`, agrega características a cada vehículo y luego imprime la información de cada uno.

Para ejecutar el script, simplemente ejecute:

```python
python carro.py
```

Esto creará tres vehículos diferentes (un coche, una bicicleta y una motocicleta) y mostrará su información en la consola.
