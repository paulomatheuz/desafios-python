valor1 = input("digite um número ")
valor2 = input("digite outro número ")
operação = input("digite a operação (+, -, *, /): ")

if operação == "+":
    resultado = float(valor1) + float(valor2)
    print("O resultado é: ", resultado)

elif operação == "-":
    resultado = float(valor1) - float(valor2)
    print("O resultado é: ", resultado)

elif operação == "*":
    resultado = float(valor1) * float(valor2)
    print("O resultado é: ", resultado)

elif operação == "/":
    resultado = float(valor1) / float(valor2)
    print("O resultado é: ", resultado)
