# -*- coding: utf-8 -*-

def tramite(valorVenta,IGV,porcentaje,ope):
	if valorVenta > 700:
		IGV = IGV * valorVenta 

		precioVenta = valorVenta + IGV

		porcentaje = porcentaje * precioVenta

		if ope == "suma":
			cantidadGral =  precioVenta + porcentaje
		elif ope == "resta":
			cantidadGral =  precioVenta - porcentaje
	else:
		cantidadGral = "No se puede aplicar tramite !!"

	return cantidadGral

tipoTramite = int ( input(
"""  Que tipo de tramite desea realizar
		1) Percepcion
		2) Retencion
		3) Detraccion
		   Respuesta: """))  


if tipoTramite == 1:
	valorVenta = int (input ("\nCual fue el valor de la venta: "))
	IGV = int (input ("Ingrese el Impuesto General a las ventas (IGV): "))
	IGV = IGV / 100
	porcentaje = int( input ("Valor de la percepcion: "))
	porcentaje = porcentaje / 100
	ope = "suma"
	print("\n --> Cobrara P/. " ,tramite(valorVenta,IGV,porcentaje,ope))
elif tipoTramite == 2:
	valorVenta = int (input ("\nCual fue el valor de la venta: "))
	IGV = int (input ("Ingrese el Impuesto General a las ventas (IGV): "))
	IGV = IGV / 100
	porcentaje = int( input ("Valor de la retencion: "))
	porcentaje = porcentaje / 100
	ope = "resta"
	print("\n --> Pagara P/. " ,tramite(valorVenta,IGV,porcentaje,ope))
else:
	valorVenta = int (input ("\nCual fue el valor de la venta: "))
	IGV = int (input ("Ingrese el Impuesto General a las ventas (IGV): "))
	IGV = IGV / 100
	porcentaje = int( input ("Valor de la detraccion: "))
	porcentaje = porcentaje / 100
	ope = "resta"
	print("\n --> Depositara P/. " ,tramite(valorVenta,IGV,porcentaje,ope))

