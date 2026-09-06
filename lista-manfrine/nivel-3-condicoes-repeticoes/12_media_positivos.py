# 12. Média de números positivos
# Faça um algoritmo que receba números positivos e, ao final, imprima a média dos números informados.

qtd_num = 0
soma_numeros = 0

num = float(input("Digite um número: "))

while num > 0:
    qtd_num += 1
    soma_numeros += num

    num = float(input("Digite um número: "))

if qtd_num > 0:
    media_num = soma_numeros / qtd_num
    print(f"A média dos números informados é: {media_num}")
else:
    print("Nenhum número positivo foi informado.")