#Salario
nombre = input("Dime el nombre del trabajador: ")
horasTrabajadas = float(input("Dime la cantidad de horas trabajadas por el trabajador: "))
Precio_hora = float(input("Dime cuanto cobra el trabajador por hora: "))
sueldo_bruto = horasTrabajadas * Precio_hora
Descuento_renta = sueldo_bruto * 0.05
Salario_a_pagar = sueldo_bruto - Descuento_renta

print(f"Nombre del trabajador: {nombre:>10}")
print(f"Sueldo Bruto: {sueldo_bruto:>10}")
print(f"Descuento del impuesto sobre la renta del 5%: {Descuento_renta:>10}")
print(f"Salario a pagar: {Salario_a_pagar:>10}")


