valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = valor1 + valor2
    print("O resultado é: ", resultado)

elif operacao == "-":
    resultado = valor1 - valor2
    print("O resultado é: ", resultado)

elif operacao == "*":
    resultado = valor1 * valor2
    print("O resultado é: ", resultado)

elif operacao == "/":
    if valor2 != 0:
        resultado = valor1 / valor2
        print("O resultado é: ", resultado)
    else:
        print("Erro: não é possível dividir por zero.")

else:
    print("Operação inválida.")
