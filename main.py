from sistema_estoque import funcao

while True:
    funcao.Menu()
    try:
        opcao = int(input("Qual funcao voce quer usar? "))

    except ValueError:
        print("Digite um Numero valido (1/2/3/4/0). ")
        continue
    
    if opcao == 1:
        try:
            nome = input("Qual o nome do produto? ")
            valor = float(input("Qual o valor do produto? "))
            id_produto = int(input("Qual o ID do produto? "))
            quantidade = int(input("Qual a quantidade do produto? "))

            funcao.CadastrarProduto(nome, valor, id_produto, quantidade)
            continue

        except ValueError:
            print("Erro. Digite apenas valores validos.")
            continue

    elif opcao == 2:
        try:
            id_produto = int(input("Qual o ID do produto que deve ser consultado? "))
            funcao.ConsultarProduto(id_produto)
            continue

        except ValueError:
            print("Erro. Digite apenas um valor valido.")
            continue

    elif opcao == 3:
        try:
            id_produto = int(input("Qual o ID do produto que deve ser alterado? "))
            campo = input("Qual campo deve ser alterado? (Nome/Valor/Quantidade) ")
            novo_valor = input(f"Qual o novo valor do {campo}? ")
            funcao.AtualizarProdutos(id_produto, campo, novo_valor)
            continue

        except ValueError:
            print("Erro. Digite apenas um valor valido.")
            continue

    elif opcao == 4:
        try:
            id_produto = int(input("Qual produto deseja excluir? (Digite seu ID) "))
            funcao.ExcluirProdutos(id_produto)
            continue

        except ValueError:
            print("Digite um ID valido. ")
            continue

    elif opcao == 0:
        break

    else:
        print("Digite um Numero valido (1/2/3/4/0). ")
        continue

    


