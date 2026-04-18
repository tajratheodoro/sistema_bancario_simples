# 🏦 Sistema Bancário em Python

Um script interativo de terminal que simula operações bancárias básicas. Este projeto foi desenvolvido para aplicar conceitos fundamentais de Python, como estruturas de repetição, condicionais e formatação de strings.

## 🚀 Funcionalidades

O menu interativo permite ao usuário escolher entre quatro opções:

* **[1] Depositar:** Permite adicionar um saldo positivo à conta. O valor é registrado no extrato.
* **[2] Sacar:** Permite realizar saques com regras de negócio específicas:
    * O valor máximo por saque é de R$ 1.000,00.
    * Existe um limite máximo de 3 saques diários.
    * Valida se há saldo suficiente antes de aprovar a transação.
* **[3] Extrato:** Lista todas as operações de depósito e saque realizadas, exibindo o saldo atual da conta formatado em Reais (R$).
* **[0] Sair:** Encerra a aplicação.

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3.14
* **Conceitos aplicados:** Variáveis, Operadores Matemáticos, Estruturas Condicionais (`if/elif/else`), Laços de Repetição (`while`), e F-Strings.