#INPUT
alumno=input("Ingrese nombre del alumno: ")
docente=input("Nombre del Docente: ")
grado=int(input("Ingrese el grado de estudios: "))
seccion=input("Ingrese la seccion: ")
nota1=float(input("Ingrese nota de Ingles: "))
nota2=float(input("Ingrese nota de Arte: "))
nota3=float(input("Ingrese nota de Comunicacion: "))

#PROCCESING
promedio=(nota1+nota2+nota3)/3

#OUTPUT
print ("###########################")
print ("#    BOLETA DE NOTAS     ##")
print ("# ALUMNO:", alumno)
print ("# DOCENTE:", docente)
print ("# GRADO:", grado,     "SECCION:", seccion)
print ("PROMEDIO FINAL:", promedio)
