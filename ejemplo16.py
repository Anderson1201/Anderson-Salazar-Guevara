#Calcular el lado recto de una elipse
lado_recto, eje_menor, eje_mayor=0.0, 0, 0

#Asignacion de valores
eje_menor=6
eje_mayor=2

#Calculo
lado_recto=(2*eje_menor)/eje_mayor

#Mostrar valores
print ("eje menor", eje_menor)
print ("eje mayor", eje_mayor)
print ("lado recto de la elipse", lado_recto)


#Verificaciones
eje_mayor, eje_menor=2, 6

#Calculo
suma=(eje_menor+eje_mayor)
a=(suma==8)
print ("la sumatoria es:", a)
