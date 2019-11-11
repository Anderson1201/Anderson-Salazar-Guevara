#INPUT
vendedor=input("Nombre del vendedor: ")
cliente=input("Nombre del cliente: ")
llantas=int(input("Ingrese numero de llantas: "))
p1=float(input("Ingrese precio unitario de llanta: "))
faros=int(input("Ingrese numero de faros: "))
p2=float(input("Ingrese precio unitario de faros: "))

#PROCESSING
total=(llantas*p1)+(faros*p2)

#OUTPUT
print ("#################################")
print ("# VENTA DE ACCESORIOS PARA CARRO #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# Llantas", llantas)
print ("# P.U:", p1)
print ("# FAROS:", faros)
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("##################################")
