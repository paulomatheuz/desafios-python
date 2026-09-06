# 11. Quantidade de numeros positivos
# Faca um algoritmo que receba numeros enquanto eles forem positivos e, ao final, informe quantos numeros foram
# digitados.

numeros_digitados = 0
numero = int(input("Digite um numero: "))

while numero > 0:
    if numero > 0:
        numeros_digitados += 1

    numero = int(input("Digite um numero: "))

print(f"A quantidade de numeros positivos digitados foi de {numeros_digitados}")