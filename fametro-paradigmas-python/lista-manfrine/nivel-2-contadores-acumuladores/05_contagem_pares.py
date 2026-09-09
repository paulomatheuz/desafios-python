# 5. Contagem de numeros pares
# Faca um algoritmo para ler 6 numeros e escrever quantos deles sao pares.

contador = 0
for i in range(6):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        contador += 1

print(f"A quantidade de numeros pares e: {contador}")