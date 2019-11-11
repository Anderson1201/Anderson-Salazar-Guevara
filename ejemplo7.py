#Calcular el area lateral del tronco de cono de revolucion
area_lateral, pi, radio_mayor, radio_menor, generatriz=0.0, 0.0, 0, 0, 0.0

#Asignacion de valores
pi=3.14
radio_mayor=5
radio_menor=3
generatriz=6.1

#Calculo
area_lateral=(radio_mayor+radio_menor)*generatriz*pi

#Mostrar valores
print ("pi", pi)
print ("radio mayor", radio_mayor)
print ("radio menor", radio_menor)
print ("generatriz", generatriz)
print ("el area lateral del tronco de cono", area_lateral)


#Verificaciones
pi, radio_mayor, radio_menor, generatriz=3.14, 5, 3, 6.1

#Calculo
suma=(pi+radio_menor+radio_mayor+generatriz)
a=(suma<20)
print ("la suma es:", a)
