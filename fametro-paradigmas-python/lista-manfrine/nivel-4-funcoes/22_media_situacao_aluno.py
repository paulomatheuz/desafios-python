# 22. Média e situação de um aluno
# Crie calcular_media(n1, n2, n3, n4) e verificar_situacao(media). Retorne Aprovado para média maior ou igual a 7,
# Recuperação para média entre 5 e 6,9 e Reprovado para média menor que 5.

def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media


def verificar_situacao(media):
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return situacao


n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = calcular_media(n1, n2, n3, n4)
situacao = verificar_situacao(media)

print(f"A situação do aluno é: {situacao}")
print(f"A média do aluno foi: {media:.2f}")