# 20. Desconto em compras
# Crie calcular_desconto(valor_compra). Compras de até R$ 100 não recebem desconto; entre R$ 100 e R$ 500 recebem 10%;
# acima de R$ 500 recebem 15%. Retorne e mostre o valor final.

def calcular_desconto(valor_compra):
    if valor_compra <= 100:
        valor_final = valor_compra

    elif valor_compra <= 500:
        desconto = valor_compra * (10 / 100)
        valor_final = valor_compra - desconto

    else:
        desconto = valor_compra * (15 / 100)
        valor_final = valor_compra - desconto

    return valor_final


valor_compra = float(input("Digite o valor da compra: "))

valor_final = calcular_desconto(valor_compra)

print(f"O valor final é de: R$ {valor_final:.2f}")