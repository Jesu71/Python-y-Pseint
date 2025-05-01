Algoritmo matriz
	Dimension Mat[3,3];
	Dimension Nom[3];
	Nom[1]<-"Juan";
	Nom[2]<-"Maria";
	Nom[3]<-"Luis";
	Definir i,j Como Entero
	Escribir "Ingresa los datos de la Matriz"
	Para i<-1 Hasta 3 con paso 1 Hacer
		para j<-1 Hasta 3 Con Paso 1 Hacer
			Escribir "Dijite la nota", j , " de ", Nom[1];
			Leer mat[i,j];
		FinPara
	FinPara
	Para i<-1 Hasta 3 con paso 1 Hacer
		para j<-1 Hasta 3 Con Paso 1 Hacer
			Escribir "Dijite la nota", j , " de ", Nom[2];
			Leer mat[i,j];
		FinPara
	FinPara
	Para i<-1 Hasta 3 con paso 1 Hacer
		para j<-1 Hasta 3 Con Paso 1 Hacer
			Escribir "Dijite la nota", j , " de ", Nom[3];
			Leer mat[i,j];
		FinPara
	FinPara
	Escribir "los valores son:";
	Para i<-1 Hasta 3 con paso 1 Hacer
		para j<-1 Hasta 3 Con Paso 1 Hacer
		Escribir mat[i,j];
		FinPara
	FinPara
FinAlgoritmo
