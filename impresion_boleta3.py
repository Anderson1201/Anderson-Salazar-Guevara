#INPUT
cliente=input("Inhrese nombre del cliente:")
vendedor=input("Ingrese nombre del vendedor:")
clavos=int(input("Ingrese la cantidad de clavos"))
pu=float(input("Ingrese precio unitario"))

#PROCESING
total=(clavos*pu)

#OUTPUT
print ("###############################")
print ("##     BOLETA ELECTRONICA    ##")
print ("#      FERRETERIA OFERTON     #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# FECHA: 08/11/2019    Hora: 9:27a.m")
print ("# CLAVOS:", clavos, "docenas")
print ("# P.U:",    pu)
print ("# TOTAL:",   total)
print ("####  GRACIAS POR SU COMPRA  ###")
print ("################################")
