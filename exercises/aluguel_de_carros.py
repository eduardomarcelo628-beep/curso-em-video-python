carro_diaria = int(input("Informe os dias alugados: "))
km_percorrido = float(input("Informe os Km rodados: "))

valor_diaria = 60
valor_kms = 0.15

total_aluguel = (valor_diaria * carro_diaria) + (valor_kms * km_percorrido)

print(f"O total a pagar é: R${total_aluguel:.2f}")
