import math

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hipotenusa_calculo = math.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa_calculo:.2f}")
