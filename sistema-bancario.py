menu = """
Escolha uma opção:
1 - Depositar
2 - Sacar
3 - Imprimir Extrato
0 - Sair

"""

saldo = 0
LIMITE = 500
extrato = ""
LIMITE_SAQUES = 3
contator_saque = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        print("-----------Deposito-----------")
        valor_deposito = float(input("Qual o valor do depósito? "))
        if(valor_deposito >= 0):
            saldo += valor_deposito
            extrato += f"Depósito: +R$ {valor_deposito:.2f} \nSaldo: R$ {saldo:.2f}\n"
        else:
            print("Valor Inválido!")

    elif opcao == "2":
        print("-----------Saque-----------")
        
        saques_excedidos = contator_saque >= LIMITE_SAQUES

        if saques_excedidos:
            print("Número diário de saques excedido!")            
        else:
            valor_saque = float(input("Qual o valor a ser sacado? "))

            saldo_excedido = valor_saque > saldo
            limite_excedido = valor_saque > LIMITE
            
            if limite_excedido:            
                print("Valor do saque excedeu o limite!")
            elif saldo_excedido:
                print("Saldo Insuficiente!") 
            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: -R$ {valor_saque:.2f} \nSaldo: R$ {saldo:.2f}\n"
                contator_saque += 1
            else:
                print("Valor Inválido!")
            
    elif opcao == "3":
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("-----------Extrato-----------")
            print(extrato)
            print(f"----------- \nSaldo Total: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Saindo da conta...")
        break    
    else:
        print("Opção inexistente! Selecione outra opção.")



