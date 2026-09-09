# 6. Numeros dentro e fora de um intervalo
# Faca um algoritmo que leia 5 numeros e informe quantos estao no intervalo de 10 a 20 e quantos estao fora desse intervalo.

dentro_do_intervalo = 0
fora_do_intervalo = 0

for i in range(5):
    num = int(input("Digite um numero: "))
    
    if num >= 10 and num <= 20:
        dentro_do_intervalo += 1
    else:
        fora_do_intervalo += 1

print(f"Numeros dentro do intervalo (10 a 20): {dentro_do_intervalo}")
print(f"Numeros fora do intervalo: {fora_do_intervalo}")