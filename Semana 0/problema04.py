print("Programa para Obtener la Couta de una compra y el Monto Total de Interes")
print("   Introduce los valores correspondientes: ")
C = float(input(" -> Costo de la compra: "))
i =  float(input(" -> Tasa de Interes mensual (%): "))
i = i /100
n = int(input(" -> Numero de Mensualidades para pagar: "))

VC = C * (i *((1 + i) ** n)/((1 + i) ** n - 1))

print("\nLa Cuota total de la compra es: ", VC)

MTI = (VC * n) - C
print("\nEL Monto total de Intereses es: ", MTI)