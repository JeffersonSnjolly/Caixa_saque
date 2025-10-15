import os
import datetime as dt
import functools

AGENCIA = "001"
saldo = 0
extrato = []
num_saques = 0
usuarios = []
contas = []

def decorador_log(funcao):
    @functools.wraps(funcao)
    def envelop(*args, **kwargs):
        retorno = funcao(*args, **kwargs)
       
            
        if os.path.exists("log.txt"):
            log = f"DATA: {dt.datetime.now().strftime("%Y - %m -%d %H:%M:%S")}, Nome da função: {funcao.__name__}, Argumentos {args} e {kwargs} , Retorno : {retorno}\n"
            with open(os.path.join("log.txt"), "a", encoding='utf8') as arq:
                arq.write(log) 
             
        else:
            log = f"DATA: {dt.datetime.now().strftime("%Y - %m -%d %H:%M:%S")}, Nome da função: {funcao.__name__}, Argumentos {args} e {kwargs} , Retorno: {retorno}\n"
            with open(os.path.join("log.txt"), "w", encoding='utf-8') as arq:
                arq.write(log)
        return retorno
    return envelop
    
@decorador_log
def depositar(valor):
    global saldo, num_saques
    if valor > 0:
        saldo += valor
        print(f"Deposito realizado com sucesso R${valor}")
        extrato.append({"transacao":depositar.__name__,"valor":valor, "Data":dt.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")})
        
    else:
        print("Operação invalida.")   
    

@decorador_log
def sacar(valor):
    global saldo, num_saques
    if valor > 0 and valor <= saldo:
        if num_saques <= 3:
            saldo -= valor
            print(f"Saque realizado com sucesso R${valor}")
            num_saques += 1
            extrato.append({f"transacao":sacar.__name__, "valor":valor, "Data":dt.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")})
        else: 
            print("Numeros de saques excedido")
    else:
        print("Operação invalida.")     

def extratos():
    print("*"*25 + " EXTRATO "+"*"*25)
    for i in extrato:
        print(f"|{i}|")
    print("*"*59)
    

@decorador_log
def criar_usuario(usuarios):
    cpf =  input("Informe seu cpf -> ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe esse CPF cadastrado em nosso sistema")
        return
        
    nome = input("Informe o nome completo -> ")
    data_nascimento = input("informe a data de nascimento -> ")
    endereco = input("Informe o endereço (rua, nro - bairro - cidade/sigla estado) ->")
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
    print("Usuário cadastrado com sucesso")    

def filtrar_usuario(cpf, usuarios):
    filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return filtrados[0] if filtrados else None
    
@decorador_log
def criar_conta(agencia, numero_conta ,usuarios):
    cpf = input("Informe o CPF -> ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso")
        return {'agencia':agencia,"numero_conta":numero_conta,"usuario":usuario}
    else:
        print("Usuario não encontrado, processo de criação de conta cancelado.")

def listar_contas(contas):
    print("*"*25 + " Contas "+"*"*25)
    for conta in contas:
        print(f"Agência: {conta['agencia']}, C/C: {conta["numero_conta"]}, Usuario: {conta["usuario"]}")
    print("*"*59)
    
    
    
while True:
    print("""
d -  Depositar.
s -  Sacar.
e -  Extrato.
nc - Nova conta
lc - Listar contas
nu - Novo ususário
q -  Sair""")
    
    op = input("-> ").lower()
    if op == "q":
        print("Até mais...")
        break
    if op == "d":
        valor = float(input("Digite o valor -> "))
        depositar(valor)
        input()
        os.system("cls")
        
    elif op == "s":
        valor = float(input("Digite o valor -> "))
        sacar(valor)
        input()
        os.system("cls")
    elif op == "e":
        extratos()
        input()
        os.system("cls") 
    
    elif op == "nu":
        criar_usuario(usuarios)
        input()
        os.system("cls")
    elif op == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
        input()
        os.system("cls") 
        
    elif op == "lc":
        listar_contas(contas)
        input()
        os.system("cls")        
        
    else:
        print("Opção invalida.")
        input()
        os.system("cls") 
        continue   
