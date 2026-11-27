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

# import random
# numerosecreto = random.randiant(1, 20)
# tentativas = 0
# palpite = int(input("Tente adivinhar um número entre 1 e 20:"))

# while palpite != numerosecreto:
#     tentativas += 1
#     if palpite < numerosecreto:
#         print("O número secreto é maior!")
#     else:
#         print("O numero secreto é menor!")
#         palpite = int(input("Tente novamente: "))
# tentativas += 1
# print("Parabéns! Você acertou!")
# print(f"Você utilizou {tentativas} tentativas.")






# nome = int(input("Seu nome: "))
# peso = int (input("Seu peso em KG"))
# altura = int(input("Sua altura em metros"))

# resultado = peso / (altura ** 2)

# print(f"Olá {nome} seu IMC é de {resultado}")





# quantia = 0
# total = 0

# preco = float(input("Digite o preço do produto: \n"
#                     "(Digite 0 para encerrar) \n"
#                     "R$"))

# while preco != 0:
#     total += preco
#     quantia += 1

# preco = float(input("Digite o preço do próximo produto: \n"
#                     "(Digite 0 para encerrar) \n"
#                     "R$"))

# print(f"Total da compra: R$ {total:.2f}")
# print(f"Quantidade de produtos: {quantia}")











# filmes = ["Divertidamente", "Era do gelo",
#           "Gente Grande", "Toy Sotry",
#           "Harry Potter"
#           ]

# print("Lista completa de filmes: \n {filmes}")
# print(f"\nO Primeiro filme é {filmes[0]}")
# print(f"\nO último filme é {filmes[4]}")
# print(f"\nQuantidade de filmes: {len(filmes)}")
      
                

# compras = ["Batata frita da playstation",
#             "Amaciante", "Cubo de chocolate"
#             ]


# compras.append("Mac n' Cheese")
# compras.append("Café")

# print(compras)





# alunos = ["Lucas", "Otho", "Rafael"]

# contador = 0
# for aluno in alunos:
#     print(f"Aluno: {contador} : {aluno}")

#     contador += 1







nota1 = int(input("Digite a primeira nota: "))

nota2 = int(input("Digite a segunda nota: "))

nota3 = int(input("Digite a terceira nota: "))

nota4 = int(input("Digite a quarta nota: "))

nota5 = int(input("Digite a última nota: "))

notas = [nota1, nota2, nota3, nota4, nota5]

soma = nota1 + nota2 + nota3 + nota4 + nota5

media = soma / 5

print(f"A soma de suas notas é: {soma}")

print(f"A sua média é: {media}")

print("A sua maior nota é:", max(notas))

print("A sua menor nota é:", min(notas))

