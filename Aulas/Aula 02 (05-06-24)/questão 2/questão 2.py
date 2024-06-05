ganhoHora = float(input("Quanto você ganha por hora? "))
hora = float(input("Quantas horas você trabalha por mês? "))

salBruto = ganhoHora * hora

# impostos
INSS = salBruto*(11/100)
sind = salBruto*(5/100)

# salário líquido
salLiq = salBruto - INSS - sind

print(f"""
Seu salário bruto é de R${salBruto:,.2f}.
Você pagou ao INSS um total de R${INSS:,.2f}.
Você pagou ao sind um total de R${sind:,.2f}.
Seu salário líquido é de R${salLiq:,.2f}.
""")