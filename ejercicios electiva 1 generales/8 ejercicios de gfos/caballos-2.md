# Documentación: Programa de Diferencia Mínima entre Fuerzas de Caballos

## Descripción General
Este programa calcula la diferencia mínima entre las fuerzas de N caballos. Lee la fuerza de cada caballo individualmente, las ordena y encuentra la menor diferencia entre cualquier par de caballos consecutivos en la lista ordenada.

## Estructura del Programa

### 1. Entrada de Datos
```python
N = int(input())  # Número de caballos
```
- **Tipo de dato**: Entero
- **Función**: Define la cantidad de caballos a procesar
- **Validación**: No requiere validación adicional

### 2. Recolección de Fuerzas
```python
fuerzas = []
for _ in range(N):
    fuerzas.append(int(input()))
```
- **Estructura de datos**: Lista de enteros
- **Proceso**:
  1. Crea una lista vacía
  2. Itera N veces
  3. En cada iteración lee un entero y lo añade a la lista
- **Ejemplo**: Para N=3, entradas "5", "8", "2" → [5, 8, 2]

### 3. Ordenamiento
```python
fuerzas.sort()
```
- **Método**: Ordenamiento in-place de Python (Timsort)
- **Complejidad**: O(n log n)
- **Resultado**: Lista ordenada de menor a mayor
- **Ejemplo**: [5, 8, 2] → [2, 5, 8]

### 4. Inicialización de Variable de Control
```python
min_diferencia = float('inf')
```
- **Tipo de dato**: Float
- **Función**: Almacena la diferencia mínima encontrada
- **Valor inicial**: Infinito (para garantizar que cualquier diferencia real será menor)

### 5. Cálculo de Diferencias
```python
for i in range(1, N):
    diferencia = fuerzas[i] - fuerzas[i-1]
    if diferencia < min_diferencia:
        min_diferencia = diferencia
```
- **Estructura**: Bucle for con condicional
- **Proceso**:
  1. Itera desde el segundo elemento hasta el último
  2. Calcula la diferencia con el elemento anterior
  3. Actualiza el mínimo si corresponde
- **Ejemplo**:
  - Para [2, 5, 8]:
    - Primera iteración: 5-2 = 3
    - Segunda iteración: 8-5 = 3
    - min_diferencia = 3

### 6. Salida
```python
print(min_diferencia)
```
- **Tipo de dato**: Entero o Float
- **Función**: Muestra la menor diferencia encontrada

## Complejidad Algorítmica
- **Tiempo**: O(n log n), dominado por el ordenamiento
- **Espacio**: O(n) para almacenar la lista de fuerzas

## Ejemplos de Uso

### Ejemplo 1:
```
Entrada:
3
5
8
2

Salida:
3
```

### Ejemplo 2:
```
Entrada:
4
1
3
2
5

Salida:
1
```

## Estructuras de Datos Utilizadas

1. **Tipos Primitivos**:
   - `int`: Para N y las fuerzas individuales
   - `float`: Para min_diferencia (infinito inicial)

2. **Estructuras Compuestas**:
   - `list`: Para almacenar las fuerzas
   - Características:
     - Acceso por índice O(1)
     - Método sort() incorporado
     - Inserción al final O(1) amortizado

## Flujo de Ejecución

1. Lectura del número de caballos (N)
2. Creación de lista vacía
3. Bucle de lectura de fuerzas:
   - Lee N valores
   - Los almacena en la lista
4. Ordenamiento de la lista
5. Inicialización de variable min_diferencia
6. Bucle de cálculo de diferencias:
   - Recorre la lista ordenada
   - Calcula diferencias consecutivas
   - Actualiza el mínimo cuando corresponde
7. Impresión del resultado

## Consideraciones y Limitaciones

1. **Entrada**:
   - N debe ser un entero positivo
   - Cada fuerza debe ser un número entero
   - Se requieren exactamente N fuerzas

2. **Rendimiento**:
   - El ordenamiento es el cuello de botella
   - Memoria proporcional al número de caballos
   - Eficiente para tamaños moderados de N

3. **Precisión**:
   - Trabaja con números enteros
   - La diferencia mínima será siempre ≥ 0
   - Puede manejar números negativos

4. **Casos Especiales**:
   - N = 1: No produce resultado válido
   - N = 2: Produce una única diferencia
   - Fuerzas iguales: Diferencia mínima será 0

## Optimizaciones Posibles

1. **Memoria**:
   - Se podría optimizar para grandes conjuntos usando generadores
   - Posibilidad de procesar entrada en streaming

2. **Tiempo**:
   - El algoritmo actual es óptimo para el problema dado
   - No es posible mejorar más allá de O(n log n) para el caso general
