# 9. Maior e menor altura
# Desenvolva um algoritmo que leia a altura de 15 pessoas e mostre a menor e a maior altura do grupo.

altura = float(input("Digite a altura de uma pessoa: "))
maior_altura = altura
menor_altura = altura

for i in range(14):
    altura = float(input("Digite a altura de uma pessoa: "))
    
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

print(f"A maior altura do grupo e: {maior_altura}")
print(f"A menor altura do grupo e: {menor_altura}")