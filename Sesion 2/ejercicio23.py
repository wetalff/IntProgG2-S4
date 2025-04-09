#Recorrido
Lunes = float(input("Dime en minutos cuanto te tardaste en recorrer la ruta el lunes: "))
Miercoles = float(input("Dime en minutos cuanto te tardaste en recorrer la ruta el miercoles: "))
Viernes = float(input("Dime en minutos cuanto te tardaste en recorrer la ruta el viernes: "))
promedio_recorrido = (Lunes + Miercoles + Viernes) / 3
print(f"En una semana te tardaste en recorrer esa ruta un promedio de: {promedio_recorrido:.2f} minutos")

