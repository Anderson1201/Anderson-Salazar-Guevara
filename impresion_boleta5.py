#INPUT
cliente=input("Inhrese nombre del cliente: ")
vendedor=input("Ingrese nombre del vendedor: ")
tortas=int(input("Ingrese la cantidad de tortas: "))
pu=float(input("Ingrese precio unitario: "))

#PROCESING
total=(tortas*pu)

#OUTPUT
print ("###############################")
print ("##     BOLETA ELECTRONICA    ##")
print ("#        PASTELERIA           #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# FECHA: 09/11/2019    Hora: 17:27p.m")
print ("# TORTAS:", tortas,)
print ("# P.U:",    pu)
print ("# TOTAL:",   total)
print ("####  GRACIAS POR SU COMPRA  ###")
print ("################################")


