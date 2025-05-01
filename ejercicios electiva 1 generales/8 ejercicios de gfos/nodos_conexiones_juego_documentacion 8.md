
# Documentación detallada del código para cortar conexiones de nodos en un juego

## 1. Descripción general del código

Este código simula una situación de un juego donde un agente llamado "Bobnet" debe cortar las conexiones entre nodos para evitar que un atacante (controlado por la IA) llegue a los nodos llamados "gateways". El objetivo es que Bobnet actúe lo más rápido posible, cortando estratégicamente las conexiones que lo acercan a los gateways.

## 2. Flujo de funcionamiento del código

### 2.1. Lectura de entrada
- El código toma como entrada varios parámetros:
  1. **`n`**: El número total de nodos en la red.
  2. **`l`**: El número de enlaces o conexiones entre los nodos.
  3. **`e`**: El número de nodos que son gateways, es decir, nodos que están siendo protegidos.

### 2.2. Inicialización de las conexiones
- Se inicializa una lista llamada `links`, que almacena las conexiones entre los nodos. Cada enlace entre dos nodos se representa como una tupla `(n1, n2)`.

### 2.3. Lectura de los gateways
- Los gateways se almacenan en la lista `gateways`, donde cada elemento es un nodo que debe protegerse.

### 2.4. Bucle del juego
- Dentro del bucle `while True`, se lee la posición actual del agente Bobnet (nodo en el que se encuentra en ese turno).
- Se buscan las conexiones en `links` que conecten el nodo actual del agente a un gateway. Si una de esas conexiones existe, se corta, es decir, se imprime la conexión y luego se elimina de `links`.

### 2.5. Estrategia de corte
- **Si el agente está conectado directamente a un gateway**:
  - Se corta el enlace entre el nodo actual del agente y el gateway.
  - Se elimina este enlace de la lista `links`.
- **Si no hay conexión directa a un gateway**:
  - Se corta el primer enlace disponible en la lista `links`.

## 3. Estructura de datos utilizada

### 3.1. `links`
- Esta es una lista que almacena las conexiones entre los nodos. Cada conexión es representada como una tupla `(n1, n2)`, donde `n1` y `n2` son nodos conectados.

### 3.2. `gateways`
- Es una lista de enteros que almacena los nodos que son gateways, es decir, aquellos nodos que deben protegerse.

### 3.3. Variables clave
- **`si`**: Esta variable almacena la posición actual del agente Bobnet en cada turno.
- **`n1, n2`**: Estas variables representan los nodos conectados por un enlace.

## 4. Flujo del código en cada turno

1. **Leer la posición de Bobnet**: Se guarda la posición del agente.
2. **Buscar conexiones con gateways**: El código revisa todas las conexiones en `links` para ver si el agente está directamente conectado a un gateway.
3. **Cortar el enlace más crítico**:
   - Si hay una conexión directa con un gateway, se corta.
   - Si no hay una conexión directa, se corta el primer enlace en `links` de manera arbitraria.
4. **Eliminar el enlace cortado**: Una vez que se corta un enlace, se elimina de la lista `links` para no volver a cortarlo en el futuro.

## 5. Potenciales mejoras y optimizaciones

- Actualmente, si no hay conexión directa con un gateway, se corta un enlace arbitrario. Se podría mejorar la estrategia para cortar conexiones que retrasen al atacante de manera más efectiva.
- Además, se podría implementar un sistema de prioridad que analice qué enlace cortar basándose en la cercanía a un gateway o la cantidad de caminos disponibles.

## 6. Ejemplo de uso

### Entrada:
```
4 4 2
0 1
1 2
2 3
0 2
2
3
```

### Salida (Posibles movimientos del agente Bobnet):
```
0 2
1 2
```

En este ejemplo, el agente Bobnet corta primero la conexión directa entre los nodos 0 y 2 (conexión entre el agente y un gateway) y luego corta la siguiente conexión relevante en el próximo turno.

