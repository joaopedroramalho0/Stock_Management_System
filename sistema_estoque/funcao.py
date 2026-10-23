import json
import os

#Aqui e onde vão ficar as funções do programa. Sendo elas:

def Menu():
    print("\n" + "=" * 48)
    print("             STOCKFLOW v0.1.0")
    print("       Sistema de Gestão de Estoque")
    print("=" * 48)

    print("""
    [1] Cadastrar produto
    [2] Consultar produtos
    [3] Buscar produto por ID
    [4] Atualizar produto
    [5] Excluir produto
    [6] Registrar venda
    [7] Consultar histórico de vendas
    [8] Relatório de estoque
    [9] Relatório de vendas
    [0] Sair
    """)

    print("=" * 48)

def CadastrarProduto(nome, valor, id, quantidade):

    produtos = []
    produto = {
        "nome": nome,
        "valor": valor,
        "id": id,
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
    """
    Cadastra um novo produto no arquivo JSON de estoque.

    Args:
        nome (str): Nome do produto a ser cadastrado.
        valor (int | float): Preço unitário do produto.
        id (int): Identificador do produto.
        quantidade (int): Quantidade inicial em estoque.

    Returns:
        None: A função salva os dados diretamente em produtos.json
        ou encerra a operação em caso de JSON inválido.
    """


    produtos.append(produto)
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def ConsultarProdutosID(id):
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)
    
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return None
    """
    Consulta um produto cadastrado utilizando seu ID.

    Args:
        id (int): Identificador do produto a ser consultado.

    Returns:
        dict | None: Dicionário contendo os dados do produto,
        caso encontrado, ou None se o ID não existir.
    """

def AtualizarProdutos(id, campo, novo_valor):

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
        if produto["id"] == id:
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
    """
    Atualiza uma informação de um produto cadastrado.

    Permite alterar o nome, o preço ou a quantidade de
    um produto e salva a alteração no arquivo JSON.

    Args:
        id (int): Identificador do produto a ser atualizado.
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
    
# def ExcluirProdutos(id):
    


            
        


                    
