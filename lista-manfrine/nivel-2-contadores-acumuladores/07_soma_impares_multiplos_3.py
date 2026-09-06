# 7. Soma de impares multiplos de tres
# Desenvolva um algoritmo que efetue a soma de todos os numeros impares que sao multiplos de tres e que se
# encontram no conjunto dos numeros de 1 ate 500.

soma_impares_multiplos_tres = 0

for i in range(501):
    if i % 2 == 1:
        if i % 3 == 0:
            soma_impares_multiplos_tres += i

print(f"A soma de todos os numeros impares entre 1 e 500 multiplos de 3 e: {soma_impares_multiplos_tres}")