Algoritmo notas_estudiantes
	//Hecho por Ingenieros Jesus R. y Vaner V.//
	Dimension nombres_estudiantes[10];
	Dimension notas_1[200];
	Dimension notas_2[200];
	Dimension notas_3[200];
	aprobatoria <- 70
	aprobados <- 0
	reprobados <- 0
	Escribir "Ingrese la cantidad de estudiantes: ";
	Leer cantidad_elementos;
	Para i<-1 Hasta cantidad_elementos Hacer
		Escribir "Ingrese el nombre del estudiante ",i,": "
		Leer nombres_estudiantes[i];
		Escribir "Ingrese la nota #1 de ",nombres_estudiantes[i],": "
		Leer notas_1[i];
		Escribir "Ingrese la nota #2 de ",nombres_estudiantes[i],": "
		Leer notas_2[i];
		Escribir "Ingrese la nota #3 de ",nombres_estudiantes[i],": "
		Leer notas_3[i];
	FinPara
	Escribir "Estudiantes: ", cantidad_elementos;
	Para i<-1 Hasta cantidad_elementos Hacer
		Escribir "______________________________________";
		Escribir "Estudiante: ", nombres_estudiantes[i];
		Escribir "Nota 1: ", notas_1[i];
		Escribir "Nota 2: ", notas_2[i];
		Escribir "Nota 3: ", notas_3[i];
		nota_promedio <- (notas_1[i]*0.3+notas_2[i]*0.3+notas_3[i]*0.4);
		Escribir "Nota definitiva: ", nota_definitiva;
		Si nota_definitiva >= aprobatoria Entonces
			aprobados = aprobados + 1
		SiNo
			reprobados = reprobados + 1
		FinSi;
		Escribir "______________________________________";
	FinPara
	Escribir "Aprobados: ", aprobados;
	Escribir "Reprobados: ", reprobados;
FinAlgoritmo