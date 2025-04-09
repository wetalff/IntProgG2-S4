#Factura
Producto_1 = float(input("Dime el precio del primer producto:"))
Producto_2 = float(input("Dime el precio del segundo producto:"))
Producto_3 = float(input("Dime el precio del tercer producto:"))

IVA = 15 

subtotal = Producto_1 + Producto_2 + Producto_3

sub_IVA = subtotal * (15 / 100)

Total_a_pagar = subtotal + sub_IVA

print(f"El subtotal es de: {subtotal:<20}")
print(f"El monto de IVA a aplicar es de: {sub_IVA:<20}")
print(f"El monto total a pagar incluyendo el IVA es de: {Total_a_pagar:<20}")


