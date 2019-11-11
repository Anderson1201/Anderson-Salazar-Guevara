#Calcular al area leteral del cilindro
area_lateral, pi, radio, generatriz=0.0, 0.0, 0, 0.0

#Asignacion de valores
pi=3.14
radio=3
generatriz=4.5

#Calculo
area_lateral=(pi*radio*generatriz)*2

#Mostrar valores
print ("pi", pi)
print ("radio", radio)
print ("generatriz", generatriz)
print ("area lateral del cilindro", area_lateral)


#Verificaciones
pi, radio, generatriz=3.14, 3, 4.5

#Calculo
suma=(pi+radio+generatriz)
a=(suma==13)
print ("la suma es:", a)
