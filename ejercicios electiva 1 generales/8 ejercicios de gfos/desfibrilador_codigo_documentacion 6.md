
# Documentación detallada del código de cálculo de desfibrilador más cercano

## 1. Descripción general del código

Este código calcula el desfibrilador más cercano a un usuario a partir de las coordenadas (latitud y longitud) del usuario y de varios desfibriladores, cuyos datos se ingresan en el programa. El cálculo se realiza utilizando la fórmula de Haversine para calcular la distancia entre dos puntos en una esfera (en este caso, la Tierra). El resultado final es el nombre del desfibrilador más cercano al usuario.

## 2. Flujo de funcionamiento del código

### 2.1. Entrada de datos
- El usuario ingresa sus propias coordenadas geográficas (longitud y latitud), las cuales se convierten de string a float, y se reemplazan comas por puntos si es necesario.
- Posteriormente, el usuario indica el número `n` de desfibriladores disponibles.
- En un bucle, el programa recibe la información de cada desfibrilador, separando los diferentes valores de cada línea por punto y coma (`;`). Entre estos valores, el programa extrae las coordenadas (latitud y longitud) y el nombre del desfibrilador.

### 2.2. Cálculo de distancias
- Para cada desfibrilador, se calcula la distancia desde las coordenadas del usuario hasta las coordenadas del desfibrilador usando una fórmula basada en la proyección de Mercator, que aproxima la distancia en una esfera.
- Esta fórmula toma en cuenta las latitudes y longitudes en radianes, y usa la constante del radio de la Tierra (6371 km) para calcular la distancia.

### 2.3. Selección del desfibrilador más cercano
- A medida que el bucle itera a través de los desfibriladores, el programa mantiene un registro de cuál es el más cercano hasta ese momento, comparando las distancias calculadas.
- Al finalizar el bucle, se imprime el nombre del desfibrilador más cercano al usuario.

## 3. Explicación de funciones

### 3.1. `to_radians(deg)`
- Convierte un valor de grados a radianes.
- **Entrada**: `deg` (float) - ángulo en grados.
- **Salida**: valor en radianes calculado como `deg * π / 180`.

### 3.2. `calculate_distance(lonA, latA, lonB, latB)`
- Calcula la distancia entre dos puntos geográficos usando la fórmula de la proyección de Mercator.
- **Entradas**:
  - `lonA`, `latA`: Longitud y latitud del punto A (usuario), en radianes.
  - `lonB`, `latB`: Longitud y latitud del punto B (desfibrilador), en radianes.
- **Salida**: distancia en kilómetros entre los dos puntos.

## 4. Estructura de datos

- **Variables locales**:
  - `lon`, `lat`: Coordenadas geográficas del usuario en formato float.
  - `n`: Número total de desfibriladores.
  - `nombre_defib_mas_cercano`: Almacena el nombre del desfibrilador más cercano encontrado.
  - `distancia_minima`: Inicializado como infinito (`float('inf')`), almacena la menor distancia calculada durante el bucle.
  - `partes`: Lista resultante de dividir la cadena de datos de cada desfibrilador por `;`, para extraer los atributos de cada desfibrilador.
  - `distancia`: Distancia entre el usuario y el desfibrilador calculado con la fórmula.

## 5. Ejemplo de uso

### Entrada:
```
3.879483, 43.608177
3
1;Desfibrilador 1;Dirección 1;Teléfono 1;3,879522;43,607527
2;Desfibrilador 2;Dirección 2;Teléfono 2;3,879300;43,607960
3;Desfibrilador 3;Dirección 3;Teléfono 3;3,879341;43,608089
```

### Salida:
```
Desfibrilador 3
```

En este caso, el desfibrilador más cercano a las coordenadas del usuario es el "Desfibrilador 3".

## 6. Potenciales mejoras y recomendaciones
- Este código asume que las coordenadas están en el formato correcto y que los datos están separados por punto y coma. Se podría agregar manejo de errores o validaciones.
- La fórmula de Mercator no es tan precisa para distancias grandes, por lo que sería mejor usar la fórmula de Haversine para cálculos geodésicos más precisos.
