# Gestión de Pestañas con Estructura de Pila en Python

## Descripción General
Este programa simula un administrador de pestañas utilizando una estructura de datos de pila (stack), donde la última pestaña abierta es la primera en cerrarse (principio LIFO - Last In, First Out).

## Estructura de la Clase `Pila`

### Métodos Principales:
1. `__init__()`: 
   - Inicializa una lista vacía `self.stack` para almacenar las pestañas
   - Es el constructor de la clase que se ejecuta al crear un nuevo objeto Pila

2. `push(item)`:
   - Agrega un nuevo elemento (pestaña) al final de la pila
   - Usa el método `append()` de listas de Python
   - Simula abrir una nueva pestaña

3. `pop()`:
   - Elimina y devuelve el último elemento de la pila
   - Si la pila está vacía, devuelve un mensaje de error
   - Simula cerrar la pestaña más reciente

4. `top()`:
   - Devuelve el último elemento de la pila sin eliminarlo
   - Si la pila está vacía, devuelve un mensaje de error
   - Muestra la pestaña actual

5. `empty()`:
   - Verifica si la pila está vacía
   - Devuelve `True` si no hay elementos, `False` en caso contrario

6. `size()`:
   - Devuelve el número de elementos en la pila
   - Cuenta cuántas pestañas están abiertas

7. `clear()`:
   - Borra todos los elementos de la pila
   - Simula cerrar todas las pestañas

8. `buscar_pestaña(nombre)`:
   - Busca una pestaña por su nombre
   - Retorna el índice de la pestaña si se encuentra
   - No distingue entre mayúsculas y minúsculas
   - Devuelve -1 si no encuentra la pestaña

9. `eliminar_pestaña(nombre)`:
   - Elimina una pestaña específica por su nombre
   - Usa `buscar_pestaña()` para encontrar el índice
   - Elimina la pestaña del índice encontrado
   - Devuelve `True` si se eliminó, `False` si no se encontró

## Funcionamiento del Menú

### Opciones del Menú:
1. Abrir nueva pestaña
2. Cerrar pestaña actual
3. Ver pestaña actual
4. Verificar si hay pestañas abiertas
5. Contar pestañas abiertas
6. Cerrar todas las pestañas
7. Buscar y ver pestaña
8. Eliminar pestaña específica
9. Listar todas las pestañas
10. Salir

## Almacenamiento de Pestañas

### Dónde se Guardan las Pestañas
- Las pestañas se almacenan en memoria, específicamente en `self.stack`
- Es un almacenamiento temporal (volátil)
- Se pierden al cerrar el programa
- No se guardan en un archivo o base de datos permanente

### Características del Almacenamiento
- Utiliza una lista de Python
- Orden de almacenamiento: Último en entrar, primero en salir (LIFO)
- Cada pestaña es un string en la lista
- No hay límite predefinido de pestañas

## Ejemplo de Uso

```python
# Crear una nueva pila de pestañas
pila = Pila()

# Abrir pestañas
pila.push("Google")
pila.push("YouTube")
pila.push("GitHub")

# Estado actual
print(pila.top())  # Muestra "GitHub"
print(pila.size())  # Muestra 3

# Cerrar pestaña actual
pila.pop()  # Cierra "GitHub"
```

## Consideraciones
- El programa funciona solo durante la ejecución
- No guarda las pestañas entre sesiones
- Simple interfaz de consola
- Fácilmente extensible para más funcionalidades

## Posibles Mejoras
- Guardar pestañas en archivo
- Implementar persistencia de datos
- Añadir más funcionalidades de gestión
