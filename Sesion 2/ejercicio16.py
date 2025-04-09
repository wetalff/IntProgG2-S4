#Propina
total_cuenta = float(input("Dime de cuanto fue el total de la cuenta a pagar:"))
porcent_propina = float(input("Dime de cuanto es el porcentaje de propina:"))
Propina = total_cuenta * (porcent_propina / 100)
total_Pago = total_cuenta + Propina

print("La cantidad extra que debes de pagar de propina es de",Propina,"Y ya sumado con el total de la cuenta dada, deberias de pagar en total",total_Pago)


