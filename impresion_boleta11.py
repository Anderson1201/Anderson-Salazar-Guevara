#INPUT
vendedor=input("Nombre del vendedor: ")
cliente=input("Nombre del cliente: ")
celular=int(input("Ingrese numero de celulares vendidos: "))
pu=float(input("Ingrese el costo de celular: "))

#PROCESSING
total=(celular*pu)

#OUTPUT
print ("#################################")
print ("# VENTA DE ACCESORIOS PARA CARRO #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# CELULAR", celular)
print ("# P.U:", pu)
print ("# TOTAL:", total)
print ("##################################")
