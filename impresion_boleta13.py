#INPUT
masa=float(input("Ingrese numero de masa: "))
velocidadluz=float(input("Ingrese numero de velocidad de la luz: "))
velocidadsol=float(input("Ingrese numero de velocidad del sol: "))

#PROCESSING
area=(masa*velocidadluz*velocidadsol)

#OUTPUT
print ("################################")
print ("# CALCULAR LA ENERGIA #")
print ("# MASA", masa)
print ("# VELCCIDAD DE LA LUZ:", velocidadluz)
print ("# VELOCIDAD DEL SOL:", velocidadsol)
print ("# EL AREA DEL CIRCULO ES:", area)
print ("#################################")
