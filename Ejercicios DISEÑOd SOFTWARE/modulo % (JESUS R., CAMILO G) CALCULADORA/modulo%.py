# Solicitar el numero del porcentaje a calcular.
porc = float(input("Ingrese el % que se desea calcular: "))

# Solicitar el número base el cual se le va sacar el porcentaje previamente ya dado.
num = float(input("Ingrese el número base: "))

# Calcular el porcentaje, funcion "%".
result = porc * num / 100

# Mostrar el resultado.
print(f"El {porc}% de {num} es {round(result, 2)}")