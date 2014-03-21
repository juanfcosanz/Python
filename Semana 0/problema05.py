print("Calcula Retiro Rapicash")
print("  Introduce loque se te pide: ")
retorix = float(input(" -> Efectivo a retirar: "))
n = int(input(" -> Numero de coutas: "))
i = float(input(" ->Tasa de interes Rapicash (mensual): "))
i = i /100

CuotaRapicash = retorix *  ((i  * ((1+i))**n)/ (((1+i)**n)-1))

print("\n Retiro en eefctivo Rapisach: ", CuotaRapicash)

MTI = (CuotaRapicash * 12) - retorix

print("\n Monto total de intereses : ",MTI)