#INPUT
alumno=input("Nombre del alumno: ")
facultad=input("Nombre de facultad: ")
ciclo=str(input("Ingrese ciclo academico: "))
anio=int(input("Ingrese numero del año: "))
nrocursos=int(input("Ingrese numero de cursos: "))
puntaje=float(input("Ingrese numero del puntaje total: "))
#PROCESSING
ponderado=(puntaje)/(nrocursos)

#OUTPUT
print ("#################################")
print ("#### CALCULAR EL PONDERADO ####")
print ("# ALUMNO:", alumno)
print ("# FACULTAD:", facultad)
print ("# CICLO ACADEMICO", ciclo)
print ("# AÑO:", anio)
print ("# NUMERO DE CURSOS:", nrocursos)
print ("# PUNTAJE FINAL:", puntaje)
print ("# PONDERADO:", ponderado)
print ("##################################")
