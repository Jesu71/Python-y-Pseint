Algoritmo Numero_Perfecto
Definir n,x,perfecto Como Entero
Escribir "Escribe un numero" 
leer n
x = 2
Mientras x <= n Hacer
si n mod x == 0 Entonces
perfecto = perfecto + (n/x)
Finsi
x = x + 1
FinMientras
si perfecto == n Entonces
Escribir "El numero ",n," es un numero perfecto"
SiNo
Escribir "El numero ",n," no es un numero perfecto"
Finsi
FinAlgoritmo