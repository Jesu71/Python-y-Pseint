
# Documentación detallada del código de Búsqueda en Anchura (BFS) para resolver el problema del lobo, la cabra y la col

## 1. Descripción general del código

Este código resuelve el clásico problema del **lobo, la cabra y la col** utilizando el algoritmo de **búsqueda en anchura (BFS)**. El problema plantea que un agricultor debe transportar un lobo, una cabra y una col a través de un río usando un bote, pero solo puede llevar un objeto a la vez. No se puede dejar al lobo solo con la cabra, ni a la cabra sola con la col, ya que en ambos casos uno se comería al otro. El objetivo es encontrar una secuencia válida de movimientos para que todos lleguen al otro lado del río sin incidentes.

## 2. Flujo de funcionamiento del código

### 2.1. Entrada de datos
- El código toma dos entradas:
  1. **`initial`**: El estado inicial del problema, donde cada elemento puede estar en la orilla izquierda (`L`) o en la orilla derecha (`R`).
  2. **`target`**: El estado objetivo donde todos los elementos deben estar en la orilla opuesta a la que comenzaron.
  
  Cada estado se representa como una tupla con cuatro elementos: 
  `(agricultor, lobo, cabra, col)`.

### 2.2. Función `is_valid(state)`
- Esta función verifica si un estado es válido, es decir, que ni la cabra se quede con el lobo sin la presencia del agricultor ni la cabra se quede con la col sin la presencia del agricultor.
- **Entrada**: `state` (tupla con 4 valores: `agricultor`, `lobo`, `cabra`, `col`).
- **Salida**: `True` si el estado es válido, `False` si es inválido.

### 2.3. Función `get_next_states(state)`
- Dada una situación actual (estado), genera todos los posibles estados a los que se puede llegar moviendo al agricultor y, opcionalmente, a uno de los otros tres elementos (lobo, cabra o col) al otro lado del río.
- Para cada nuevo estado generado, se verifica su validez con `is_valid()` y, si es válido, se agrega a la lista de posibles siguientes estados.
- **Entrada**: `state` (estado actual del agricultor, lobo, cabra y col).
- **Salida**: Lista de tuplas que representan los siguientes estados válidos.

### 2.4. Función `bfs(initial, target)`
- Implementa el algoritmo de búsqueda en anchura (BFS) para explorar los diferentes estados desde el estado inicial hasta llegar al estado objetivo.
- Usa una cola (estructura FIFO) para realizar la exploración por niveles, asegurándose de encontrar la solución más corta.
- **Entradas**:
  - `initial`: Estado inicial (tupla).
  - `target`: Estado objetivo (tupla).
- **Salida**: La secuencia de estados que llevan del estado inicial al objetivo, si existe una solución. Si no la hay, devuelve `None`.

### 2.5. Impresión del resultado
- Si se encuentra una solución, se imprimen los estados en la secuencia que lleva del estado inicial al estado objetivo.
- Si no se encuentra una solución, se imprime el mensaje “No se encontró solución”.

## 3. Estructura de datos

### 3.1. `state`
- Un estado se representa como una tupla de cuatro elementos:
  - `agricultor`: Posición del agricultor (izquierda: `L` o derecha: `R`).
  - `lobo`: Posición del lobo.
  - `cabra`: Posición de la cabra.
  - `col`: Posición de la col.

### 3.2. `queue`
- Es una cola de la librería `deque`, que almacena los estados por explorar. Cada elemento de la cola es una tupla con el estado actual y la secuencia de estados que llevaron a él.

### 3.3. `visited`
- Es un conjunto que almacena los estados ya visitados, para evitar ciclos o repeticiones innecesarias durante la búsqueda.

### 3.4. `path`
- Es una lista que representa la secuencia de estados desde el estado inicial hasta el estado actual. Se actualiza conforme se exploran nuevos estados.

## 4. Ejemplo de uso

### Entrada:
```
L L L L
R R R R
```

### Salida (Posible solución):
```
L L L L
R L R L
L L L L
R R R L
L R L L
R R R R
```

En este ejemplo, el agricultor logra llevar al lobo, la cabra y la col al otro lado del río sin incidentes.

## 5. Potenciales mejoras y recomendaciones
- Se podría mejorar el código añadiendo manejo de errores en la entrada de datos.
- También se podría optimizar el código almacenando solo las posiciones de los elementos que cambian en cada transición de estado.
