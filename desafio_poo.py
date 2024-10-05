from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass
    
class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    
    def registrar(self, conta: Conta):
        conta._saldo += self._valor
    
class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    
    def registrar(self, conta: Conta):
        if conta._saldo >= self._valor:
            conta._saldo -= self._valor
            return True
        return False
    
class Historico:
    def __init__(self):
        self._transacao = []
        
    def adicionar_transacao(self, transacao: Transacao):
        self._transacao.append(transacao)
        
class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = 0001
        self._cliente = cliente
        self._historico = Historico()
        
    def saldo(self):
        return self._saldo
    
    @staticmethod
    def nova_conta(cliente: Cliente, numero: int):
        conta = Conta(cliente, numero)
        cliente.adicionar_conta(conta)
        return conta
        
    def sacar(self, valor: float):
        pass
    
    def depositar(self, valor: float)
        pass
        

class Cliente:
    def __init__(self, endereco) -> None:
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)
    

        
    


