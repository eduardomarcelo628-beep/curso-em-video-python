largura_parede = float(input("Digite a largura da parede: "))
altura_parede = float(input("Digite a altura da parede: "))

dimensao_parede = largura_parede * altura_parede

quantidade_tinta = dimensao_parede / 2

print(f"Sua parede tem a dimensão de {largura_parede}x{altura_parede} e sua área é de {dimensao_parede}m².")
print(f"Para pintar essa parede, você precisará de {quantidade_tinta}l de tinta.")
