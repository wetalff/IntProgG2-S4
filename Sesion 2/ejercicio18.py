#Ponderaciones

Tareas = float(input("Dime la calificacion de tus tareas: "))
Examen_parcial = float(input("Dime la calificacion de tu examen parcial: "))
Examen_Final = float(input("Dime la calificacion de tu examen final: "))

Calificacion_final = ((Tareas * 0.30) + (Examen_parcial * 0.30) + (Examen_Final * 0.40))
print(f"Tu calificacion final tomando en cuenta que las tareas valian un 30% el examen parcial otro 30% y el examen final un 40% es de: {Calificacion_final:.2f}")
