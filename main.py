menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

Digite a opção desejada: """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do seu depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Saldo atualizado: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor do seu saque: "))
        if valor <= saldo and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saldo atualizado: R$ {saldo:.2f}")
        else:
            print("Operação falhou! Verifique o valor do saque, o limite disponível e o número de saques restantes.")

    elif opcao == "3":
        print(extrato or "Não foram realizadas movimentações.")
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
