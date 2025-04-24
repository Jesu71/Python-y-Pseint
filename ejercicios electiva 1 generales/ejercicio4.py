# Pedir una letra.
letra = input("Por favor, ingresa una letra del alfabeto: ").lower()

# Verificar si la letra es vocal o consonante.
if len(letra) == 1 and letra.isalpha():
    if letra in 'aeiou':
        print(f"La letra '{letra}' es una vocal.")
    else:
        print(f"La letra '{letra}' es una consonante.")
else:
    print(f"El carácter '{letra}' no es válido.")
