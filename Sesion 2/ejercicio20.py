#Masa
Presion = float(input("Ingrese la presion del objeto: "))
volumen = float(input("Ingrese el volumen del objeto: "))
temperatura = float(input("ingrese la temperatura del objeto: "))

masa = (Presion * volumen) / (0.37 * (temperatura + 460))
print(f"La masa del objeto es de: {masa:.2f}")



