#Algoritmo para calcular el porcentaje de mujeres y varones en un aula.
totalPersonas = int(input("Dime la cantidad total de personas en el aula:"))
total_varones = int(input("Dime la cantidad total de varones en el aula:"))
total_mujeres = int(input("Dime la cantidad total de mujeres en el aula:"))
porcentVarones = total_varones / totalPersonas * 100
porcentMujeres = total_mujeres / totalPersonas * 100
print("El porcentaje de hombres en el aula es del",porcentVarones,"% y del de mujeres es del",porcentMujeres,"%.")
