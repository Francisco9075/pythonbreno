Loja Virtual em Python
Este é um projeto simples de uma loja virtual feito em Python, para ser usado no terminal.
A ideia é praticar o uso de tratamento de erros com try, except, else, finally, além de criar erros personalizados.

Funcionalidades
Ver os produtos disponíveis, com preços e stock;

Adicionar produtos ao carrinho (máximo de 100 unidades por produto);

Ver o carrinho e o total da compra;

Consultar e adicionar saldo;

Fazer o pagamento (só se tiver saldo suficiente).

Erros Personalizados
ProdutoInexistenteError
Usado quando se tenta adicionar um produto que não existe.

SaldoInsuficienteError
Aparece quando o saldo não é suficiente para pagar a compra.

Tratamento de Erros
O programa consegue identificar e tratar situações como:

Produto não encontrado;

Quantidade inválida (negativa ou não numérica);

Tentar comprar mais do que o stock disponível;

Carrinho vazio no momento do pagamento;

Saldo insuficiente;

Outros erros de dados (como ValueError).
