# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa, mostre:
# A média de idade do grupo
# qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 a anos


soma_idades = 0
homem_mais_velho = ""
idade_homem_mais_velho = -1  
mulheres_menores_20 = 0

for i in range(1, 5):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()

    soma_idades += idade

    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres_menores_20 += 1

media_idade = soma_idades / 4

print(f"\nA média de idade do grupo é: {media_idade:.2f} anos.")
print(f"O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.")
print(f"Existem {mulheres_menores_20} mulheres com menos de 20 anos.")
