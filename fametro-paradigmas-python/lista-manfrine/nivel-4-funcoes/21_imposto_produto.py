# 21. Imposto sobre produto
# Crie calcular_imposto(preco, categoria). Use 5% para alimentos, 12% para eletronicos e 8% para roupas.
# Retorne e mostre o valor final com imposto.

def calcular_imposto(preco, categoria):
    if categoria == "alimentos":
        imposto = preco * 0.05

    elif categoria == "eletronicos":
        imposto = preco * 0.12

    elif categoria == "roupas":
        imposto = preco * 0.08

    else:
        return None

    valor_final = preco + imposto
    return valor_final


preco = float(input("Digite o preço do produto: "))
categoria = input("Digite a categoria do produto: ").lower()

valor_final = calcular_imposto(preco, categoria)

if valor_final is not None:
    print(f"O valor final do produto é de: R$ {valor_final:.2f}")
else:
    print("Categoria inválida.")