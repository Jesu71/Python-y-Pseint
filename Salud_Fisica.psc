SubProceso Peso_Ideal (Peso_Actual, Sex, Est, Nombre)
	Definir PesoI Como Real;
	Definir Direfencia Como Real;
	SI (Sex="M" o Sex ="m") Entonces 
	    PesoI=(Est-100)*0.95;
	FinSi
	SI (Sex="F" o Sex ="f") Entonces 
	    PesoI=(Est-100)*0.85;
	FinSi
	Escribir "Hola ", Nombre ," Tu Peso Ideal es : ", Pesoi , " Kilos";
	si(Peso_Actual=PesoI)
		Escribir "Felicitaciones Tienes un Peso Ideal ";    	
	FinSi
	si(Peso_Actual>PesoI)
		Escribir "Actualmente te encuentras por encima del peso Ideal por ", (Peso_Actual-PesoI) , " Kilos";    	
	FinSi
	si(Peso_Actual<PesoI)
		Escribir "Actualmente te encuentras por debajo del peso Ideal por ", (PesoI-Peso_Actual) , " Kilos";    	
	FinSi
FinSubProceso
Proceso Salud_Fisica
	Definir Nombre,Sex Como Caracter;
	Definir Estatura, Peso_Actual Como Real;
	Escribir "Bienvenidos a su programa de Salud Personal";
	Escribir "Ingresa tu Nombre";
	Leer Nombre;
	Escribir "Digita tu peso Actual";
	Leer Peso_Actual;
	Escribir "Digita tu estatura";
	Leer Estatura;
	Escribir "Digita tu sexo  M o F";
	Leer Sex;
	Peso_Ideal(Peso_Actual,sex,Estatura,Nombre);
	Repetir
		Escribir "Digita tu sexo  M o F";
		Leer Sex;
		Si(Sex<>"M" o Sex <> "m" o Sex <> "F" o Sex <> "f") Entonces
			Escribir "Opcion no Valida";
		FinSi
 	Hasta Que Sex = "M" o Sex = "m" o Sex = "F" o Sex = "f"
	Peso_Ideal(Peso_Actual,sex,Estatura,Nombre);
FinProceso