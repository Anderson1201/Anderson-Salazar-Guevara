#INPUT
recepcionista=input("Nombre del recepecionista: ")
cliente=input("Nombre del cliente: ")
cuarto1=int(input("Ingrese numero de horas: "))
pu=float(input("Ingrese el precio por ahora: "))

#PROCESSING
total=(cuarto1*pu)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("###### HOTEL LA CASACADA #######")
print ("# CLIENTE:", cliente)
print ("# RECEPCIONISTA:", recepcionista)
print ("# HORAS DE CUARTO", cuarto1)
print ("# P.U:", pu)
print ("# TOTAL:", total)
print ("######### VUELVA PRONTO #########")
print ("##################################")
