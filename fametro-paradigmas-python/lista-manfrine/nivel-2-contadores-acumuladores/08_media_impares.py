# 8. Media dos numeros impares
# Faca um algoritmo para ler 6 numeros e escrever a media somente dos numeros que sao impares.

quantidade_impares = 0
soma_impares = 0

for i in range(6):
    num = int(input("Digite um numero: "))
    if num % 2 == 1:
        soma_impares += num
        quantidade_impares += 1

if quantidade_impares > 0:
    media_final = soma_impares / quantidade_impares
    print(f"A media dos numeros impares e: {media_final}")
else:
    print("Sem numeros impares")