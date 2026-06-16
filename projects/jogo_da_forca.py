import random
palavras_aleatorias = ["python", "computador", "desenvolvimento", "programacao", "teclado"] #palavras aleatórias

palavra_secreta = random.choice(palavras_aleatorias) #escolha das palavras

tentativas = 6  #tentativas do jogador

letras_tentadas = set()    #set usado para eliminar elementos duplicados.

print("Bem-vindo ao Jogo da Forca!")  #Menu inicial.

while tentativas > 0:

    palavra_mostrada = ""    #início do jogo.

    for letra in palavra_secreta:
        if letra in letras_tentadas:
            palavra_mostrada += letra + " "
        else:
            palavra_mostrada += "_ "

    print("Palavra:", palavra_mostrada)

    if "_" not in palavra_mostrada:        #quando o jogador vence o jogo.
        print("Parabéns! Você venceu o jogo! :D")
        break

    tentativa = input("Digite uma letra: ").lower()    #recebe as letras tentadas.

    if len(tentativa) != 1:     #se o usuário tentar mais de uma letra.
        print("Digite apenas uma letra!")
        continue

    if tentativa in letras_tentadas:   #letras já tentadas pelo usuário
        print("Você já tentou essa letra!")
        continue

    letras_tentadas.add(tentativa)

    if tentativa in palavra_secreta:  #usuário acerta uma letra
        print("Letra correta!")
    else:
        tentativas -= 1
        print("Letra incorreta! Tente novamente.")   #usuário erra uma letra
        print("Tentativas restantes:", tentativas)

if tentativas == 0:     #usuário perde o jogo.
    print("Você perdeu o jogo!")
    print("A palavra correta era:", palavra_secreta)    #revelação da palavra secreta
