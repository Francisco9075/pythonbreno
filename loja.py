# excecoes.py
# Definição de exceções personalizadas para tratar diferentes tipos de erros
class ProdutoInexistenteError(Exception):
    """Exceção para quando o produto não existe no catálogo."""
    pass

class SaldoInsuficienteError(Exception):
    """Exceção para quando o saldo não é suficiente para realizar o pagamento."""
    pass

class CarrinhoVazioError(Exception):
    """Exceção para quando se tenta operar com um carrinho vazio."""
    pass

# Catálogo de produtos disponíveis na loja, com preço, descrição e stock
produtos = {
    "camiseta": {
        "preco": 50.0,
        "descricao": "Camiseta confortável de algodão.",
        "disponibilidade": 100
    },
    "calças": {
        "preco": 80.0,
        "descricao": "Calças de jeans, disponíveis em diversos tamanhos.",
        "disponibilidade": 100
    },
    "ténis": {
        "preco": 120.0,
        "descricao": "Ténis desportivos, ideais para corridas.",
        "disponibilidade": 100
    },
    "boné": {
        "preco": 30.0,
        "descricao": "Boné desportivo para o verão.",
        "disponibilidade": 100
    }
}

# Dicionário que representa os produtos adicionados ao carrinho
carrinho = {}

# Saldo inicial do utilizador
saldo = 200.0

# Função que lista todos os produtos disponíveis no catálogo
def listar_produtos():
    print("\nProdutos disponíveis:")
    for nome, detalhes in produtos.items():
        print(f"- {nome.capitalize()} - {detalhes['preco']:.2f}€")
        print(f"  {detalhes['descricao']}")
        print(f"  Disponível: {detalhes['disponibilidade']} unidades\n")

# Função que adiciona produtos ao carrinho de compras
def adicionar_ao_carrinho():
    try:
        produto = input("Produto a adicionar: ").strip().lower()

        if produto not in produtos:
            raise ProdutoInexistenteError("Produto não encontrado.")

        disponibilidade = produtos[produto]["disponibilidade"]
        if disponibilidade == 0:
            raise ValueError(f"'{produto}' está esgotado.")

        quantidade = input(f"Quantidade de '{produto}': ").strip()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")
        quantidade = int(quantidade)

        if carrinho.get(produto, 0) + quantidade > disponibilidade:
            raise ValueError(f"Quantidade excede o stock disponível ({disponibilidade}).")

    except (ProdutoInexistenteError, ValueError) as e:
        print(f"Erro: {e}")
    else:
        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        produtos[produto]["disponibilidade"] -= quantidade
        print(f"Foram adicionadas {quantidade} unidades de '{produto}' ao carrinho.")
    finally:
        print("Operação concluída.\n")

# Função para remover produtos do carrinho
def remover_do_carrinho():
    try:
        if not carrinho:
            raise CarrinhoVazioError("O carrinho está vazio.")

        produto = input("Produto a remover: ").strip().lower()

        if produto not in carrinho:
            raise ValueError("Produto não está no carrinho.")

        quantidade = input(f"Quantidade de '{produto}' para remover: ").strip()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise ValueError("Quantidade inválida.")
        quantidade = int(quantidade)

        if quantidade > carrinho[produto]:
            raise ValueError(f"Só existem {carrinho[produto]} unidades de '{produto}' no carrinho.")

    except (CarrinhoVazioError, ValueError) as e:
        print(f"Erro: {e}")
    else:
        carrinho[produto] -= quantidade
        produtos[produto]["disponibilidade"] += quantidade
        if carrinho[produto] == 0:
            del carrinho[produto]
        print(f"Foram removidas {quantidade} unidades de '{produto}' do carrinho.")
    finally:
        print("Operação concluída.\n")

# Mostra os produtos presentes no carrinho e o total da compra
def mostrar_carrinho():
    try:
        if not carrinho:
            raise ValueError("O carrinho está vazio.")

        print("\nCarrinho de Compras:")
        total = 0
        for produto, qtd in carrinho.items():
            subtotal = produtos[produto]["preco"] * qtd
            print(f"- {qtd}x {produto} - {subtotal:.2f}€")
            total += subtotal
        print(f"Total da compra: {total:.2f}€")

    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        print("Consulta concluída.\n")

# Mostra o saldo disponível do utilizador
def consultar_saldo():
    print(f"\nSaldo atual: {saldo:.2f}€\n")

# Permite ao utilizador adicionar mais saldo
def adicionar_saldo():
    global saldo
    try:
        valor = input("Valor a adicionar: ").replace(",", ".").strip()
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
    except ValueError as e:
        print(f"Erro: {e}")
    else:
        saldo += valor
        print(f"Saldo atualizado: {saldo:.2f}€")
    finally:
        print("Operação concluída.\n")

# Efetua o pagamento dos produtos no carrinho, descontando o saldo
def Pagamento():
    global saldo
    try:
        if not carrinho:
            raise ValueError("O carrinho está vazio.")

        total = sum(produtos[produto]["preco"] * qtd for produto, qtd in carrinho.items())
        if total > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para efetuar o pagamento.")

    except (ValueError, SaldoInsuficienteError) as e:
        print(f"Erro: {e}")
    else:
        saldo -= total
        carrinho.clear()
        print(f"Pagamento efetuado com sucesso! Novo saldo: {saldo:.2f}€")
    finally:
        print("Pagamento concluído.\n")

# Menu principal da aplicação, com as opções para o utilizador
def menu():
    while True:
        print("===== Loja Virtual =====")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Remover do carrinho")
        print("4. Ver carrinho")
        print("5. Consultar saldo")
        print("6. Adicionar saldo")
        print("7. Efetuar pagamento")
        print("8. Sair")

        try:
            opcao = input("Escolha uma opção: ").strip()

            match opcao:
                case "1":
                    listar_produtos()
                case "2":
                    adicionar_ao_carrinho()
                case "3":
                    remover_do_carrinho()
                case "4":
                    mostrar_carrinho()
                case "5":
                    consultar_saldo()
                case "6":
                    adicionar_saldo()
                case "7":
                    Pagamento()
                case "8":
                    print("Obrigado por visitar a minha loja!")
                    break
                case _:
                    raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}")
        finally:
            print("-----------------------------\n")

# Início da aplicação
if __name__ == "__main__":
    menu()
