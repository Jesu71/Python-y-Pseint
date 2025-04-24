def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
n = 10
print(f"El {n}-ésimo número de Fibonacci es: {fibonacci(n)}")