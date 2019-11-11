#INPUT
cliente=input("Ingrese el nombre del cliente:")
kg=int(input("Ingrese Nr Kg de mandarina:"))
pu=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (pu * kg)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",kg,"  kg Fresa")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")
