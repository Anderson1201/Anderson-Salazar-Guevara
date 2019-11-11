#INPUT
laboratorio=input("Ingrese nombre de laboratorio: ")
docente=input("Ingrese nombre del docente encargado: ")
computadoras=int(input("Ingrese el total de computadoras: "))
mouse=int(input("Ingrese toal de mouse: "))
cpu=int(input("Ingrese el total de cpu: "))
#PROCESING
total=(computadoras+mouse+cpu)

#OUTPUT
print ("###############################")
print ("## INVENTARIO DE LABORATORIO ##")
print ("# NOMBRE DEL LABORATORIO:", laboratorio)
print ("# DOCENTE:", docente)
print ("# FECHA: 12/11/2019    Hora: 9:27a.m")
print ("# COMPUTADORAS:", computadoras)
print ("# MOSUES:", mouse)
print ("# CPU:", cpu)
print ("#TOTAL DE ACCESORIOS:", total)
print ("################################")
