# 16. Estatísticas de valores
# Leia uma quantidade indeterminada de valores e calcule:
# a média aritmética; a quantidade de valores positivos e negativos;
# e o percentual de valores positivos e negativos.

soma_valores = 0
qtd_valores = 0

qtd_positivos = 0
qtd_negativos = 0

valor = float(input("Digite um valor (0 para encerrar): "))

while valor != 0:
    soma_valores += valor
    qtd_valores += 1

    if valor > 0:
        qtd_positivos += 1
    elif valor < 0:
        qtd_negativos += 1

    valor = float(input("Digite um valor (0 para encerrar): "))

if qtd_valores > 0:
    media_aritmetica = soma_valores / qtd_valores

    perc_positivos = (qtd_positivos / qtd_valores) * 100
    perc_negativos = (qtd_negativos / qtd_valores) * 100

    print(f"Média aritmética: {media_aritmetica:.2f}")
    print(f"Quantidade de positivos: {qtd_positivos} | Quantidade de negativos: {qtd_negativos}")
    print(f"Percentual de positivos: {perc_positivos:.2f}% | Percentual de negativos: {perc_negativos:.2f}%")
else:
    print("Nenhum valor foi informado.")