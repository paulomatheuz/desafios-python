# 18. Folha de pagamento
# Para 5 funcionários, leia nome, horas trabalhadas e valor da hora.
# Calcule o salário bruto, o INSS (7,5% até R$ 2.500,00; 9% até R$ 5.000,00; 12% acima disso) e o salário líquido.
# Exiba todos esses valores.

for i in range(5):
    funcionario = input("Digite o nome do funcionário: ")
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
    valor_hora = float(input("Digite o valor da hora trabalhada: "))

    salario_bruto = horas_trabalhadas * valor_hora

    if salario_bruto <= 2500:
        inss = salario_bruto * (7.5 / 100)
    elif salario_bruto <= 5000:
        inss = salario_bruto * (9 / 100)
    else:
        inss = salario_bruto * (12 / 100)

    salario_liquido = salario_bruto - inss

    print(f"Funcionário: {funcionario}")
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"INSS: R$ {inss:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")
    print("-" * 30)