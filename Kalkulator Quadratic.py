
print('Quadratic Equation Calculator ax²+bx+c')

val_a = int(input("Insert a value: "))
val_b = int(input("Insert b value: "))
val_c = int(input("Insert c value: "))

dscrmnt = (val_b**2) - (4 * val_a * val_c)
sqrt_discri = dscrmnt**0.5

print("Discriminant:", dscrmnt)

X1 = (-val_b + sqrt_discri) / (2 * val_a)
X2 = (-val_b - sqrt_discri) / (2 * val_a)
 
print(" X1 val =", X1)
print(" X2 val =", X2)

#-b+- sqrt(-b^2 - 4ac)/2a

