import os

def menu():
    MENU ="""======================Banco Silva Tech======================

        [D]  DEPOSITAR
        [S]  SACAR
        [E]  EXTRATO
        [NC] NOVA CONTA
        [LC] LISTAR CONTAS
        [NU] NOVO USUÁRIO
        [Q]  SAIR:

        ============================================================ 
        DIGITE : """
    return input(MENU)

saldo = 0
LIMITE_VALOR = 500
extrato  = []
saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = menu().upper()
    os.system('cls')
    if opcao == 'D':
        while True:
            try:    
                valor  = float(input('DIGITE O VALOR DO DEPOSITO R$ '))
                os.system('cls')
                if valor > 0:
                    config = input(f"""DEPOSITO NO VALOR DE  R${valor} ESTÁ CORRETO?
                                    [S] SIM
                                    [N] NÃO 
                                    DIGITE : """).upper()
                    os.system('cls')
                    if config == 'S':
                        saldo += valor
                        extrato.append(f'DEPOSITO DE {valor:.2f}')
                        print('SUCESSO NA OPERAÇÃO.')
                        print(f'SALDO EM CONTA {saldo:.2f}')
                        input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
                        os.system('cls')
                        break
                    elif config == 'N':
                        tentativa = input("""DESEJA TENTAR NOVAMENTE ?
                                        [S] SIM
                                        [N] NÃO
                                        DIGITE : """).upper()
                        os.system('cls')
                        if tentativa != 'S':
                            break     
            except:                   
                print('DIGITE APENAS VALORES NUMÉRICOS....')
                input()
                os.system('cls')
                break                          
    elif opcao == 'S':
        while True:
            try:
                saque = float(input("VALOR DESEJADO R$ "))
                os.system('cls')
                config_2 = input(f"""SAQUE NO VALOR DE  R${saque} ESTÁ CORRETO?
                                    [S] SIM
                                    [N] NÃO 
                                    DIGITE : """).upper()
                os.system('cls')
                if config_2 == 'S':
                    if (saldo > 0) & (saldo >= saque) & (saque <= LIMITE_VALOR) & (saques < LIMITE_SAQUE):
                        saldo -= saque
                        extrato.append(f'SAQUE DE {saque:.2f}')
                        saques +=1                    
                        print('SAQUE REALIZADO COM SUCESSO')
                        print(f'SALDO {saldo:.2f}')
                        input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
                        os.system('cls')
                        break
                    elif saque > LIMITE_VALOR:
                        print('VALOR EXCEDIDO...')
                        input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
                        os.system('cls')
                        break
                    elif saques  == LIMITE_SAQUE:
                        print('LIMITE EXCEDIDO...')
                        input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
                        os.system('cls')
                        break
                    elif saldo < saque:
                        print('SALDO EM CONTA EXCEDIDO...')
                        print(f'SALDO EM CONTA {saldo:.2f}')
                        input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
                        os.system('cls')
                        break    
                    elif config_2 == 'N':
                        tentativa = input("""DESEJA TENTAR NOVAMENTE ?
                                        [S] SIM
                                        [N] NÃO
                                        DIGITE : """).upper()
                        os.system('cls')
                        if (tentativa != 'S') or (tentativa != 'N'):
                            break
            except:
                print('DIGITE APENAS VALORES NUMÉRICOS....')
                input()
                os.system('cls')
                break           
    elif opcao == 'E':
        if len(extrato) > 0:
            for i in extrato:
                print(i)
            input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
            os.system('cls') 
        else:
            print('NÃO TEMOS EXTRATO...')
            input('APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL... ')
            os.system('cls') 
    elif opcao  == 'Q':
        break
