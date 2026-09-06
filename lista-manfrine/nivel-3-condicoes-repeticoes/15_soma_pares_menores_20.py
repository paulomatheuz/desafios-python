# 15. Soma dos números pares menores que 20
# Escreva um algoritmo que leia números menores que 20
# e imprima a soma somente dos números pares.

num = int(input("Digite um número: "))
soma_pares = 0

while num < 20:
    if num % 2 == 0:
        soma_pares += num

    num = int(input("Digite um número: "))

print(f"A soma dos números pares é: {soma_pares}")