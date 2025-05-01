Algoritmo N_primos
	Definir x,num,contador Como Entero
	Para num = 1 Hasta 50 Hacer
		x=1
		contador = 0
		Mientras x<= num Hacer
			si num mod x == 0 Entonces
				contador = contador + 1
			FinSi
			x=x+1
		FinMientras
		si contador == 2 Entonces
			Escribir "El numero ",num," es primo"
		FinSi
	FinPara
FinAlgoritmo
