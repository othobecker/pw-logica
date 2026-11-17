# Idade = int(input("Sua idade: "))

# if Idade >= 18:

#     print("Você é maior de idade!")

   

# else:
#     print("Você é meenor de idade")











# nota =float(input("Sua nota: ").replace (".", "."))

# if nota >= 9.0:
#         print("Excelente!")

# elif nota >= 7.0:
#         print("Bom!")

# elif nota >= 5.0:
#         print("Regular")

# elif nota < 5.0:
#         print("Reprovado")








# nome = (input("Seu nome: "))

# peso = float(input("Seu peso em KG: "))

# altura = float(input("Sua altura: "))

# IMC = peso / (altura ** 2)

# if IMC <= 18.5:
#     print("Abaixo do peso")

# elif IMC <= 25:
#     print("Peso NORMAL")

# elif IMC <= 30:
#     print("Gordo")

# else:
#     print("Obesity") 












# Idade = int(input("Sua idade: "))

# if Idade <= 0:

#      print("Idade invalida")

# elif Idade <= 12:
     
#      print("Criança")

# elif Idade <= 17:

#     print("Adolescente")

# elif Idade <= 59:
     
#      print("Adulto")

# elif Idade <= 100:
     
#      print("Velho")


# else:
     
#      print("Pré-cadáver")
   






nome1 = (input("Jogador 1: "))

nome2 = (input("Jogador 2: "))

jogada = (input("Jogador 1, você quer par ou ímpar? "))

if jogada == "par":

    numeropar = int(input("Escolha um número: "))
    numeroimpar= int(input("Escolha um número: "))

if jogada == "ímpar":
    numeroimpar= int(input("Escolha um número: "))
    numeropar = int(input("Escolha um número: "))
    
    conta= numeropar + numeroimpar % 2 == 0 else "ímpar":

 print(f"{nome1} vence!")



    print(f"{nome2} vence!")

    if jogada== "ímpar" 
    numeropar + numeroimpar % 2 != 0:
 







 import random
print ("=" * 35)
print (" PEDRA, PAPEL OU TESOURA")
print("=" * 35)

opcoes = ["pedra", "papel" , "tesoura"]
computador = random.choice(opcoes)

Jogador = input ("\nEscolha (pedra/papel/tesoura): ").lower()

print(f"\nVocê: {Jogador}")
print(f"Computador: {computador}")

if Jogador == computador:
    print("\nEmpate!")
elif Jogador == "pedra" and computador == "tesoura":
    print("\nVocê ganhou!")
elif Jogador == "papel" and computador == "pedra":
     print("\nVocê ganhou!")
elif Jogador == computador:
     print("\nEmpate!")
elif Jogador == "tesoura" and computador == "papel":
     print("\nVocê ganhou!")
else:
    print("\nVocê empate!")