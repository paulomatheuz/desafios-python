def perguntar():
    return input(
        "O que deseja realizar?\n"
        "<I> - Para Inserir um usuário\n"
        "<P> - Para Pesquisar um usuário\n"
        "<E> - Para Excluir um usuário\n"
        "<L> - Para Listar um usuário: "
    ).upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [
        input("Digite o nome: ").upper(),
        input("Digite a última data de acesso: "),
        input("Qual a última estação acessada: ").upper()
    ]
    salvar(dicionario)


def pesquisar(dicionario):
    print("Usuários atuais:", list(dicionario.keys()))

    quem_encontrar = input("Quem deseja pesquisar?\n").upper()
    procurar = dicionario.get(quem_encontrar)

    if procurar is not None:
        print(f"{quem_encontrar} encontrado!")
        print("Dados:", procurar)
    else:
        print(f"{quem_encontrar} não foi encontrado")


def remover(dicionario):
    print("Usuários atuais:", list(dicionario.keys()))

    quem_deletar = input("Quem deseja deletar?\n").upper()
    removido = dicionario.pop(quem_deletar, None)

    if removido is not None:
        print(f"{quem_deletar} deletado com sucesso")
    else:
        print(f"Erro ao deletar '{quem_deletar}'. Usuário não encontrado.")

    print("Dicionário atualizado:", dicionario)


def listar(dicionario):
    print("Usuários atuais:", list(dicionario.keys()))

def salvar(dicionario):
    with open("db.txt", "a") as usuarios:
        for chave, valor in dicionario.items():
            usuarios.write(f"{chave}: {valor}\n")
