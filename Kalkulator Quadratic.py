
print('Kalkulator Persamaan Kuadrat ax+bx+c')

val_a = int(input("Masukan nilai a: "))
val_b = int(input("Masukan nilai b: "))
val_c = int(input("Masukan nilai c: "))

dscrmnt = (val_b**2) - (4 * val_a * val_c)
sqrt_discri = dscrmnt**0.5

print("Discriminant:", dscrmnt)

X1 = (-val_b + sqrt_discri) / (2 * val_a)
X2 = (-val_b - sqrt_discri) / (2 * val_a)
 
print(" X1 val =", X1)
print(" X2 val =", X2)

#-b+- sqrt(-b^2 - 4ac)/2a

