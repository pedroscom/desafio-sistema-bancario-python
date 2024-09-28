import textwrap

def sacar(*, saldo, extrato, limite_valor_saque, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_valor_saque
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
  
def visualizar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():
    usuario = {}
    usuario["cpf"] = input("Digite seu cpf: ")
    
    for usuario_existente in lista_de_usuarios:
        if usuario_existente["cpf"] == usuario["cpf"]:
            print("Usuário já cadastrado.")
            return
    
    senha = input ("Digite para criar uma nova senha: ")
    confirmar_senha = input ("Confime sua senha: ")

    if senha == confirmar_senha:
        usuario["senha"] = senha
        usuario["nome"] = input("Digite seu nome: ")
        usuario["data_nascimento"] = input("Digite data de nascimento: ")
        usuario["endereco"] = input("Digite seu endereço: ")
        print("Cadastro realizado, use seu CPF e senha digitada pra acessar sua conta.")
        lista_de_usuarios.append(usuario)

    else:
        print("As senha digitadas são diferentes, tente novamente.")
    
def entrar(lista_de_usuarios):
    global usuario_logado
    cpf_digitado = input("Digite seu CPF: ")
    for usuario_existente in lista_de_usuarios:
        if usuario_existente["cpf"] == cpf_digitado:
            senha_digitada = input("Digite sua senha: ")
            if senha_digitada == usuario_existente["senha"]:
                usuario_logado = usuario_existente["nome"]
                print(f"Bem-vindo, {usuario_existente['nome']}!")
                return True
            else:
                print("Senha inválida.")
                return False
    else:
        print("CPF não encontrado.")
        return False
    
def operacoes(menu, saldo, limite_valor_saque, extrato, numero_saques, LIMITE_SAQUES, lista_de_usuarios): # Criei uma função para manipular as operação pós autenticação de usuário.
      
    while True:

        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato) # O Input com o valor do depósito e as tomadas de decisão if-else foram movidas para o bloco da função "Depositar".

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite_valor_saque=limite_valor_saque, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES) # O Input com o valor do saque e as tomadas de decisão if-else foram movidas para o bloco da função "Sacar".

        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)
            
        elif opcao == "c":
            numero_conta = len(contas) + 1
            print("\n=== Conta criada com sucesso! ===")
            contas.append({"usuario": usuario_logado, "agencia": AGENCIA, "numero_conta": numero_conta})
        
        elif opcao == "l":
            for conta in contas:
                print(f"Usuário: {conta['usuario']}, Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

""" def listar_contas(contas):
    print (contas({"usuario": usuario_logado, "agencia": AGENCIA, "numero_conta": numero_conta})) """

numero_conta = []
lista_de_usuarios = []
contas_de_usuario = []
contas = []
AGENCIA = "0001"

menu = """\n  [d] Depositar\n  [s] Sacar\n  [e] Extrato\n  [c] Criar Conta\n  [l] Listar Contas\n  [q] Sair\n\n  =>"""
menu_autenticacao = """\n  [1] Entrar na sua conta\n  [2] Novo Cadastro\n  [0] Sair\n\n  =>"""
saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: # Repetição (Loop) do novo menu de autenticação e cadastro.

    opcao = input(menu_autenticacao)

    if opcao == "1" and entrar(lista_de_usuarios) == True:
            operacoes(menu, saldo, limite_valor_saque, extrato, numero_saques, LIMITE_SAQUES, lista_de_usuarios)

    elif opcao == "2":
        criar_usuario()
        
    elif opcao == "0":
        break

    else:
        print("Operação inválida ou usuário não cadastrado, por favor selecione novamente a operação desejada.")