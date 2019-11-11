#Calcular la velocidad final de un cuerpo
velocidad_final, velocidad_inicial, gravedad, tiempo=0.0, 0.0, 0.0, 0.0

#Asignacion de valores
velocidad_inicial=10
gravedad=9.8
tiempo=20

#Calculo
velocidad_final=(gravedad*tiempo)+velocidad_inicial

#Mostrar valores
print ("velocidad inicial", velocidad_inicial)
print ("gravedad", gravedad)
print ("tiempo", tiempo)
print ("velocidad final", velocidad_final)


#Verificaciones
velocidad_inicial, gravedad, tiempo=10, 9.8, 20

#Calculo
suma=(velocidad_final+gravedad+tiempo)
a=(suma<40)
print ("la sumatoria es:", a)
