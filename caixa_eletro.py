saldo = 1000


def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print(f'SAQUE REALIZADO NO VALOR DE R$ {valor}')
        print(f'VALOR ATUAL DISPONIVEL NA CONTA R$ {saldo}')
    else:
        print('SALDO INSUFICIENTE')
        print(f"SALDO ATUAL DE R$  {saldo}")

def depositar(valor):
    global saldo
    saldo += valor
    print(f'VALOR ATUAL DISPONIVEL NA CONTA R$ {saldo}')

while True:
    print("""========BANCO SILVA========
    
    OPÇÃO[1] - SAQUE

    OPÇÃO[2] - DEPOSITAR

    OPÇAO[0] - EXIT
    """)
    print('===========================')
    opcao = int(input("DIGITE A SUA ESCOLHA: "))
    if opcao == 1:
        valor = float(input("VALOR DESEJADO R$ "))
        sacar(valor)
    elif opcao == 2:
        valor = float(input("VALOR DO DEPOSITO R$ "))
        depositar(valor)
    else:
        print("OBRIGADO, ATE MAIS!")
        break