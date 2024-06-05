peso = float(input("Qual é o peso total de peixes pescado (kg)? "))
éMenor : bool = (peso <= 50)

print(f"O peso total pescado foi de {peso} kg de peixes.")

if éMenor:
  print("Tudo certo, não precisa pagar multa")
else:
  excesso = peso - 50
  multa = excesso * 4
  print(f"Você excedeu {excesso} kg de peixe, e por isso terá que pagar uma multa de R${multa:.2f}.")