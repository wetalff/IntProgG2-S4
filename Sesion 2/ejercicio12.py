#Pago de interes

Prestamo = 10000
interes = 27
tiempo_años = int(input("Dime el tiempo en años que durara el prestamo:"))
pagoTotal = Prestamo * (1 + (interes * tiempo_años /100))
print("La cantidad final que se va a pagar por los", Prestamo,"por el tiempo de",tiempo_años,"años, y con un interes del",interes,"porciento es de:",pagoTotal)
