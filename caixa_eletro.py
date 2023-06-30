saldo = 1000
extrato = []

def Sacar(valor):
    global saldo, extrato
    
    if saldo >= valor:
        saldo -= valor
        extrato.append(f"SAQUE: R$ {valor}")
        print(f'SAQUE REALIZADO NO VALOR DE R$ {valor}')
        print(f'VALOR ATUAL DISPONIVEL NA CONTA R$ {saldo}')    
    else:
        print('SALDO INSUFICIENTE')
        print(f"SALDO ATUAL DE R$  {saldo}")

def Depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato.append(f"DEPOSITO: R$ {valor}")
    print(f'VALOR ATUAL DISPONIVEL NA CONTA R$ {saldo}')

def Extrato():
    for i in extrato:
        print(i)

limete_saq = 0
while True:
    print("""========BANCO SILVA========
    
    OPÇÃO[1] - DEPOSITAR

    OPÇÃO[2] - SACAR

    OPÇAO[3] - EXTRATO

    OPCAO[0] - SAIR
    """)
    print('===========================')
    opcao = input("DIGITE A SUA ESCOLHA: ")
    if opcao == "1" :
        valor = float(input("VALOR DO DEPOSITO: R$ "))
        Depositar(valor)
    elif opcao == "2":
        if limete_saq < 3:
            valor = float(input("VALOR A SACAR: R$ "))
            limete_saq += 1
            Sacar(valor)
    elif limete_saq > 3:
        print("LIMITE DE SAQUE ATIGINDO!")
    elif opcao == "3":
        Extrato()
    elif opcao =="0":
        break
    else:
        print("OPÇÃO INVALIDA, TENTE NOVAMENTE")
        