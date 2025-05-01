# Documentación: Programa de Temperatura más Cercana a Cero

## Descripción General
Este programa encuentra la temperatura más cercana a 0 de una lista de temperaturas proporcionada por el usuario. En caso de empate entre una temperatura positiva y negativa con el mismo valor absoluto, selecciona la temperatura positiva.

## Estructura del Programa

### 1. Entrada de Datos
```python
N = int(input())  # Primera línea: número de temperaturas
```
- **Tipo de dato**: Entero
- **Función**: Lee la cantidad de temperaturas que se procesarán
- **Validación**: No requiere validación adicional

### 2. Casos Especiales
```python
if N == 0:
    print(0)
```
- **Condición**: Si N es 0
- **Acción**: Imprime 0 y termina el programa
- **Razón**: Caso base cuando no hay temperaturas para procesar

### 3. Lectura de Temperaturas
```python
temperaturas = list(map(int, input().split()))
```
- **Estructura de datos**: Lista de enteros
- **Proceso**:
  1. `input().split()`: Lee una línea y la divide en strings por espacios
  2. `map(int, ...)`: Convierte cada string a entero
  3. `list(...)`: Convierte el objeto map a una lista
- **Ejemplo**: "5 -2 3 8 -1" → [5, -2, 3, 8, -1]

### 4. Inicialización
```python
mas_cercana = temperaturas[0]
```
- **Tipo de dato**: Entero
- **Función**: Almacena la primera temperatura como referencia inicial
- **Acceso**: Índice 0 de la lista

### 5. Procesamiento Principal
```python
for temp in temperaturas:
    if abs(temp) < abs(mas_cercana) or (abs(temp) == abs(mas_cercana) and temp > mas_cercana):
        mas_cercana = temp
```
- **Estructura**: Bucle for con condicional compuesto
- **Lógica de comparación**:
  1. `abs(temp) < abs(mas_cercana)`: Compara distancias absolutas a 0
  2. `abs(temp) == abs(mas_cercana) and temp > mas_cercana`: Maneja empates
- **Ejemplo**:
  - Si temp = 5 y mas_cercana = -5, se selecciona 5
  - Si temp = -3 y mas_cercana = 4, se selecciona -3

### 6. Salida
```python
print(mas_cercana)
```
- **Tipo de dato**: Entero
- **Función**: Muestra la temperatura más cercana a 0

## Complejidad Algorítmica
- **Tiempo**: O(n), donde n es el número de temperaturas
- **Espacio**: O(n) para almacenar la lista de temperaturas

## Ejemplos de Uso

### Ejemplo 1:
```
Entrada:
5
1 -2 -8 4 5

Salida:
1
```

### Ejemplo 2:
```
Entrada:
3
-5 -4 -2

Salida:
-2
```

### Ejemplo 3:
```
Entrada:
0

Salida:
0
```

## Estructuras de Datos Utilizadas

1. **Tipos Primitivos**:
   - `int`: Para N y las temperaturas individuales
   - `bool`: Implícito en las comparaciones

2. **Estructuras Compuestas**:
   - `list`: Para almacenar el conjunto de temperaturas
   - Características:
     - Acceso por índice O(1)
     - Iteración secuencial
     - Tamaño dinámico

## Flujo de Ejecución

1. Lectura del número de temperaturas (N)
2. Si N = 0:
   - Imprime 0
   - Termina el programa
3. Si N > 0:
   - Lee la línea de temperaturas
   - Convierte a lista de enteros
   - Inicializa la variable de resultado
   - Itera sobre cada temperatura
   - Aplica la lógica de comparación
   - Imprime el resultado final

## Consideraciones y Limitaciones

1. **Entrada**:
   - Requiere que N sea un entero válido
   - La segunda línea debe contener exactamente N números
   - Los números deben ser enteros separados por espacios

2. **Memoria**:
   - Usa memoria proporcional al número de temperaturas
   - No optimizado para conjuntos de datos muy grandes

3. **Precisión**:
   - Trabaja con temperaturas enteras
   - No maneja temperaturas decimales
