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



    produtos.append(produto)
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def ConsultarProdutosID(id):
    with open("produtos,json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)
    
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return None


