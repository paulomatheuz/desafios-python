# 17. Situação de uma turma
# Processe uma turma de 5 alunos. Para cada aluno, leia 3 notas, calcule a média e informe:
# Aprovado para média maior ou igual a 7; Em exame para média entre 5 e 6,9; Reprovado para média menor que 5.

for i in range(5):
    aluno = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        mensagem = "Aprovado"
    elif media >= 5:
        mensagem = "Em exame"
    else:
        mensagem = "Reprovado"

    print(f"Aluno: {aluno}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {mensagem}")
    print("-" * 30)