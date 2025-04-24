# Documentación: Ejemplo de Ransomware en Python

## Descripción General
Este script es una implementación simplificada de un ransomware con fines educativos. Demuestra conceptos de criptografía, manipulación de archivos y diseño de software. El programa simula el proceso de encriptar archivos en una carpeta específica, solicitar un "pago" para desbloquearlos, y luego desencriptarlos.

## Estructura del Código

### Importaciones
```python
import os
from cryptography.fernet import Fernet
```
- `os`: Utilizado para operaciones del sistema de archivos.
- `Fernet`: Una implementación de criptografía simétrica.

### Configuración
```python
ARCHIVO_DE_SEGREDO = "desbloquear.key"
COMISION = 100
```
- Define constantes para el nombre del archivo de clave y la comisión simulada.

### Funciones Principales

1. `generar_clave()`
   - Genera una nueva clave de encriptación.
   - Guarda la clave en un archivo.

2. `cargar_clave()`
   - Lee la clave de encriptación desde el archivo.

3. `encriptar_archivos(ruta, clave)`
   - Recorre recursivamente todos los archivos en la ruta especificada.
   - Encripta cada archivo usando la clave proporcionada.

4. `desencriptar_archivos(ruta, clave)`
   - Similar a `encriptar_archivos()`, pero realiza la operación inversa.

5. `desbloquear_archivos(ruta)`
   - Simula el proceso de desbloqueo después del "pago".
   - Verifica la existencia de la clave y desencripta los archivos.

### Flujo Principal
```python
if __name__ == "__main__":
    # Código principal aquí
```
- Define la ruta objetivo.
- Encripta los archivos.
- Simula la solicitud de pago.
- Desencripta los archivos si se "paga".
- Elimina el archivo de clave.

## Aspectos de Diseño de Software

1. **Modularidad**: El código está organizado en funciones con responsabilidades específicas, facilitando la lectura y mantenimiento.

2. **Uso de Constantes**: Variables como `ARCHIVO_DE_SEGREDO` y `COMISION` están definidas como constantes, mejorando la mantenibilidad.

3. **Manejo de Archivos**: Utiliza context managers (`with` statements) para asegurar que los archivos se cierren correctamente.

4. **Recursividad**: Usa `os.walk()` para recorrer directorios de manera recursiva.

5. **Separación de Concerns**: Las operaciones de encriptación y desencriptación están separadas en funciones distintas.

6. **Simulación de Interfaz de Usuario**: Aunque básica, incluye una interacción simulada con el usuario.

7. **Manejo de Errores**: Incluye un manejo básico de errores, como la verificación de la existencia del archivo de clave.

## Consideraciones de Seguridad
- Este código es una simplificación y no incluye muchas características de seguridad que un ransomware real tendría.
- La clave de encriptación se almacena localmente, lo cual no sería seguro en un escenario real.
- No hay mecanismos para asegurar que el pago se haya realizado realmente.

## Conclusión
Este script demuestra conceptos básicos de criptografía y manipulación de archivos en Python. Sirve como un ejemplo educativo de cómo podría estructurarse un software malicioso, pero carece de la complejidad y las medidas de seguridad de un ransomware real. Es crucial enfatizar que el desarrollo o uso de ransomware es ilegal y éticamente incorrecto fuera de entornos controlados de investigación y educación.
