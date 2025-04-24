# loja_virtual.py

class ProdutoDesconhecido(Exception):
    def __init__(self, mensagem="Produto não reconhecido."):
        super().__init__(mensagem)

class SemSaldo(Exception):
    def __init__(self, mensagem="Saldo insuficiente para concluir a compra."):
        super().__init__(mensagem)

class CarrinhoVazio(Exception):
    def __init__(self, mensagem="O carrinho está vazio."):
        super().__init__(mensagem)

artigos = {
    "camiseta": {"preco": 37.5, "descricao": "Conforto e estilo num só.", "stock": 100},
    "calças": {"preco": 64.9, "descricao": "Perfeitas para o dia-a-dia.", "stock": 100},
    "ténis": {"preco": 112.0, "descricao": "Ideais para dar aquele passeio.", "stock": 100},
    "boné": {"preco": 18.75, "descricao": "Para proteger do sol com pinta.", "stock": 100}
}

carrinho = {}
dinheiro = 1000.0

def saldo():
    print(f"\nSaldo disponível: {dinheiro:.2f}€\n")

def carregar_conta():
    global dinheiro
    try:
        valor = input("Quanto queres carregar? ").replace(",", ".").strip()
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Tem de ser um valor positivo.")
    except ValueError as erro:
        print(f"Aviso: {erro}")
    else:
        dinheiro += valor
        print(f"Conta atualizada. Novo saldo: {dinheiro:.2f}€")
    finally:
        print("Ação concluída.\n")

def ver_lista():
    print("\nLista de artigos disponíveis:\n")
    for nome, info in artigos.items():
        print(f"{nome.capitalize()} - {info['preco']}€")
        print(f"Descrição: {info['descricao']}")
        print(f"Em stock: {info['stock']}\n")

def meter_no_carrinho():
    try:
        item = input("Nome do artigo a adicionar: ").strip().lower()
        if item not in artigos:
            raise ProdutoDesconhecido("Esse artigo não está na loja.")

        if artigos[item]["stock"] == 0:
            raise ValueError(f"Infelizmente, '{item}' está esgotado.")

        qtd = input("Quantidade a adicionar: ").strip()
        if not qtd.isdigit() or int(qtd) <= 0:
            raise ValueError("Quantidade inválida.")
        qtd = int(qtd)

        disponivel = artigos[item]["stock"]
        if carrinho.get(item, 0) + qtd > disponivel:
            raise ValueError(f"Apenas temos {disponivel} unidades de '{item}'.")

    except (ProdutoDesconhecido, ValueError) as erro:
        print(f"Erro: {erro}")
    else:
        carrinho[item] = carrinho.get(item, 0) + qtd
        artigos[item]["stock"] -= qtd
        print(f"{qtd} unidade(s) de '{item}' adicionadas ao carrinho.")
    finally:
        print("Ação concluída.\n")

def tirar_do_carrinho():
    try:
        if not carrinho:
            raise CarrinhoVazio("O teu carrinho está vazio.")

        item = input("Que artigo queres remover? ").strip().lower()
        if item not in carrinho:
            raise ValueError("Esse artigo não está no carrinho.")

        qtd = input("Quantidade a remover: ").strip()
        if not qtd.isdigit() or int(qtd) <= 0:
            raise ValueError("Número inválido.")
        qtd = int(qtd)

        if qtd > carrinho[item]:
            raise ValueError(f"Tens só {carrinho[item]} unidade(s) de '{item}' no carrinho.")

    except (CarrinhoVazio, ValueError) as erro:
        print(f"Aviso: {erro}")
    else:
        carrinho[item] -= qtd
        artigos[item]["stock"] += qtd
        if carrinho[item] == 0:
            del carrinho[item]
        print(f"{qtd} unidade(s) de '{item}' removidas do carrinho.")
    finally:
        print("Tudo tratado.\n")

def mostrar_carrinho():
    try:
        if not carrinho:
            raise ValueError("O carrinho está vazio.")

        print("\nCarrinho atual:")
        total = 0
        for nome, qtd in carrinho.items():
            subtotal = artigos[nome]["preco"] * qtd
            print(f"{qtd}x {nome} = {subtotal:.2f}€")
            total += subtotal
        print(f"Total estimado: {total:.2f}€")
    except ValueError as erro:
        print(f"Erro: {erro}")
    finally:
        print("Fim da visualização.\n")

def finalizar_compra():
    global dinheiro
    try:
        if not carrinho:
            raise ValueError("Não há nada no carrinho para pagar.")

        total = sum(artigos[n]["preco"] * q for n, q in carrinho.items())
        if total > dinheiro:
            raise SemSaldo("Não tens saldo suficiente.")

    except (ValueError, SemSaldo) as erro:
        print(f"Erro: {erro}")
    else:
        dinheiro -= total
        carrinho.clear()
        print(f"Compra feita com sucesso. Saldo restante: {dinheiro:.2f}€")
    finally:
        print("Processo terminado.\n")

def principal():
    while True:
        print("=== LOJA VIRTUAL ===")
        print("1. Ver artigos")
        print("2. Adicionar artigo ao carrinho")
        print("3. Remover artigo do carrinho")
        print("4. Ver carrinho")
        print("5. Ver saldo")
        print("6. Carregar saldo")
        print("7. Finalizar compra")
        print("8. Sair")

        try:
            acao = input("Escolhe uma opção: ").strip()
            match acao:
                case "1":
                    ver_lista()
                case "2":
                    meter_no_carrinho()
                case "3":
                    tirar_do_carrinho()
                case "4":
                    mostrar_carrinho()
                case "5":
                    saldo()
                case "6":
                    carregar_conta()
                case "7":
                    finalizar_compra()
                case "8":
                    print("Até breve! Obrigado pela visita.")
                    break
                case _:
                    raise ValueError("Opção não reconhecida.")
        except ValueError as erro:
            print(f"Aviso: {erro}")
        finally:
            print("--------------------------\n")

if __name__ == "__main__":
    principal()
