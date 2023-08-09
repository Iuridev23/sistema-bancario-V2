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
            return saldo, extrato, numero_saques

def imprimirExtrato(saldo, extrato=""):
    if not extrato:
        print("Não foram realizadas movimentações.")
        print(f"----------- \nSaldo Total: R$ {saldo:.2f}")
    else:
        print("-----------Extrato-----------")
        print(extrato)
        print(f"----------- \nSaldo Total: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já cadastrado!")
        return

    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print((linha))

menu = """
Escolha uma opção:
1 - Depositar
2 - Sacar
3 - Imprimir Extrato
4 - Criar Usuário
5 - Criar Conta
6 - Listar Conta
0 - Sair

"""

saldo = 0
extrato = ""
contator_saque = 0
usuarios = []
contas = []
AGENCIA = "0001"

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
    
    elif opcao == "4":
        criar_usuario(usuarios)
    
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        print("Saindo da conta...")
        break    
    else:
        print("Opção inexistente! Selecione outra opção.")



