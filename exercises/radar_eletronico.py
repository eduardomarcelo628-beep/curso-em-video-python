velocidade_carro = float(input("Qual é a velocidade do carro? "))

if velocidade_carro > 80:
    multa_velocidade = (velocidade_carro - 80) * 7

    print("\033[31mMULTADO! Você excedeu o limite da velocidade de 80 km/h!\033[m")
    print(f"\033[31mVocê deve pagar uma multa de \033[33mR${multa_velocidade:.2f}.\033[m")

print("\033[33mTenha um bom dia! Dirija com segurança.\033[m")
