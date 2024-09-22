# Implementando o sistema bancário do desafio, utilizando função. Sei que não ficou eficiente, fiz com o intuito de praticar.
menu = """\n  [d] Depositar\n  [s] Sacar\n  [e] Extrato\n  [q] Sair\n\n  =>""" # A declaração do texto do "menu" foi compactado, por opção.
saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

cpf_usuario = ""
senha_usuario = ""
menu_autenticacao = """\n  [1] Entrar na sua conta\n  [2] Novo Cadastro\n  [0] Sair\n\n  =>""" # Também compactado para diminuir a linhas totais do código, por questão de gosto.

def Cadastrar(cpf_usuario, senha_usuario): # Função para cadastrar usuário. Problemas: não verifica se usuário já está cadastrado, não verifica se CPF é válido, se a senha é muito curta, um mesmo CPF pode se cadastrar multiplas vezes (acredito que não seja necessário implementar, para a etapa do aprendizado).

    cpf = input("Digite seu CPF: ")
    senha = input ("Digite para criar uma nova senha: ")
    confirmar_senha = input ("Confime sua senha: ")

    if senha == confirmar_senha:
        print("Cadastro realizado, use seu CPF e senha digitada pra acessar sua conta.")
        cpf_usuario = cpf
        senha_usuario = senha

    else:
        print("As senha digitadas são diferentes, tente novamente.")
    
    return cpf_usuario, senha_usuario

def Entrar(cpf_usuario, senha_usuario): # Função para entrar no sistema após ter criado um usuário. Problema: pode se autenticar com senha e usuário vazios (pelo menos facilitou alguns testes).

    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")

    if cpf == cpf_usuario and senha == senha_usuario:
        print("Usuário autenticado!")
        return True

    else:
        print("CPF ou senha inválida(os).")
        return False

def Depositar(saldo, extrato): # Função "Depositar".

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato = Extrato_deposito(valor, extrato)

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def Sacar(saldo, extrato, limite_valor_saque, numero_saques, LIMITE_SAQUES): # Função "Sacar".

    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_valor_saque
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato = Extrato_saque(valor, extrato)
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def Extrato_deposito(valor, extrato): # Foi necessário criar duas função para incrementar as informações do extrato. Essa é para incrimentar os depósitos na variável "extrato".

    extrato += f"Depósito: R$ {valor:.2f}\n"
    
    return extrato

def Extrato_saque(valor, extrato): # Foi necessário criar duas função para incrementar as informações do extrato. Essa é para incrimentar os saques na variável "extrato".

    extrato += f"Saque: R$ {valor:.2f}\n"
    
    return extrato

def Operacoes(menu, saldo, limite_valor_saque, extrato, numero_saques, LIMITE_SAQUES): # Criei uma função para manipular as operação pós autenticação de usuário.
      
    while True:

        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = Depositar(saldo, extrato) # O Input com o valor do depósito e as tomadas de decisão if-else foram movidas para o bloco da função "Depositar".

        elif opcao == "s":
            saldo, extrato, numero_saques = Sacar(saldo, extrato, limite_valor_saque, numero_saques, LIMITE_SAQUES) # O Input com o valor do saque e as tomadas de decisão if-else foram movidas para o bloco da função "Sacar".

        elif opcao == "e": # Porem, não houve alteração daqui pra baixo.
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

while True: # Repetição (Loop) do novo menu de autenticação e cadastro.

    opcao = input(menu_autenticacao)

    if opcao == "1" and Entrar(cpf_usuario, senha_usuario) == True:
            Operacoes(menu, saldo, limite_valor_saque, extrato, numero_saques, LIMITE_SAQUES)

    elif opcao == "2":
        cpf_usuario, senha_usuario = Cadastrar(cpf_usuario, senha_usuario)

    elif opcao == "0":
        break

    else:
        print("Operação inválida ou usuário não cadastrado, por favor selecione novamente a operação desejada.")