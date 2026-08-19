from cadastro_usuarios.usuarios import perguntar, inserir, pesquisar, remover, listar

usuarios = {}

opcao = perguntar()

while opcao in ["I", "P", "E", "L"]:

    if opcao == "I":
        inserir(usuarios)

    elif opcao == "E":
        remover(usuarios)

    elif opcao == "L":
        listar(usuarios)

    elif opcao == "P":
        pesquisar(usuarios)

    opcao = perguntar()