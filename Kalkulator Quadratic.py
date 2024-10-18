
print('Quadratic Equation Calculator ax²+bx+c')

val_a = int(input("Insert a value: "))
val_b = int(input("Insert b value: "))
val_c = int(input("Insert c value: "))

dscrmnt = (val_b**2) - (4 * val_a * val_c)
sqrt_discri = dscrmnt**0.5

print("Discriminant:", dscrmnt)

X1 = (-val_b + sqrt_discri) / (2 * val_a)
X2 = (-val_b - sqrt_discri) / (2 * val_a)
 
resultX1 = str(X1)
resultX2 = str(X2)
resultX_1 = resultX1[0:4]
resultX_2 = resultX2[0:4]

print(" X1 val =", resultX_1)
print(" X2 val =", resultX_2)

#-b+- sqrt(-b^2 - 4ac)/2a

