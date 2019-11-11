#INPUT
alumno:input("Ingrese nombre del alumno: ")
peso=float(input("Ingrese el peso: "))
talla=float(input("Ingrese la talla: "))

#PROCESSING
indice=(peso+talla)/2

#OUTPUT
print ("#####################################")
print ("#CALCULAR EL INDICE DE MASA CORPORAL#")
print ("# PESO", peso)
print ("# TALLA:", talla)
print ("# INDICE DE MASA CORPORAL:", indice)
print ("#################################")
