# Documentación de pizza.py

Este archivo implementa un sistema para crear pizzas personalizadas utilizando el patrón de diseño Builder.

## Clases

### Pizza

Representa el producto final (una pizza).

#### Atributos:
- `tamano`: str - El tamaño de la pizza.
- `ingredientes`: list - Lista de ingredientes de la pizza.

#### Métodos:
- `__str__()`: Retorna una representación en string de la pizza.

### PizzaBuilder (Interfaz)

Define la interfaz para construir diferentes partes de la Pizza.

#### Métodos:
- `set_tamano(tamano)`: Establece el tamaño de la pizza.
- `add_queso()`: Añade queso a la pizza.
- `add_pepperoni()`: Añade pepperoni a la pizza.
- `add_champinones()`: Añade champiñones a la pizza.
- `build()`: Construye y retorna el objeto Pizza final.

### PizzaConcreteBuilder

Implementación concreta de PizzaBuilder.

#### Atributos:
- `pizza`: Pizza - La pizza que se está construyendo.

#### Métodos:
- `set_tamano(tamano)`: Establece el tamaño de la pizza.
- `add_queso()`: Añade queso a la pizza.
- `add_pepperoni()`: Añade pepperoni a la pizza.
- `add_champinones()`: Añade champiñones a la pizza.
- `build()`: Retorna la pizza construida.

Nota: Todos los métodos (excepto `build()`) retornan `self` para permitir el encadenamiento de métodos.

### Pizzeria

Utiliza el builder para construir pizzas personalizadas.

#### Atributos:
- `builder`: PizzaBuilder - El builder utilizado para construir pizzas.

#### Métodos:
- `construir_pizza_personalizada(tamano, ingredientes)`: Construye una pizza personalizada con el tamaño e ingredientes especificados.

## Funciones

### main()

Función principal que demuestra el uso de las clases definidas.

## Uso

El script crea una pizza personalizada utilizando el patrón Builder. Para ejecutar el script:

```python
python pizza.py
```

Esto creará una pizza grande con queso, pepperoni y champiñones, y mostrará su descripción en la consola.

## Patrón de Diseño

Este script implementa el patrón de diseño Builder, que permite la construcción de objetos complejos paso a paso. Las principales ventajas de usar este patrón en este contexto son:

1. Flexibilidad: Permite crear diferentes representaciones del mismo objeto (diferentes tipos de pizzas).
2. Separación de la construcción: Separa el código de construcción del objeto de su representación.
3. Control fino: Proporciona control sobre el proceso de construcción, permitiendo añadir ingredientes de forma individual.

