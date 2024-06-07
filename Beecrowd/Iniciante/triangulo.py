entradas = []

entradas = input()

A = float(entradas.split()[0])
B = float(entradas.split()[1])
C = float(entradas.split()[2])

if A >= B + C or B >= A + C or C >= A + B:
    area = ((A + B)*C) / 2
    print(f'Area = {area:.1f}')
else: 
    peri = A + B + C
    print(f'Perimetro = {peri:.1f}')