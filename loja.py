# excecoes.py
class ProdutoInexistenteError(Exception):
    """Exceção para produto não encontrado no catálogo."""
    pass

class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente ao tentar pagar."""
    pass

class CarrinhoVazioError(Exception):
    """Exceção para tentativas de operar em um carrinho vazio."""
    pass



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
        "descricao": "Ténis esportivos, ideais para corridas.",
        "disponibilidade": 100
    },
    "boné": {
        "preco": 30.0,
        "descricao": "Boné esportivo para o verão.",
        "disponibilidade": 100
    }
}

carrinho = {}
saldo = 200.0


def listar_produtos():
    print("\n📦 Produtos disponíveis:")
    for nome, detalhes in produtos.items():
        print(f"- {nome.capitalize()} - {detalhes['preco']:.2f}€")
        print(f"  {detalhes['descricao']}")
        print(f"  Disponível: {detalhes['disponibilidade']} unidades\n")


def adicionar_ao_carrinho():
    try:
        produto = input("🔹 Produto a adicionar: ").strip().lower()

        if produto not in produtos:
            raise ProdutoInexistenteError("Produto não encontrado.")

        disponibilidade = produtos[produto]["disponibilidade"]
        if disponibilidade == 0:
            raise ValueError(f"'{produto}' está fora de estoque.")

        quantidade = input(f"🔹 Quantidade de '{produto}': ").strip()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise ValueError("Quantidade deve ser um número inteiro positivo.")
        quantidade = int(quantidade)

        if carrinho.get(produto, 0) + quantidade > disponibilidade:
            raise ValueError(f"Quantidade excede estoque disponível ({disponibilidade}).")

    except (ProdutoInexistenteError, ValueError) as e:
        print(f"❌ Erro: {e}")
    else:
        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        produtos[produto]["disponibilidade"] -= quantidade
        print(f"✅ Adicionado {quantidade}x '{produto}' ao carrinho.")
    finally:
        print("🛒 Operação finalizada.\n")


def remover_do_carrinho():
    try:
        if not carrinho:
            raise CarrinhoVazioError("Não é possível remover: o carrinho está vazio.")

        produto = input("🔹 Produto a remover: ").strip().lower()

        if produto not in carrinho:
            raise ValueError("Produto não está no carrinho.")

        quantidade = input(f"🔹 Quantidade de '{produto}' para remover: ").strip()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise ValueError("Quantidade inválida.")
        quantidade = int(quantidade)

        if quantidade > carrinho[produto]:
            raise ValueError(f"Só tem {carrinho[produto]} unidades de '{produto}' no carrinho.")

    except (CarrinhoVazioError, ValueError) as e:
        print(f"❌ Erro: {e}")
    else:
        carrinho[produto] -= quantidade
        produtos[produto]["disponibilidade"] += quantidade
        if carrinho[produto] == 0:
            del carrinho[produto]
        print(f"✅ Removido {quantidade}x '{produto}' do carrinho.")
    finally:
        print("🛒 Operação finalizada.\n")


def mostrar_carrinho():
    try:
        if not carrinho:
            raise ValueError("Carrinho está vazio.")

        print("\n🛍️  Carrinho de compras:")
        total = 0
        for produto, qtd in carrinho.items():
            subtotal = produtos[produto]["preco"] * qtd
            print(f"- {qtd}x {produto} - {subtotal:.2f}€")
            total += subtotal
        print(f"💰 Total: {total:.2f}€")

    except ValueError as e:
        print(f"❌ {e}")
    finally:
        print("🛒 Consulta finalizada.\n")


def consultar_saldo():
    print(f"\n💼 Saldo atual: {saldo:.2f}€\n")


def adicionar_saldo():
    global saldo
    try:
        valor = input("🔹 Valor a adicionar: ").replace(",", ".").strip()
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Valor deve ser positivo.")
    except ValueError as e:
        print(f"❌ Erro: {e}")
    else:
        saldo += valor
        print(f"✅ Novo saldo: {saldo:.2f}€")
    finally:
        print("💼 Operação concluída.\n")


def simular_pagamento():
    global saldo
    try:
        if not carrinho:
            raise ValueError("Carrinho está vazio.")

        total = sum(produtos[produto]["preco"] * qtd for produto, qtd in carrinho.items())
        if total > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para finalizar a compra.")

    except (ValueError, SaldoInsuficienteError) as e:
        print(f"❌ Erro: {e}")
    else:
        saldo -= total
        carrinho.clear()
        print(f"✅ Pagamento efetuado com sucesso! Novo saldo: {saldo:.2f}€")
    finally:
        print("💳 Pagamento concluído.\n")


def menu():
    while True:
        print("===== 🛍️ Loja Virtual =====")
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
                    simular_pagamento()
                case "8":
                    print("👋 Obrigado por visitar nossa loja!")
                    break
                case _:
                    raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"❌ Erro: {e}")
        finally:
            print("-----------------------------\n")


if __name__ == "__main__":
    menu()
