#Presupuesto
Monto_Presupuestal = float(input("Ingrese la cantidad del monto presupuestal destinada al hospital: "))
Urgencias = Monto_Presupuestal * (37 / 100)
Pediatria = Monto_Presupuestal * (42 / 100)
Traumatologia = Monto_Presupuestal * (21 / 100)

print(f"El presupuesto asignado para el area de urgencias es de {Urgencias:.2f}")
print(f"El presupuesto asignado para el area de pediatria es de {Pediatria:.2f}")
print(f"El presupuesto asignado para el area de traumatologia es de {Traumatologia:.2f}")


    
 