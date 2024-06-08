from math import sqrt

entradas = input()

a = float(entradas.split()[0])
b = float(entradas.split()[1])
c = float(entradas.split()[2])

delta = pow(b, 2) - (4*a*c)

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    R1 = (-b + sqrt(delta))/(2*a)
    R2 = (-b - sqrt(delta))/(2*a)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')

