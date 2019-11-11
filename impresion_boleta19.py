#INPUT
cliente=input("Nombre del cliente: ")
vendedor=input("Ingrese nombre del vendedor: ")
cerveza1=int(input("Ingrese numero de cajas de cerveza cristal: "))
p1=float(input("Ingrese precio unitario del cristal: "))
cerveza2=int(input("Ingrese numero de cajas de cerveza trigo: "))
p2=float(input("Ingrese precio unitario de trigo "))

#PROCESSING
total=(cerveza1*p1)+(cerveza2*p2)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("### DISTRIBUIDOR DE CERVEZA ####")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# CERVEZA CRISTAL:", cerveza1, "cajas")
print ("# P.U:", p1)
print ("# CERVEZA TRIGO:", cerveza2, "cajas")
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("###GRACIAS POR LA PREDERENCIA###")
print ("##################################")
