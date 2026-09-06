# 13. Dobro dos números com valor sentinela
# Escreva um algoritmo que leia números e imprima o dobro de cada número.
# O algoritmo deverá encerrar quando o usuário informar -99.

num = float(input("Digite um número: "))

while num != -99:
    dobro_num = num * 2
    print(f"O dobro de {num} é: {dobro_num}")

    num = float(input("Digite um número: "))