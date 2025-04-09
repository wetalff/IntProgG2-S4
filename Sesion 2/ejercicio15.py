#Total a pagar por un producto
nombreProducto = input("Dime el nombre del producto a comprar:")
precioProducto = float(input("Dime el precio del producto:"))
porcentajeDesc = float(input("Dime el porcentaje de descuento que se va a aplicar al producto:"))
precioDesc = precioProducto * porcentajeDesc / 100
precioFinal = precioProducto - precioDesc

print(f"nombre del producto: {nombreProducto:>15}")
print(f"Precio final con descuento: {precioFinal:>9}")



                       
                       