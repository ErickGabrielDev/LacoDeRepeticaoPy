# crie um programa que leia o ano de nascimenrto de sete pessoas, no final mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores

menores_de_idade = 0
maiores_de_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    
    idade = 2024 - ano_nascimento  
    
    if idade < 18:
        menores_de_idade += 1
    else:
        maiores_de_idade += 1

print(f"\nTotal de pessoas menores de idade: {menores_de_idade}")
print(f"Total de pessoas maiores de idade: {maiores_de_idade}")
