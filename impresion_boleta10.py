#INPUT
vendedor=input("Nombre del vendedor: ")
cliente=input("Nombre del cliente: ")
pastel1=int(input("Ingrese numero de torta tres leches: "))
p1=float(input("Ingrese precio unitario: "))
pastel2=int(input("Ingrese numero de torta de chocolate: "))
p2=float(input("Ingrese precio unitario: "))
pastel3=int(input("Ingrese numero de Pai de manzana: "))
p3=float(input("Ingrese precio unitario: "))

#PROCESSING
total=(pastel1*p1)+(pastel2*p2)+(pastel3*p3)

#OUTPUT
print ("#################################")
print ("####   BOLETA ELECTRONICA   ####")
print ("####  PASTELERIA RICO SABOR  ####")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# TORTA TRES LECHES:", pastel1)
print ("# P.U:", p1)
print ("# TORTA DE CHOCOLATE:", pastel2)
print ("# P.U:", p2)
print ("# PAI DE MANZANA:", pastel3)
print ("# P.U:", p3)
print ("# TOTAL:", total)
print ("##### GRACIAS POR SU COMPRA #####")
print ("#################################")
