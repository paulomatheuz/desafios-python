# 19. Salário líquido com descontos
# Crie calcular_salario_liquido(salario_bruto).
# Desconte 8% de INSS e 6% de vale-transporte.
# Exiba salário bruto, total de descontos e salário líquido.

def calcular_salario_liquido(salario_bruto):
    inss = salario_bruto * (8 / 100)
    vale_transporte = salario_bruto * (6 / 100)

    descontos = inss + vale_transporte
    salario_liquido = salario_bruto - descontos

    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Total de descontos: R$ {descontos:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

    return salario_liquido
