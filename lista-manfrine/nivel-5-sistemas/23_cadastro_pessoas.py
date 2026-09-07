# 23. Cadastro de pessoas e profissões

# Crie um sistema que permita cadastrar pessoas e suas profissões,
# listar todos os cadastros e listar somente os desenvolvedores.
# Cadastre mais de três desenvolvedores.
# Use uma estrutura de seleção do tipo caso e repetição.

pessoas = []

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar todos")
    print("3 - Listar desenvolvedores")
    print("4 - Sair")

    opcao = int(input("Escolha uma opcao: "))
    if opcao < 1 or opcao > 4:
        print("Opção inválida. Tente novamente.")
        continue

    match opcao:
        case 1:
            nome = input("Digite um nome: ")
            profissao = input("Digite uma profissão: ").lower()

            pessoa = {
                "nome": nome,
                "profissao": profissao
            }

            pessoas.append(pessoa)

            print("Cadastro realizado com sucesso.")

        case 2:
            for pessoa in pessoas:
                print(
                    f"Nome: {pessoa['nome']} | "
                    f"Profissão: {pessoa['profissao']}"
                )

        case 3:
            for pessoa in pessoas:
                if pessoa["profissao"] == "desenvolvedor":
                    print(
                        f"Nome: {pessoa['nome']} | "
                        f"Profissão: {pessoa['profissao']}"
                    )

        case 4:
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")