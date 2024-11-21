# Desenvolva um programa que leia o primeiro termo e a razão de uma PA, no final mostre os 10 primeiros termos dessa progressão

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))

for c in range(primeiro, primeiro + 10 * razao, razao):
    print(c, end=" - ")
print("ACABOU!")
