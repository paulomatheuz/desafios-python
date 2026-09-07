# 24. Sistema de aluguel de carros
# Crie um sistema com: cadastrar carro e preco (status inicial disponivel); pesquisar; listar; alugar, recebendo dias e
# calculando o valor total, com status alugado; devolver e pagar, alterando o status para disponivel.

veiculos = []

def cadastrar_carro():
    modelo = input("Digite o modelo do carro: ")
    preco = float(input("Digite o preço do aluguel por dia: "))
    veiculo = {
        "modelo": modelo,
        "preco": preco,
        "status": "disponivel",
        "dias_alugados": 0,
        "valor_total": 0
    }
    veiculos.append(veiculo)

def listar_veiculos():
    for veiculo in veiculos:
        print(
            f"Modelo: {veiculo['modelo']} | "
            f"Preço: {veiculo['preco']} | "
            f"Status: {veiculo['status']}"
        )

def pesquisar_veiculo():
    modelo = input("Digite o modelo do carro que deseja pesquisar: ")
    for veiculo in veiculos:
        if veiculo["modelo"].lower() == modelo.lower():
            print(
                f"Modelo: {veiculo['modelo']} | "
                f"Preço: {veiculo['preco']} | "
                f"Status: {veiculo['status']}"
            )
            return
    print("Veículo não encontrado.")

def alugar_veiculo():
    modelo = input("Digite o modelo do carro que deseja alugar: ")
    for veiculo in veiculos:
        if veiculo["modelo"].lower() == modelo.lower():
            if veiculo["status"] == "disponivel":
                dias = int(input("Digite a quantidade de dias para aluguel: "))
                if dias <= 0:
                    print("A quantidade de dias deve ser maior que zero.")
                    return

                valor_total = veiculo["preco"] * dias
                veiculo["status"] = "alugado"
                veiculo["dias_alugados"] = dias
                veiculo["valor_total"] = valor_total
                print(f"Veículo alugado com sucesso! Valor total: R${valor_total:.2f}")
            else:
                print("Veículo não disponível para aluguel.")
            return
    print("Veículo não encontrado.")

def devolver_veiculo():
    modelo = input("Digite o modelo do carro que deseja devolver: ")
    for veiculo in veiculos:
        if veiculo["modelo"].lower() == modelo.lower():
            if veiculo["status"] == "alugado":
                print(f"Valor a pagar: R$ {veiculo['valor_total']:.2f}")
                veiculo["status"] = "disponivel"
                veiculo["dias_alugados"] = 0
                veiculo["valor_total"] = 0
                print("Veículo devolvido e pagamento realizado com sucesso!")
            else:
                print("Veículo não está alugado.")
            return
    print("Veículo não encontrado.")

while True:
    print("\n1 - Cadastrar carro")
    print("2 - Listar veículos")
    print("3 - Pesquisar veículo")
    print("4 - Alugar veículo")
    print("5 - Devolver veículo")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao < 1 or opcao > 6:
        print("Opção inválida. Tente novamente.")
        continue

    match opcao:
        case 1:
            cadastrar_carro()
        case 2:
            listar_veiculos()
        case 3:
            pesquisar_veiculo()
        case 4:
            alugar_veiculo()
        case 5:
            devolver_veiculo()
        case 6:
            print("Programa encerrado.")
            break
