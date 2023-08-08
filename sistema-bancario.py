def deposito(saldo, valor, extrato):
    if(valor >= 0):
        saldo += valor
        extrato += f"Depósito: +R$ {valor:.2f} \nSaldo: R$ {saldo:.2f}\n"
        return saldo, extrato
    else:
        print("Valor Inválido!")

def saque(saldo=0, valor=0, extrato="", numero_saques=0, limite_saques=3):    
    saques_excedidos = numero_saques >= limite_saques

    if saques_excedidos:
        print("Número diário de saques excedido!")
        return saldo, extrato, numero_saques            
    else:     
        saldo_excedido = valor > saldo
        limite_excedido = valor > 500
        
        if limite_excedido:            
            print("Valor do saque excedeu o limite!")
            return saldo, extrato, numero_saques
        elif saldo_excedido:
            print("Saldo Insuficiente!")
            return saldo, extrato, numero_saques 
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f} \nSaldo: R$ {saldo:.2f}\n"
            numero_saques += 1
            return saldo, extrato, numero_saques
        else:
            print("Valor Inválido!")

def imprimirExtrato(saldo, extrato=""):
    if not extrato:
        print("Não foram realizadas movimentações.")
        print(f"----------- \nSaldo Total: R$ {saldo:.2f}")
    else:
        print("-----------Extrato-----------")
        print(extrato)
        print(f"----------- \nSaldo Total: R$ {saldo:.2f}")

menu = """
Escolha uma opção:
1 - Depositar
2 - Sacar
3 - Imprimir Extrato
0 - Sair

"""

saldo = 0
# LIMITE = 500
extrato = ""
# LIMITE_SAQUES = 3
contator_saque = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        print("-----------Deposito-----------")
        valores_deposito = (deposito(saldo, float(input("Digite o valor a ser depositado? ")), extrato))
        saldo = valores_deposito[0]
        extrato = valores_deposito[1]                
       

    elif opcao == "2":
        print("-----------Saque-----------")        
        valores_saque = (saque(saldo, float(input("Qual o valor a ser sacado? ")), extrato, contator_saque))
        saldo = valores_saque[0]
        extrato = valores_saque[1]
        contator_saque = valores_saque[2]       
            
    elif opcao == "3":
        imprimirExtrato(saldo, extrato=extrato)


    elif opcao == "0":
        print("Saindo da conta...")
        break    
    else:
        print("Opção inexistente! Selecione outra opção.")



