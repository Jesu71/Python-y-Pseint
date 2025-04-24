Algoritmo notasEstudiantes
	Definir nota1,nota2,nota3 Como Entero
	para estudiante=1 Hasta 3 con paso 1 Hacer
		Escribir "Ingrese el nombre del estudiante ", estudiante
		leer nombre
		Escribir "Ingrese las tres notas del estudiante ", nombre
		leer nota1, nota2, nota3
		promedio = nota1 + nota2 + nota3 / 3
		Escribir "La definitiva del estudiante ", nombre, " es: ", promedio
	FinPara
FinAlgoritmo