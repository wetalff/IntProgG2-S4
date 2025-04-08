#algoritmo que intercambie el valor de dos variables numéricas. Usa una variable auxiliar para hacerlo.

a = int(input("Ingrese un numero para a:"))

b = int(input("Ingrese un numero para b:"))

Aux = a
a = b
b = Aux

print("Después del intercambio:")
print("a = ", a)
print("a = ", b)


