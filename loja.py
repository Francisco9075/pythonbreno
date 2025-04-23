# excecoes.py
# Exceções personalizadas para lidar com situações específicas
class ProdutoInexistenteError(Exception):
    """Quando o produto não existe no catálogo."""
    pass

class SaldoInsuficienteError(Exception):
    """Quando o saldo não cobre o total da compra."""
    pass

class CarrinhoVazioError(Exception):
    """Quando o carrinho está vazio e se tenta mexer nele."""
    pass

produtos = {
    "camiseta": {
        "preco": 50.0,
        "descricao": "Camiseta confortável de algodão.",
        "disponibilidade": 100
    },
    "calças": {
        "preco": 80.0,
        "descricao": "Calças jeans em vários tamanhos.",
        "disponibilidade": 100
    },
    "ténis": {
        "preco": 120.0,
        "descricao": "Ténis desportivos para corridas.",
        "disponibilidade": 100
    },
    "boné": {
        "preco": 30.0,
        "descricao": "Boné leve, ótimo para o verão.",
        "disponibilidade": 100
    }
}

carrinho = {}
saldo = 200.0

def listar_produtos():
    print("\nAqui estão os produtos que temos disponíveis:")
    for nome, detalhes in produtos.items():
        print(f"- {nome.capitalize()} - {detalhes['preco']:.2f}€")
        print(f"  {detalhes['descricao']}")
        print(f"  Em stock: {detalhes['disponibilidade']} unidades\n")

def adicionar_ao_carrinho():
    try:
        produto = input("Qual produto queres adicionar ao carrinho? ").strip().lower()

        if produto not in produtos:
            raise ProdutoInexistenteError("Este produto não está disponível.")

        disponibilidade = produtos[produto]["disponibilidade"]
        if disponibilidade == 0:
            raise ValueError(f"O produto '{produto}' está esgotado no momento.")

        quantidade = input(f"Quantas unidades de '{produto}' gostarias de adicionar? ").strip()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise ValueError("A quantidade deve ser um número positivo.")
        quantidade = int(quantidade)

        if carrinho.get(produto, 0) + quantidade > disponibilidade:
            raise ValueError(f"Temos só {disponibilidade} unidades de '{produto}' disponíveis.")

    except (ProdutoInexistenteError, ValueError) as e:
        print(f"Erro: {e}")
    else:
        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        produtos[produto]["disponibilidade"] -= quantidade
        print(f"{quantidade} unidades de '{produto}' foram adicionadas ao teu carrinho.")
    finally:
        print("Operação concluída.\n")

def remover_do_carrinho():
    try:
        if not carrinho:
            raise CarrinhoVazioError("O teu carrinho está vazio, não há nada para remover.")

        produto = input("Qual produto queres remover do carrinho? ").strip().lower()

        if produto not in carrinho:
            raise ValueError(f"Não tens '{produto}' no teu carrinho.")

        quantidade = input(f"Quantas unidades de '{produto}' gostarias de remover? ").strip()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise ValueError("A quantidade deve ser um número positivo.")
        quantidade = int(quantidade)

        if quantidade > carrinho[produto]:
            raise ValueError(f"Só tens {carrinho[produto]} unidades de '{produto}' no carrinho.")

    except (CarrinhoVazioError, ValueError) as e:
        print(f"Erro: {e}")
    else:
        carrinho[produto] -= quantidade
        produtos[produto]["disponibilidade"] += quantidade
        if carrinho[produto] == 0:
            del carrinho[produto]
        print(f"{quantidade} unidades de '{produto}' foram removidas do teu carrinho.")
    finally:
        print("Operação concluída.\n")

def mostrar_carrinho():
    try:
        if not carrinho:
            raise ValueError("O teu carrinho está vazio, adiciona produtos para ver o conteúdo.")

        print("\nAqui está o teu carrinho de compras:")
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

def consultar_saldo():
    print(f"\nO teu saldo atual é: {saldo:.2f}€\n")

def adicionar_saldo():
    global saldo
    try:
        valor = input("Quanto gostarias de adicionar ao teu saldo? ").replace(",", ".").strip()
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor precisa ser positivo.")
    except ValueError as e:
        print(f"Erro: {e}")
    else:
        saldo += valor
        print(f"Saldo atualizado para: {saldo:.2f}€")
    finally:
        print("Operação concluída.\n")

def efetuar_pagamento():
    global saldo
    try:
        if not carrinho:
            raise ValueError("Não tens produtos no carrinho para pagar.")

        total = sum(produtos[produto]["preco"] * qtd for produto, qtd in carrinho.items())
        if total > saldo:
            raise SaldoInsuficienteError("O teu saldo não é suficiente para concluir a compra.")

    except (ValueError, SaldoInsuficienteError) as e:
        print(f"Erro: {e}")
    else:
        saldo -= total
        carrinho.clear()
        print(f"Pagamento concluído! O teu novo saldo é: {saldo:.2f}€")
    finally:
        print("Operação concluída.\n")

def menu():
    while True:
        print("===== Bem-vindo à Loja Virtual =====")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Remover do carrinho")
        print("4. Ver carrinho")
        print("5. Consultar saldo")
        print("6. Adicionar saldo")
        print("7. Efetuar pagamento")
        print("8. Sair")

        try:
            opcao = input("O que gostarias de fazer? ").strip()

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
                    efetuar_pagamento()
                case "8":
                    print("Obrigado por fazeres compras connosco! Até à próxima!")
                    break
                case _:
                    raise ValueError("Opção inválida. Tenta novamente.")
        except ValueError as e:
            print(f"Erro: {e}")
        finally:
            print("-----------------------------\n")

if __name__ == "__main__":
    menu()
