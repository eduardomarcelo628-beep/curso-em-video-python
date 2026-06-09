dinheiro_reais = float(input("Olá! Qual é o valor disponível em sua carteira?: R$"))   

dinheiro_dolar = dinheiro_reais / 5.20   #realiza a conversão para o dolar, que atualmente equivale US$5.20

print(f"Com R${dinheiro_reais} você pode comprar US${dinheiro_dolar:.2f}")
