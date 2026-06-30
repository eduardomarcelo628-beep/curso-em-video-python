import math

angulo_graus = float(input("Digite um ângulo qualquer: "))

angulo_radianos = math.radians(angulo_graus)

seno_angulo = math.sin(math.radians(angulo_graus))
cosseno_angulo = math.cos(math.radians(angulo_graus))

tangente_angulo = math.tan(math.radians(angulo_graus))

print(f"O ângulo de {angulo_graus}° tem o SENO de {seno_angulo:.2f}.")
print(f"O ângulo de {angulo_graus}° tem o COSSENO de {cosseno_angulo:.2f}.")
print(f"O ângulo de {angulo_graus}° tem a TANGENTE de {tangente_angulo:.2f}.")
