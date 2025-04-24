Funcion pesoideal<-operacion(estatura,sexo)
	si sexo="masculino" Entonces
		pesoideal<-(estatura-100)*0.85
	SiNo
		pesoideal<-(estatura-100)*0.75
	FinSi
Fin Funcion
Algoritmo peso_ideal
	Definir peso,estatura Como Real
	Definir sexo Como Caracter
	Escribir "Ingrese el sexo de la persona:"
	Leer sexo
	Escribir "Ingrese la estatura de la persona:"
	Leer estatura
	Escribir "Ingrese el peso actual de la persona:"
	Leer peso
	Escribir "Su peso ideal es:" operacion(estatura,sexo)
FinAlgoritmo