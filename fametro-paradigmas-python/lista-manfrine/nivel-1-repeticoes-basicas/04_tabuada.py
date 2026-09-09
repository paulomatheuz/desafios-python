# 4. Tabuada
# Faca um algoritmo que apresente a tabuada de multiplicacao de um numero qualquer informado pelo usuario.

num = int(input("Digite um numero: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} multiplicado por {i} e igual a {resultado}")