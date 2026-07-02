import random

alunos_lista = [input("Digite o primeiro aluno: "),
                     input("Digite o segundo aluno: "),
                     input("Digite o terceiro aluno: "),
                     input("Digite o quarto aluno: ")
                     ]

aluno_sorteado = random.choice(alunos_aleatorios)

print(f"O aluno sorteado foi: {aluno_sorteado}.")
