#INPUT
cliente=input("Nombre del cliente: ")
vendedor=input("Ingrese nombre del vendedor: ")
mesas=int(input("Ingrese numero de mesas: "))
p1=float(input("Ingrese precio unitario de cada mesa: "))
sillas=int(input("Ingrese numero de sillas: "))
p2=float(input("Ingrese precio unitario de cada silla: "))

#PROCESSING
total=(mesas*p1)+(sillas*p2)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("###### MADERERA MI ROSITA ######")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# MESAS:", mesas)
print ("# P.U:", p1)
print ("# SILLAS:", sillas)
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("##################################")
