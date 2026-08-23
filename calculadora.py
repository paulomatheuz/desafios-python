valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = valor1 + valor2

elif operacao == "-":
    resultado = valor1 - valor2

elif operacao == "*":
    resultado = valor1 * valor2

elif operacao == "/":
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        resultado = "Erro: não é possível dividir por zero."

else:
    resultado = "Operação inválida."

print("O resultado é:", resultado)
