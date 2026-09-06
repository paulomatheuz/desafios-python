# 14. Soma limitada e sucessora
# Escreva um algoritmo que leia números maiores que zero enquanto
# a soma deles não ultrapassar 10.
# Para cada número, escreva o seu sucessor.

soma_num = 0
num = float(input("Digite um número: "))

while num > 0 and soma_num + num <= 10:
    print(f"Número atual: {num}, sucessor: {num + 1}")
    soma_num += num

    num = float(input("Digite um número: "))

print(f"Soma final: {soma_num}")