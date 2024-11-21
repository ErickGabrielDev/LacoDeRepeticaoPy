# Faça um programa que leia o peso de cinco pessoas e no final mostre qual foi o maior e o menor peso lidos

maior_peso = float('-inf')  
menor_peso = float('inf')  

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (kg): "))
    
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f"\nO maior peso registrado foi: {maior_peso} kg")
print(f"O menor peso registrado foi: {menor_peso} kg")