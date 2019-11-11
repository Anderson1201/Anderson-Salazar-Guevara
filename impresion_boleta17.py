#INPUT
supervisor=input("Nombre del suppervisor: ")
cliente=input("Nombre del cliente: ")
vendedor=input("Ingrese nombre del vendedor: ")
televisor=int(input("Ingrese numero de televisores: "))
p1=float(input("Ingrese precio unitario del televisor: "))
dvd=int(input("Ingrese numero de DVD: "))
p2=float(input("Ingrese precio unitario de dvd: "))

#PROCESSING
total=(televisor*p1)+(dvd*p2)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("######VENTA DE ARTEFACTOS#######")
print ("# SUPERVISOR:", supervisor)
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# TELEVISOR:", televisor)
print ("# P.U:", p1)
print ("# DVD:", dvd)
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("###GRACIAS POR LA PREDERENCIA###")
print ("##################################")
