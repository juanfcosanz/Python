print("Valor Cuota de los rpimox 36 meses")

TEA = 11.49 / 100
CA = 12
ID = S1 = 12000.00
TSDI = 0.050 / 100
periodo = 31
TVA = 5.23 / 100
VV = 15000.00
FC = 6000.00
cuotas  = 37
portes = 3.80

print("\n  -> Calcular la tasa de interes")

TNA = (((1+TEA) ** (1/CA)) - 1)  * ((CA * 365) / 360)
#print("   *** Calculando la Tasa Efectiva Anual =  %.4f" %(TNA))
i = (TNA * periodo) / 365 
#print("   *** Calculando la Tasa Ajustada al Plazo(i) = %.4f" %(i))
interes = S1 * i
print("   *** Calculando el Interes del Primer Mes = %.2f" %(interes))

print("\n  -> Calculo del Seguro de Desagravamen")

TDA = TSDI  * CA
#print("   *** Calculando la Tasa de Seguro de Desgravamen Anual = %.4f" %(TDA))
d = (TDA * periodo) / 365
#print("   *** Calculando la Tasa de Seguro de Desgravamen Ajustada al Plazo = %.5f" %(d))
seguroDesgravamen = S1 * d
print("   *** Calculando Seguro de Desgravamen  = %.2f" %(seguroDesgravamen))
print("\n  -> Calculo del Seguro Vehicular")
n = (TVA * periodo) / 365
#print("   *** Calculando Tasa de Seguro Vehicular Ajustada al Plazo(n)  = %.4f" %(n))
seguroVehivular = VV * n
print("   *** Calculando Tasa de Seguro Vehicular Mensual  = %.2f" %(seguroVehivular))
print("\n  -> Amortizacion")

amortizacion = FC / cuotas

print("   *** Calculando Tasa de Seguro Vehicular  = %.2f" %(amortizacion))

cuotaTotal = interes + seguroDesgravamen + seguroVehivular + amortizacion + portes

print("\n  -> Pago total a pagar %.2f"  %(cuotaTotal))