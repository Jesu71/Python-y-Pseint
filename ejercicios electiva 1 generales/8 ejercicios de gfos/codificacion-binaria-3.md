# Documentación: Programa de Codificación de Mensaje Binario

## Descripción General
Este programa implementa un codificador que convierte un mensaje de texto en una representación binaria especial. Primero convierte cada carácter a su representación binaria de 7 bits y luego aplica una codificación especial donde las secuencias de bits iguales se representan mediante bloques de ceros.

## Estructura del Programa

### 1. Entrada de Datos
```python
mensaje = input()  # Línea 1: mensaje de entrada
```
- **Tipo de dato**: String
- **Función**: Lee el mensaje a codificar
- **Ejemplo**: "C" → "C"

### 2. Conversión a Binario
```python
mensaje_binario = ''.join(f'{ord(c):07b}' for c in mensaje)
```
- **Proceso**:
  1. `ord(c)`: Convierte cada carácter a su valor ASCII
  2. `f'{:07b}'`: Formatea el número en binario con 7 bits
  3. `join()`: Une todos los bits en una sola cadena
- **Ejemplo**: "C" → "1000011"

### 3. Inicialización de Variables
```python
resultado = []  # Lista para almacenar los bloques codificados
i = 0          # Índice para recorrer el mensaje binario
```
- **Estructuras**:
  - Lista vacía para resultado
  - Contador para posición actual

### 4. Procesamiento Principal
```python
while i < len(mensaje_binario):
    bit = mensaje_binario[i]
    contador = 1
    while i + 1 < len(mensaje_binario) and mensaje_binario[i] == mensaje_binario[i + 1]:
        contador += 1
        i += 1
```
- **Estructura**: Bucle anidado
- **Proceso**:
  1. Lee el bit actual
  2. Cuenta bits consecutivos iguales
  3. Actualiza el índice

### 5. Codificación de Secuencias
```python
if bit == '1':
    resultado.append('0')    # Secuencia de unos
else:
    resultado.append('00')   # Secuencia de ceros
resultado.append('0' * contador)
```
- **Reglas de codificación**:
  - Secuencia de 1s: '0' seguido de N ceros
  - Secuencia de 0s: '00' seguido de N ceros
- **Ejemplo**:
  - "111" → "0 000"
  - "000" → "00 000"

### 6. Salida
```python
print(' '.join(resultado))
```
- **Formato**: Bloques separados por espacios
- **Tipo**: String

## Algoritmo de Codificación

### Reglas de Codificación
1. Cada carácter se convierte a 7 bits
2. Las secuencias de bits se codifican:
   - Para 1s: "0" + N ceros
   - Para 0s: "00" + N ceros
3. Los bloques se separan por espacios

### Ejemplo Completo
```
Entrada: "C"
1. ASCII a binario: "1000011"
2. Codificación por secuencias:
   - "1" → "0 0"
   - "000" → "00 000"
   - "11" → "0 00"
Salida: "0 0 00 000 0 00"
```

## Estructuras de Datos Utilizadas

1. **Strings**:
   - Mensaje de entrada
   - Representación binaria
   - Bloques individuales

2. **Lista**:
   - `resultado`: Almacena bloques codificados
   - Características:
     - Append O(1)
     - Join O(n)

3. **Variables de Control**:
   - `i`: Índice de posición
   - `contador`: Cantidad de bits consecutivos
   - `bit`: Bit actual en proceso

## Complejidad Algorítmica
- **Tiempo**: O(n), donde n es la longitud del mensaje binario
- **Espacio**: O(n) para almacenar el resultado

## Flujo de Ejecución

1. Lectura del mensaje
2. Conversión a representación binaria de 7 bits
3. Inicialización de variables
4. Bucle principal:
   - Identificación de secuencias
   - Conteo de bits consecutivos
   - Generación de bloques codificados
5. Unión de bloques y salida

## Consideraciones y Limitaciones

1. **Entrada**:
   - Acepta cualquier carácter ASCII
   - Cada carácter usa 7 bits
   - No hay límite de longitud explícito

2. **Memoria**:
   - Uso proporcional a la longitud del mensaje
   - Almacenamiento temporal de secuencias

3. **Rendimiento**:
   - Procesamiento lineal
   - Eficiente para mensajes de cualquier tamaño

4. **Casos Especiales**:
   - Mensaje vacío
   - Caracteres no ASCII
   - Secuencias largas de bits iguales

## Optimizaciones Posibles

1. **Memoria**:
   - Procesamiento por chunks para mensajes grandes
   - Generación directa de salida sin lista intermedia

2. **Velocidad**:
   - Procesamiento paralelo para mensajes muy grandes
   - Uso de búfer para optimizar joins

3. **Robustez**:
   - Validación de caracteres de entrada
   - Manejo de errores explícito
   - Soporte para diferentes codificaciones

## Ejemplos de Uso

### Ejemplo 1:
```
Entrada: "C"
Salida: "0 0 00 000 0 00"
```

### Ejemplo 2:
```
Entrada: "CC"
Salida: "0 0 00 000 0 00 0 0 00 000 0 00"
```

### Ejemplo 3:
```
Entrada: "%"
Salida: "00 0 0 0 00 00"
```
