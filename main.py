# import pygame
# pygame.init()

# LARGURA = 600
# ALTURA = 400

# tela = pygame.display.set_mode((LARGURA, ALTURA))
# pygame.display.set_caption("Space invaders")

# FUNDO = (0, 0, 0)
# VERDE = (100, 255, 100)
# TAMNHO_PIXEL = 20





# anos = int(input("Sua idade: "))
# if anos >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade. sair")







# notas = int(input("Digite sua nota: "))
# if notas == 10.0:
#     print("Nota máxima")
# elif notas != 0:
#     print("A nota é diferente de zero")
# elif notas >= 7.0:
#     print("Passou de ano")
# else:
#     print("Rodou de ano")








# numero = int(input("Digite um número: "))

# for i in range(1, numero +1):
#     print(i)






# senhacerta = 29102010

# senha = int(input("Digite sua senha:"))

# while senha != senhacerta:
#     print("Tente novamente")
#     senha = int(input("Digite sua senha:"))

# print("Bem vindo!")

import random
numerosecreto = random.randiant(1, 20)
tentativas = 0
palpite = int(input("Tente adivinhar um número entre 1 e 20:"))

while palpite != numerosecreto:
    tentativas += 1
    if palpite < numerosecreto:
        print("O número secreto é maior!")
    else:
        print("O numero secreto é menor!")
        palpite = int(input("Tente novamente: "))
tentativas += 1