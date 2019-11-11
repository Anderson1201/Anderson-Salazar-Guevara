#INPUT
masa=float(input("Ingrese numero de masa: "))
gravedad=float(input("Ingrese numero de la gravedad: "))
altura=int(input("Ingrese numero de la altura: "))

#PROCESSING
energia_cinetica=(masa*gravedad*altura)

#OUTPUT
print ("###############################")
print ("## CALCULAR ENERGIS CINETICA ##")
print ("# MASA:", masa)
print ("# GRAVEDAD:", gravedad)
print ("# ALTURA:", altura)
print ("# ENERGIA CINETICA:", energia_cinetica)
print ("################################")
