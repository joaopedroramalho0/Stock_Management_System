import json
import os

#Aqui e onde vão ficar as funções do programa. Sendo elas:

def Menu():
    print("\n" + "=" * 48)
    print("       Sistema de Gestão de Estoque")
    print("=" * 48)

    print("""
    [1] Cadastrar produto
    [2] Consultar produtos
    [3] Atualizar produto
    [4] Excluir produto
    [0] Sair
    """)

    print("=" * 48)

def CadastrarProduto(nome, valor, id_produto, quantidade):
    """
    Cadastra um novo produto no arquivo JSON de estoque.

    Args:
        nome (str): Nome do produto a ser cadastrado.
        valor (int | float): Preço unitário do produto.
        id_produto (int): Identificador do produto.
        quantidade (int): Quantidade inicial em estoque.

    Returns:
        None: A função salva os dados diretamente em produtos.json
        ou encerra a operação em caso de JSON inválido.
    """
    produtos = []
    produto = {
        "nome": nome,
        "valor": valor,
        "id": id_produto,
        "quantidade": quantidade
    }

    if not os.path.exists("produtos.json"):
        with open("produtos.json", "w", encoding="utf-8") as arquivo:
            pass
    else:
        try:
            with open("produtos.json", "r", encoding="utf-8") as arquivo:
                produtos = json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está vazio ou possui dados inválidos.")
            return

    produtos.append(produto)
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)



def ConsultarProdutosID(id_produto):
    """
        Consulta um produto cadastrado utilizando seu ID.
    
        Args:
            id_produto (int): Identificador do produto a ser consultado.
    
        Returns:
            dict | None: Dicionário contendo os dados do produto,
            caso encontrado, ou None se o ID não existir.
    """
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return None



def AtualizarProdutos(id_produto, campo, novo_valor):
    """
    Atualiza uma informação de um produto cadastrado.

    Permite alterar o nome, o preço ou a quantidade de
    um produto e salva a alteração no arquivo JSON.

    Args:
        id_produto (int): Identificador do produto a ser atualizado.
        campo (str): Campo que será alterado. Aceita
            "nome", "valor" ou "quantidade".
        novo_valor (str | int | float): Novo valor do campo.
            É convertido para float quando o campo é "valor"
            e para int quando é "quantidade".

    Returns:
        None: A função atualiza diretamente produtos.json.
        Caso o campo, o valor ou o ID seja inválido,
        a operação é encerrada sem salvar alterações.
    """
    campo = campo.strip().lower()
    encontrado = False

    if campo not in ("nome", "valor", "quantidade"):
        print("Campo inválido.")
        return

    try:
        if campo == "valor":
            novo_valor = float(novo_valor)
        elif campo == "quantidade":
            novo_valor = int(novo_valor)
    except ValueError:
        print("Digite um número válido.")
        return

    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

    for produto in produtos:
        if produto["id"] == id_produto:
            encontrado = True
            if campo == "nome":
                produto["nome"] = novo_valor
            elif campo == "valor":
                produto["valor"] = novo_valor
            elif campo == "quantidade":
                produto["quantidade"] = novo_valor
            break

    if not encontrado:
        print("Produto não encontrado.")
        return

    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)



def ExcluirProdutos(id_produto):
    """
    Exclui um produto cadastrado utilizando seu ID.

    Localiza o produto no arquivo JSON e solicita confirmação
    do usuário antes de realizar a exclusão.

    Args:
        id_produto (int): Identificador do produto a ser excluído.

    Returns:
        None: A função salva a lista atualizada em produtos.json
        caso a exclusão seja confirmada. Se o produto não existir
        ou o usuário cancelar, nenhuma alteração será salva.
    """
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

    for indice, produto in enumerate(produtos):
        if produto["id"] == id_produto:
            print(produto)

            while True:
                confirmacao = input("Voce deseja apagar esse produto? (S/N): ")

                if confirmacao.upper().strip() == "S":
                    del produtos[indice]

                    with open("produtos.json", "w", encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

                    print("Produto excluído com sucesso!")
                    return

                elif confirmacao.upper().strip() == "N":
                    return

                else:
                    print("Digite um valor valido 'S' para Sim e 'N' para Não. ")
                    continue



def ConsultarProduto(id_produto):
    """
    Consulta e exibe as informações de um produto pelo seu ID.

    Percorre os produtos cadastrados no arquivo JSON e exibe
    o nome, o valor, o ID e a quantidade do produto encontrado.

    Args:
        id_produto (int): Identificador do produto a ser consultado.

    Returns:
        None: A função exibe os dados do produto no terminal.
        Caso o ID não seja encontrado, informa ao usuário
        que o produto não existe.
    """
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)

    for produto in produtos:
        if produto["id"] == id_produto:
            print(f"Nome: {produto['nome']}")
            print(f"Valor: {produto['valor']:.2f}")
            print(f"ID do Produto: {produto['id']}")
            print(f"Quantidade: {produto['quantidade']}")
            return
    print("Produto nao encontrado. ")
    


     

    


            
        


                    
