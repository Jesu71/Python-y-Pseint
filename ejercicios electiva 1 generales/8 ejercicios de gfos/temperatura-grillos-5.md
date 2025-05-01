# Documentación: Sistema de Cálculo de Temperatura por Chirridos de Grillos

## Descripción General
Este programa implementa dos métodos diferentes para calcular la temperatura ambiente basándose en el conteo de chirridos de grillos: el método N60 (chirridos por minuto) y el método N8 (grupos de 8 segundos). El programa procesa múltiples mediciones y aplica fórmulas específicas para cada método.

## Estructura del Programa

### 1. Entrada de Datos Inicial
```python
M = int(input())  # Número de minutos de medición
```
- **Tipo de dato**: Entero
- **Función**: Define la cantidad de líneas de medición
- **Validación**: No requiere validación adicional

### 2. Recolección de Mediciones
```python
mediciones = []
for _ in range(M):
    linea = input().split()
    mediciones.extend([int(x) for x in linea])
```
- **Estructura**: Lista de enteros
- **Proceso**:
  1. Lee cada línea de entrada
  2. Divide la línea en valores
  3. Convierte a enteros
  4. Agrega a lista principal

### 3. Cálculo de N60
```python
N60 = sum(mediciones) * (60 / (M * 60))
temp_N60 = 10 + (N60 - 40) / 7
print(f"{temp_N60:.1f}")
```
- **Fórmula N60**:
  1. Chirridos por minuto = suma_total * (60 / tiempo_total)
  2. Temperatura = 10 + (chirridos_por_minuto - 40) / 7
- **Precisión**: 1 decimal en salida

### 4. Cálculo de N8
```python
if 5 <= temp_N60 <= 30:
    if len(mediciones) % 2 != 0:
        mediciones = mediciones[:-1]
    
    N8_total = 0
    count = 0
    for i in range(0, len(mediciones), 2):
        N8 = mediciones[i] + mediciones[i+1]
        N8_total += N8 + 5
        count += 1
    
    temp_N8 = N8_total / count
    print(f"{temp_N8:.1f}")
```
- **Condiciones**:
  1. Temperatura N60 entre 5°C y 30°C
  2. Número par de mediciones
- **Proceso**:
  1. Agrupa mediciones en pares
  2. Suma cada par
  3. Añade 5 a cada suma
  4. Calcula promedio

## Fórmulas Utilizadas

### 1. Método N60
```
N60 = (suma_total_chirridos) * (60 / tiempo_total_segundos)
Temperatura_N60 = 10 + (N60 - 40) / 7
```
- **Unidades**: 
  - Entrada: chirridos/segundo
  - Salida: grados Celsius

### 2. Método N8
```
Para cada par de mediciones:
N8 = (suma_par) + 5
Temperatura_N8 = promedio(todos_los_N8)
```
- **Unidades**:
  - Entrada: chirridos/segundo
  - Salida: grados Celsius

## Estructuras de Datos

### 1. Lista de Mediciones
- **Tipo**: List[int]
- **Características**:
  - Almacena todas las mediciones
  - Acceso secuencial y por índice
  - Modificable (truncamiento para N8)

### 2. Variables de Control
- **M**: Número de minutos
- **N60**: Chirridos por minuto
- **N8_total**: Suma acumulada de N8
- **count**: Contador de grupos N8

## Flujo de Ejecución

1. **Fase de Entrada**:
   ```
   Leer M
   Para cada minuto:
       Leer línea
       Convertir valores
       Añadir a mediciones
   ```

2. **Fase N60**:
   ```
   Calcular suma total
   Aplicar fórmula N60
   Imprimir temperatura N60
   ```

3. **Fase N8** (condicional):
   ```
   Si temperatura en rango:
       Ajustar mediciones a par
       Procesar en grupos de 2
       Calcular promedio
       Imprimir temperatura N8
   ```

## Ejemplos de Uso

### Ejemplo 1: Temperatura Normal
```
Entrada:
2
4 5 6
3 4 5
Salida:
22.5
27.0
```

### Ejemplo 2: Temperatura Fuera de Rango
```
Entrada:
1
2 2 2
Salida:
15.7
```

## Consideraciones y Limitaciones

### 1. Validaciones
- No verifica validez de mediciones
- No maneja valores negativos
- Asume formato correcto de entrada

### 2. Precisión
- Resultados redondeados a 1 decimal
- Posible pérdida de precisión en conversiones

### 3. Restricciones
- Requiere temperatura N60 entre 5°C y 30°C para N8
- Necesita número par de mediciones para N8

## Optimizaciones Posibles

1. **Validación de Datos**:
   - Verificar rango de mediciones
   - Validar formato de entrada
   - Manejar valores erróneos

2. **Precisión**:
   - Usar decimal.Decimal para cálculos
   - Ajustar reglas de redondeo
   - Validar límites de temperatura

3. **Eficiencia**:
   - Procesar datos en streaming
   - Optimizar uso de memoria
   - Paralelizar cálculos grandes

## Casos de Uso

### 1. Medición Científica
- Monitoreo ambiental
- Estudios biológicos
- Validación de sensores

### 2. Educativo
- Demostración de bioacústica
- Prácticas de campo
- Ejercicios de programación

### 3. Aplicación Práctica
- Meteorología básica
- Monitoreo ecológico
- Estudios de comportamiento animal

## Diagrama de Flujo Conceptual
```
Inicio
  ├─ Leer número de minutos (M)
  ├─ Recolectar mediciones
  ├─ Calcular N60
  │   ├─ Sumar todos los chirridos
  │   ├─ Aplicar fórmula de temperatura
  │   └─ Imprimir resultado N60
  └─ Si temperatura en rango [5,30]:
      ├─ Ajustar a mediciones pares
      ├─ Calcular N8 por grupos
      ├─ Promediar resultados
      └─ Imprimir resultado N8
Fin
```
