#INPUT
cliente=input("Ingrese el nombre del cliente:")
arroz=int(input("Ingrese Nr de arroz con pato:"))
p1=float(input("Ingrese precio unitario:"))
postre=int(input("Ingrese el numero de postres:"))
p2=float(input("Ingrese precio unitario"))

# PROCESSING
total = (arroz*p1)+(postre*p2)

# OUTPUT
print ("#######################")
print ("# BOLETA DE VENTA")
print ("#######################")
print ("#")
print ("# Cliente:  ", cliente)
print ("#                    Nro")
print ("# Arroz con Pato:    ", arroz)
print ("# P.U:", p1)
print ("# Gelatina:   ",        postre)
print ("# P.U:", p2)
print ("# Total  :  S/.", total)
print ("#######################")
