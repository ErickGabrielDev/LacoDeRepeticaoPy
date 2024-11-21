# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares, se o valor for impar, desconsidere-o

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1 
print(f"Você informou {cont} Números PARES e a soma entre eles é: {soma}")