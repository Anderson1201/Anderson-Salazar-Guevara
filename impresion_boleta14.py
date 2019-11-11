#INPUT
mesero=input("Nombre del mesero: ")
cliente=input("Nombre del cliente: ")
cabrito=int(input("Ingrese numero de platos de cabrito: "))
p1=float(input("Ingrese precio de cada plato de cabrito: "))
cebada=int(input("Ingrese el numero de cebadas: "))
p2=float(input("Ingrese precio unitario de cebada: "))

#PROCESSING
total=(cabrito*p1)+(cebada*p2)

#OUTPUT
print ("#################################")
print ("##### RESTAURANT EL CHOLITO #####")
print ("# CLIENTE:", cliente)
print ("# MESERO:", mesero)
print ("# CABRITO", cabrito)
print ("# P.U:", p1)
print ("# CEBADA:", cebada)
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("##################################")
