# Documentación: Sistema de Gestión de Puntuaciones de Gimnasia

## Descripción General
Este programa gestiona las puntuaciones de gimnastas en diferentes categorías (barras, barra de equilibrio y suelo). Lee los datos de entrada, mantiene un registro de las mejores puntuaciones por gimnasta y categoría, y genera un reporte ordenado de resultados.

## Estructura del Programa

### 1. Entrada de Datos Inicial
```python
gimnastas = input().split(",")  # Lista de nombres de gimnastas
categorias = input().split(",")  # Lista de categorías
N = int(input())                # Número de registros
```
- **Tipos de datos**: 
  - `gimnastas`: Lista de strings
  - `categorias`: Lista de strings
  - `N`: Entero
- **Formato esperado**:
  - Línea 1: "nombre1,nombre2,nombre3"
  - Línea 2: "bars,beam,floor"
  - Línea 3: Número entero

### 2. Inicialización de Estructura de Datos
```python
mejores_puntuaciones = {
    gimnasta: {"bars": None, "beam": None, "floor": None} 
    for gimnasta in gimnastas
}
```
- **Estructura**: Diccionario anidado
- **Características**:
  - Clave externa: Nombre de gimnasta
  - Valor: Diccionario de categorías
  - Valores iniciales: None
- **Ejemplo**:
```python
{
    "Ana": {"bars": None, "beam": None, "floor": None},
    "María": {"bars": None, "beam": None, "floor": None}
}
```

### 3. Procesamiento de Registros
```python
for _ in range(N):
    registro = input().split(",")
    nombre = registro[0].strip()
    bars = float(registro[1])
    beam = float(registro[2])
    floor = float(registro[3])
```
- **Proceso por registro**:
  1. Lee línea de entrada
  2. Divide por comas
  3. Convierte puntuaciones a float
  4. Actualiza mejores marcas

### 4. Actualización de Puntuaciones
```python
if nombre in mejores_puntuaciones:
    if mejores_puntuaciones[nombre]["bars"] is None or bars > mejores_puntuaciones[nombre]["bars"]:
        mejores_puntuaciones[nombre]["bars"] = bars
    # Similar para beam y floor
```
- **Lógica de actualización**:
  - Verifica existencia del gimnasta
  - Compara con puntuación existente
  - Actualiza si es mejor o primera marca

### 5. Generación de Resultados
```python
for gimnasta in gimnastas:
    resultado = []
    for categoria in categorias:
        puntuacion = mejores_puntuaciones[gimnasta][categoria]
        if puntuacion.is_integer():
            resultado.append(str(int(puntuacion)))
        else:
            resultado.append(str(puntuacion))
    print(",".join(resultado))
```
- **Proceso**:
  1. Itera sobre gimnastas en orden original
  2. Para cada categoría:
     - Obtiene mejor puntuación
     - Formatea resultado
  3. Une resultados con comas
  4. Imprime línea por gimnasta

## Estructuras de Datos Utilizadas

### 1. Diccionario Principal (mejores_puntuaciones)
- **Tipo**: Dict[str, Dict[str, float]]
- **Características**:
  - Acceso O(1)
  - Estructura jerárquica
  - Mantiene mejores marcas

### 2. Listas
- **gimnastas**: List[str]
  - Mantiene orden original
  - Nombres únicos
- **categorias**: List[str]
  - Define orden de salida
  - Categorías fijas

### 3. Tipos de Datos Básicos
- **str**: Nombres y categorías
- **float**: Puntuaciones
- **None**: Valores iniciales

## Flujo de Datos

1. **Entrada**:
   ```
   Ana,María,Juan
   bars,beam,floor
   3
   Ana,8.5,9.0,8.8
   María,9.2,8.7,9.1
   Juan,8.9,8.8,9.3
   ```

2. **Procesamiento Interno**:
   ```python
   {
       "Ana": {"bars": 8.5, "beam": 9.0, "floor": 8.8},
       "María": {"bars": 9.2, "beam": 8.7, "floor": 9.1},
       "Juan": {"bars": 8.9, "beam": 8.8, "floor": 9.3}
   }
   ```

3. **Salida**:
   ```
   8.5,9.0,8.8
   9.2,8.7,9.1
   8.9,8.8,9.3
   ```

## Complejidad Algorítmica

- **Tiempo**: 
  - Inicialización: O(G) donde G = número de gimnastas
  - Procesamiento: O(N) donde N = número de registros
  - Generación resultados: O(G * C) donde C = número de categorías
- **Espacio**: O(G * C)

## Consideraciones y Limitaciones

### 1. Validaciones
- No valida duplicados en nombres
- No valida rango de puntuaciones
- No valida formato de entrada

### 2. Formato de Números
- Elimina decimales en números enteros
- Mantiene decimales significativos

### 3. Orden
- Mantiene orden original de gimnastas
- Mantiene orden de categorías

## Casos Especiales

### 1. Puntuaciones Enteras
```python
entrada: "Juan,8.0,9.0,7.0"
salida: "8,9,7"
```

### 2. Sin Registros
```python
entrada: N = 0
salida: Todas las puntuaciones None
```

### 3. Actualizaciones Múltiples
```python
entradas múltiples para mismo gimnasta:
"Ana,8.5,9.0,8.8"
"Ana,9.0,8.5,9.1"
salida: "9.0,9.0,9.1"
```

## Optimizaciones Posibles

1. **Memoria**:
   - Usar float16 para puntuaciones
   - Implementar limpieza de datos

2. **Validaciones**:
   - Verificar rango de puntuaciones
   - Validar nombres de gimnastas
   - Verificar formato de entrada

3. **Funcionalidad**:
   - Agregar estadísticas adicionales
   - Incluir fecha/hora de registros
   - Agregar categorización por nivel

## Ejemplos de Uso Completo

### Ejemplo 1: Caso Básico
```
Entrada:
Ana,María
bars,beam,floor
2
Ana,8.5,9.0,8.8
María,9.2,8.7,9.1

Salida:
8.5,9.0,8.8
9.2,8.7,9.1
```

### Ejemplo 2: Actualizaciones
```
Entrada:
Ana
bars,beam,floor
2
Ana,8.5,9.0,8.8
Ana,9.0,8.5,9.1

Salida:
9.0,9.0,9.1
```
