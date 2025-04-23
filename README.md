# 🛒 Loja Virtual em Python

Este é um projeto de loja virtual feito em Python para a escola, executado no terminal.  
O foco é aplicar **tratamento de erros** com `try`, `except`, `else`, `finally` e criar **exceções personalizadas**.

---

## 📌 Funcionalidades

- Ver lista de produtos com preços e stock disponível;
- Adicionar produtos ao carrinho (respeitando limite de stock máximo de 100);
- Consultar o carrinho com total da compra;
- Consultar o saldo disponível;
- Adicionar saldo;
- Simular pagamento (com verificação de saldo).

---

## 💡 Exceções Personalizadas

### `ProdutoInexistenteError`
Lançada quando o utilizador tenta adicionar um produto que **não existe**.

### `SaldoInsuficienteError`
Lançada quando o utilizador tenta pagar uma compra sem saldo suficiente.

---

## ⚠️ Tratamento de Erros

O sistema trata os seguintes erros:

- Produto inexistente;
- Quantidade inválida (não numérica ou negativa);
- Adicionar mais do que o stock disponível (máximo 100);
- Tentar pagar com carrinho vazio;
- Saldo insuficiente;
- Tipo de dados incorreto (ValueError, etc.).

---

## 🧪 Como executar

1. Instala o Python (se ainda não tiveres).
2. Executa o ficheiro `.py` no terminal com o comando:

```bash
python loja_virtual.py
